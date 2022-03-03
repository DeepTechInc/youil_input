from socket import AddressFamily
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from numpy import average, spacing
from .models import *
from django.db import connection, reset_queries
from .forms import *
from django.contrib import messages
from django import forms
rows_master = []
rows_detail = []
workorderinput_index = 0
# Create your views here.

def After_add(request, id):
    search_form = searchForm()
    add_form = addForm()
    global rows_master
    global rows_detail
    global workorderinput_index
    
    if request.method == 'POST':
        #   "AFTER ADD, POST RECEIVED")
        Base(request, id)

    cursor = connection.cursor()
    strsql = f'''SELECT 
                        a.workorderinput_index
                        , a.workorder_index
                        , a.row_production_LOT
                        , a.goodsnum_index
                        , a.goodsnum_name
                        , b.sample_type_code
                        , case when sample_type_code = 0 then '도금두께'
                            when sample_type_code = 1 then 'Sn함량70%이상'
                            when sample_type_code = 2 then 'Zn함량 나머지' END sample_typ_name
                        , b.x1 x1
                        , b.x2 x2
                        , b.x3 x3
                        , b.x4 x4
                        , b.x5 x5
                        , b.input_datetime intput_time
                        , b.complete_datetime complete_time 
                        FROM spc22_inspectiontable a INNER JOIN spc22_inspectioninputtable b
                        on a.inspection_index = b.inspection_index
                        AND a.workorderinput_index =  {id} 
                        LEFT OUTER JOIN mes_goodsnumtable c
                    ON a.goodsnum_index = c.goodsnum_index
                    ORDER BY b.inspectioninput_index
        
        '''
    result = cursor.execute(strsql)
    datas = cursor.fetchall()
    
    connection.commit()
    connection.close()
    
    rows_detail = []
    
    rownum = 0
    
    for data in datas:                    
        d_range = [data[7], data[8], data[9], data[10],data[11]]
        d_min = min(d_range)
        d_max = max(d_range)
        d_sum = sum(d_range)
        d_avg = d_sum/5
        d_range = d_max - d_min
        rownum = rownum + 1
        val = {'id': rownum,
            'sample_type': data[7],
            'x1': data[7],
            'x2': data[8],
            'x3': data[9],
            'x4': data[10],
            'x5': data[11],
            'min': d_min,
            'max': d_max,
            'avg': d_avg,
            'range': d_range, 
            'inputtime': data[12],
            'completetime': data[13],
            'workorderinput_index':id
            }
        rows_detail.append(val)
    
    
    # print('(AFTER_ADD)rows_detail', rows_detail)
    context = {'s_form': search_form,
               'a_form': add_form,
               'rows_master': rows_master,
               'rows_detail': rows_detail, 
               }   
    
    return render(request, 'base.html', context)    



def Base(request, id=None):
    search_form = searchForm()
    add_form = addForm()
    global rows_master
    global rows_detail
    global workorderinput_index
    cursor = connection.cursor()

    
    if request.method == 'POST':
        # 데이터 등록
        s_param = request.POST
        if not s_param['x1']:
        # if not input_data.is_valid():
            work_id = workorderinput_index            
            messages.info(request, '값이 비었습니다.')
            return HttpResponseRedirect(f'{work_id}/')
        else:
            x1 = s_param['x1']
            x2 = s_param['x2']
            x3 = s_param['x3']
            x4 = s_param['x4']
            x5 = s_param['x5']
            input_datetime = s_param['input_datetime']
            complete_datetime = s_param['complete_datetime']
            
            # QUERY 0 : get gildStandard
            strSql = f'''
            SELECT a.gildStandard
            FROM mes_goodsnumtable a, mes_workorderinputtable b, mes_workordertable c
            WHERE b.workorderinput_index = {workorderinput_index}
            AND a.goodsnum_index = c.goodsnum_index
            AND b.workorder_index = c.workorder_index
            '''
            
            result = cursor.execute(strSql)
            datas = cursor.fetchall()                    
            gildStandard = datas[0][0]
            
            print('query 1')
            # QUERY 1
            strSql = f'''
            INSERT INTO spc22_inspectiontable (
                    workorder_index
                , workorderinput_index
                , production_line
                , row_production_lot
                , goodsnum_index
                , goodsnum_name
                , complete_datetime
                , writer
                )
            SELECT
                    a.workorder_index
                , b.workorderinput_index
                , b.production_line
                , b.row_production_LOT
                , a.goodsnum_index
                , c.goodsnum_name
                , b.complete_datetime
                , 'DEEPTECH'                
            FROM mes_workordertable a INNER JOIN mes_workorderinputtable b 
            ON a.workorder_index = b.workorder_index
            AND b.workorderinput_index = {workorderinput_index}
            LEFT OUTER JOIN mes_goodsnumtable C
            ON a.goodsnum_index = c.goodsnum_index;
            '''
            result = cursor.execute(strSql)
            
            print('query 2')
            # Query 2            
            strSql = f'''
            SELECT inspection_index
            FROM spc22_inspectiontable
            WHERE workorderinput_index = {workorderinput_index}
            '''
            result = cursor.execute(strSql)            
            data = cursor.fetchall()
            inspection_index = data[-1][0]
            
            print('query 3')
            # Query 3
            strSql = strSql_m = f'''
            INSERT INTO spc22_inspectioninputtable(
                inspection_index, input_datetime, complete_datetime
                , x1, x2, x3, x4, x5, writer, gildStandard) 
            VALUES ('{inspection_index}', '{input_datetime}', '{complete_datetime}'
                , {x1}, {x2}, {x3}, {x4}, {x5}
                , 'DEEPTECH', {gildStandard});
            '''
            print(strSql)
            result = cursor.execute(strSql)                        
            

            connection.commit()
            connection.close()
            work_id = workorderinput_index            
            workorderinput_index = 0
            
            return redirect(f'/youil/{work_id}/')

    
    elif request.method == 'GET':
        s_param = request.GET
        # print('s_param', s_param)
        
        if 'data_for_detail' in s_param:
            # 마스터 데이터 선택 후 디테일 출력
            workorderinput_index = request.GET['workorderinput_index']
            # print('workorderinput_index', workorderinput_index)
            strsql = f'''SELECT
                                a.workorderinput_index
                                , a.workorder_index
                                , a.row_production_LOT
                                , a.goodsnum_index
                                , a.goodsnum_name
                                , b.sample_type_code
                                , case when sample_type_code = 0 then '도금두께'
                                    when sample_type_code = 1 then 'Sn함량70%이상'
                                    when sample_type_code = 2 then 'Zn함량 나머지' END sample_typ_name
                                , b.x1 x1
                                , b.x2 x2
                                , b.x3 x3
                                , b.x4 x4
                                , b.x5 x5
                                , b.input_datetime intput_time
                                , b.complete_datetime complete_time 
                                FROM spc22_inspectiontable a INNER JOIN spc22_inspectioninputtable b
                                on a.inspection_index = b.inspection_index
                                AND a.workorderinput_index =  {workorderinput_index} 
                                LEFT OUTER JOIN mes_goodsnumtable c
                            ON a.goodsnum_index = c.goodsnum_index
                            ORDER BY b.inspectioninput_index
                
                '''
            result = cursor.execute(strsql)
            datas = cursor.fetchall()

            connection.commit()
            connection.close()           
            
            rows_detail = []

            for data in datas:
                # print("두꼐?", data[7:12])
                d_range = [ data[7], data[8], data[9], data[10], data[11] ]
                d_min = min(d_range)
                d_max = max(d_range)
                d_sum = sum(d_range)
                d_avg = d_sum/5
                d_range = d_max - d_min
                row = { 'sample_type': data[6],
                        'x1': data[7],
                        'x2': data[8],
                        'x3': data[9],
                        'x4': data[10],
                        'x5': data[11],
                        'min': d_min,
                        'max': d_max,
                        'avg': d_avg,
                        'range':d_range,
                        'inputtime': data[12],             
                        'completetime': data[13],
                        'workorderinput_index':request.GET['workorderinput_index']
                }
                rows_detail.append(row)
                
                # print('rows_detail', rows_detail)
            # print('rows_detail --\n', rows_detail)
                    
        else:
            # 초기 or 검색 후
            if 'data_for_search' in s_param:
                rows_detail = []
            strsql = f'''           
                SELECT
                    a.workorder_index
                    , b.workorderinput_index
                    , a.goodsnum_index
                    , c.goodsnum_code
                    , c.goodsnum_name
                    , a.production_date
                    , b.row_production_LOT # lot_no
                    , case when b.production_line = '1' then '자동라인'
                        when  b.production_line = '2' then '수동라인'
                        when  b.production_line = '3' then '합금라인'
                        when  b.production_line = '4' then 'Tank 라인'
                        when  b.production_line = '5' then '착색라인'
                        when  b.production_line = '7' then '은라인'
                        when  b.production_line = '8' then '무전해'
                        when  b.production_line = '9' then '인산피막염'
                        when  b.production_line = '11' then '재고정리'
                        when  b.production_line = '12' then '세척라인'
                        when  b.production_line = '13' then '광택주석라인' END production_line
                    , case when b.completeyn = '0' then '투입'
                        when b.completeyn = '11' then '중간완료'
                        when b.completeyn = '1' then '완료' END completeyn #workorder_staus
                FROM mes_workordertable a INNER JOIN mes_workorderinputtable b 
                ON a.workorder_index = b.workorder_index'''
                
            if 'lot_no' in s_param and s_param['lot_no'] != '':
                strsql += f"\nAND b.row_production_lot LIKE CONCAT('%', '{s_param['lot_no']}', '%')"

            
            if 'date_start' in s_param and 'date_start' in s_param:
                strsql += f"\nAND a.production_date between '{s_param['date_start']}' AND '{s_param['date_end']}'"
            
            if 'line_index' in s_param and s_param['line_index'] != '':
                strsql += f"\nAND b.production_line = '{s_param['line_index']}'"

                            
            strsql += f'''
            LEFT OUTER JOIN mes_goodsnumtable C
            ON a.goodsnum_index = c.goodsnum_index
            WHERE 1=1 '''

            if 'text_goodsnum' in s_param and s_param['text_goodsnum'] != '':
                if s_param['select_goodsnum'] == 's_goodsnum_code':
                    strsql += f"AND c.goodsnum_code LIKE CONCAT('%', '{s_param['code_goodsnum']}', '%') "
                else:
                    strsql += f"AND c.goodsnum_name LIKE CONCAT('%', '{s_param['text_goodsnum']}', '%') "                
            
            strsql += f'''
                ORDER BY a.production_date DESC
                LIMIT 1000
            '''
            
            result = cursor.execute(strsql)
            datas = cursor.fetchall()
            connection.commit()
            connection.close()

            rows_master = []
            
            for data in datas:
                row = {'workorderinput_index':data[1],
                    'production_date':data[5],
                    'goodsnum_name':data[4],
                    'row_production_lot':data[6],
                    'production_line':data[7],
                    'completeyn':data[8],
                }
                rows_master.append(row)
    
    context = {
            'rows_master': rows_master,
            'rows_detail': rows_detail,
            's_form': search_form,
            'a_form': add_form,
        }        
    # print('rows_detail', context['rows_detail'])
    # print('rows_master', context['rows_master'])
    return render(request, 'base.html', context)

from django import forms
from django.forms import ModelForm
from django import forms
from django.forms.fields import ChoiceField
from django.forms.widgets import TextInput
# from django import forms
from .models import *
from datetime import datetime

class myForm(ModelForm):
    class Meta:
        model = Spc22Inspectioninputtable
        fields = ['inspectioninput_index',
                  'inspection_index',
                  'sample_type_code',
                  'input_datetime',
                  'complete_datetime',
                  'x1',
                  'x2',
                  'x3',
                  'x4', 
                  'x5',
                  'writer',
                  'reg_datetime']
        # fields = '__all__'
        widgets = {
            'inspection_index': TextInput(attrs={'class':'m-input', 'maxlength':'10'}),
            'x1': TextInput(attrs={'size': 3}),
            'x2': TextInput(attrs={'class':'m-input'}),
            'x3': TextInput(attrs={'size': 3}),
            'x4': TextInput(attrs={'size': 3}),
            'x5': TextInput(attrs={'size': 3}),
        }

class searchForm(forms.Form):
    DAY_CHOICES = (        
        ('10', '금일'),
        ('20', '전일'),
        ('30', '1 주일'),
        ('40', '2 개월'),
        ('50', '3 개월')
        )
    GOODSNUM_CHOICES = (
        ('s_goodsnum_name', '제품명'),
        ('s_goodsnum_code', '제품코드')        
        )
    ORDG_STAT_CHOICES = (
        ('0', '투입'),
        ('11', '중간완료'),
        ('1', '완료')
        )
    LINE_INDEX_CHOICES = (
        ('1', '자동라인'),
        ('2', '수동라인'),
        ('4', 'Tank 라인'),
        ('5', '착색라인'),
        ('7', '은라인'),
        ('3', '합금라인'),
        ('8', '무전해'),
        ('12', '세척라인'),
        ('9', '인산피막염'),
        ('13', '광택주석라인'),
        ('11', '재고정리'),
    )
    select_count_day = forms.ChoiceField(choices=DAY_CHOICES,
                                    widget=forms.Select(attrs={'class':'m-select', 'id':'dt_stat', 'onchange':"dateChange('dt_stat','stt_dt','end_dt')"}))
    
    date_start = forms.CharField(
        widget=forms.TextInput(attrs={
            'type':'text',
            'class':'datepicker m-calendar',
            'id':'stt_dt',
            'readonly':'True'
        })
    )
    date_end = forms.CharField(
        widget=forms.TextInput(attrs={
            'type':'text',
            'class':'datepicker m-calendar',
            'id':'end_dt',
            'readonly':'True'
        })
    )
    lot_no = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'m-input',
                                                           'maxlength':'50',
                                                           'id':'odrg_chpr_nm'}))
    select_goodsnum = forms.ChoiceField(choices=GOODSNUM_CHOICES,
                                    widget=forms.Select(attrs={'class':'m-select', 'id':'search_type'}))
    text_goodsnum = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'m-input',
                                                                   'id':'search_value',
                                                                'maxlength':'50'}))
    # select_ordg_stat = forms.ChoiceField(choices=ORDG_STAT_CHOICES,
    #                                 widget=forms.Select(attrs={'class':'m-select', 'id':'search_type'}))
    line_index = forms.ChoiceField(choices=LINE_INDEX_CHOICES,
                                    widget=forms.Select(attrs={'class':'m-select', 'id':'search_type'}))
    data_for_search = forms.CharField(widget=forms.HiddenInput(attrs={'value':'SEARCH'}))

class addForm(forms.Form):
    x1 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'m-input',
                                                                       'maxlength':'50',
                                                                       'id':'odrg_chpr_nm'}))
    
    x2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'m-input',
                                                                       'maxlength':'50',
                                                                       'id':'odrg_chpr_nm'}))
    
    x3 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'m-input',
                                                                       'maxlength':'50',
                                                                       'id':'odrg_chpr_nm'}))
    
    x4 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'m-input',
                                                                       'maxlength':'50',
                                                                       'id':'odrg_chpr_nm'}))
    
    x5 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'m-input',
                                                                       'maxlength':'50',
                                                                       'id':'odrg_chpr_nm'}))
    
    input_datetime = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'m-input',
                                                                       'maxlength':'50',
                                                                       'id':'odrg_chpr_nm'}))
    
    complete_datetime = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'m-input',
                                                                       'maxlength':'50',
                                                                       'id':'odrg_chpr_nm'}))
    
    # input_datetime = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'value': datetime.today().strftime("%Y%m%d%H%M%S")})) 
    # complete_datetime = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'value': datetime.today().strftime("%Y%m%d%H%M%S")})) 
    data_for_add = forms.CharField(widget=forms.HiddenInput(attrs={'value':'ADD'})) 
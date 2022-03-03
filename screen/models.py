from django.db import models

# Create your models here.
class MesGoodsnumtable(models.Model):
    goodsnum_index = models.IntegerField(primary_key=True)
    goodsnum_code = models.CharField(unique=True, max_length=50)
    goodsnum_name = models.CharField(max_length=50)
    goodsnumgroup_index = models.IntegerField(blank=True, null=True)
    customer_index = models.IntegerField()
    goodsnum_customer = models.CharField(max_length=50, blank=True, null=True)
    goodstype_index = models.IntegerField(blank=True, null=True)
    gildtype = models.CharField(db_column='gildType', max_length=50)  # Field name made lowercase.
    standard = models.CharField(max_length=250, blank=True, null=True)
    unit = models.CharField(max_length=20)
    output_unit = models.CharField(max_length=20)
    goodsnum_unit_name = models.CharField(max_length=50, blank=True, null=True)
    result_table = models.IntegerField()
    youilnumber = models.CharField(db_column='youilNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gildstandard = models.CharField(db_column='gildStandard', max_length=50, blank=True, null=True)  # Field name made lowercase.
    goodsclassify_index1 = models.CharField(max_length=50)
    goodsclassify_index2 = models.CharField(max_length=50)
    goodsclassify_index3 = models.CharField(max_length=50)
    accrue_in_amount = models.FloatField(blank=True, null=True)
    accrue_out_amount = models.FloatField(blank=True, null=True)
    indate = models.DateTimeField(blank=True, null=True)
    outdate = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    useyn = models.IntegerField()
    fileupload = models.CharField(max_length=100)
    historyindex = models.IntegerField()
    autobarrel = models.IntegerField(blank=True, null=True)
    line_index = models.IntegerField()
    safe_amount = models.FloatField(blank=True, null=True)
    alarmyn = models.IntegerField(blank=True, null=True)
    unit_name = models.CharField(max_length=50, blank=True, null=True)
    goodsnum_output_unit_name = models.CharField(max_length=50, blank=True, null=True)
    output_rate = models.FloatField(blank=True, null=True)
    rack_charging_cnt = models.IntegerField()
    rack_unit = models.CharField(max_length=50)
    power = models.IntegerField()
    power_unit = models.CharField(max_length=50)
    gildtime = models.IntegerField(db_column='gildTime')  # Field name made lowercase.
    gildtime_unit = models.CharField(max_length=50)
    rack_img = models.CharField(max_length=100, blank=True, null=True)
    material_width = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    stand_unitcost = models.BigIntegerField(blank=True, null=True)
    process = models.CharField(max_length=50, blank=True, null=True)
    subm_shape = models.CharField(max_length=150, blank=True, null=True)
    subm_case_size = models.CharField(max_length=150, blank=True, null=True)
    material_type = models.CharField(max_length=150, blank=True, null=True)
    works_type = models.CharField(max_length=150, blank=True, null=True)
    chemical_polishing = models.CharField(max_length=150, blank=True, null=True)
    sanding = models.CharField(max_length=150, blank=True, null=True)
    unit_weight = models.CharField(max_length=150, blank=True, null=True)
    apply_field = models.CharField(max_length=150, blank=True, null=True)
    car_type = models.CharField(max_length=150, blank=True, null=True)
    model_name = models.CharField(max_length=150, blank=True, null=True)
    carrier_amt = models.CharField(max_length=150, blank=True, null=True)
    shineyn = models.CharField(max_length=50, blank=True, null=True)
    gildthick_insidespec = models.CharField(max_length=50, blank=True, null=True)
    each_amount = models.CharField(max_length=50, blank=True, null=True)
    order_amount = models.CharField(max_length=50, blank=True, null=True)
    goodsnum_thick = models.CharField(max_length=50, blank=True, null=True)
    goodsnum_thick_unit = models.CharField(max_length=50, blank=True, null=True)
    goodsnum_width = models.CharField(max_length=50, blank=True, null=True)
    goodsnum_width_unit = models.CharField(max_length=50, blank=True, null=True)
    goodsnum_weight = models.CharField(max_length=50, blank=True, null=True)
    goodsnum_weight_unit = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mes_goodsnumtable'

class MesWorkorderinputtable(models.Model):
    workorderinput_index = models.IntegerField(primary_key=True)
    workorder_index = models.IntegerField()
    injection_lot = models.CharField(db_column='injection_LOT', max_length=50)  # Field name made lowercase.
    input_amount = models.FloatField()
    carrier_amount = models.IntegerField()
    inspect_amount = models.FloatField()
    complete_amount = models.FloatField()
    input_time = models.CharField(max_length=50)
    input_datetime = models.DateTimeField(blank=True, null=True)
    completeyn = models.IntegerField()
    production_line = models.CharField(max_length=10)
    datainput = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=2048, blank=True, null=True)
    historyindex = models.IntegerField()
    complete_time = models.CharField(max_length=50, blank=True, null=True)
    complete_datetime = models.DateTimeField(blank=True, null=True)
    noinput_reason = models.CharField(max_length=255, blank=True, null=True)
    lose_amount = models.FloatField(blank=True, null=True)
    ng_amount = models.FloatField(db_column='NG_amount', blank=True, null=True)  # Field name made lowercase.
    ng_reason = models.CharField(db_column='NG_reason', max_length=250, blank=True, null=True)  # Field name made lowercase.
    row_production_lot = models.CharField(db_column='row_production_LOT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    process_injection_result = models.CharField(max_length=250, blank=True, null=True)
    process_injection_remark = models.IntegerField()
    gildtype_thick = models.CharField(db_column='gildType_thick', max_length=20, blank=True, null=True)  # Field name made lowercase.
    qualityyn = models.IntegerField()
    qualityshipyn = models.IntegerField(blank=True, null=True)
    barcode = models.CharField(max_length=50, blank=True, null=True)
    process_inspection_deg1 = models.CharField(max_length=10, blank=True, null=True)
    process_inspection_deg2 = models.CharField(max_length=10, blank=True, null=True)
    process_inspection_deg3 = models.CharField(max_length=10, blank=True, null=True)
    process_inspection_deg_result = models.CharField(max_length=10, blank=True, null=True)
    process_inspection_app1 = models.CharField(max_length=10, blank=True, null=True)
    process_inspection_app2 = models.CharField(max_length=10, blank=True, null=True)
    process_inspection_app3 = models.CharField(max_length=10, blank=True, null=True)
    process_inspection_app_result = models.CharField(max_length=10, blank=True, null=True)
    process_inspection_thick1 = models.CharField(max_length=10, blank=True, null=True)
    process_inspection_thick2 = models.CharField(max_length=10, blank=True, null=True)
    process_inspection_thick3 = models.CharField(max_length=10, blank=True, null=True)
    process_inspection_thick4 = models.CharField(max_length=10, blank=True, null=True)
    process_inspection_thick5 = models.CharField(max_length=10, blank=True, null=True)
    process_inspection_thick_result = models.CharField(max_length=10, blank=True, null=True)
    drop_check_yn = models.IntegerField()
    complete_amount_2ndunit = models.FloatField(blank=True, null=True)
    process_inspection_datetime = models.DateTimeField(blank=True, null=True)
    work_vc = models.CharField(max_length=10, blank=True, null=True)
    work_va = models.CharField(max_length=10, blank=True, null=True)
    work_vc1 = models.CharField(max_length=50, blank=True, null=True)
    work_va1 = models.CharField(max_length=50, blank=True, null=True)
    work_vc2 = models.CharField(max_length=50, blank=True, null=True)
    work_va2 = models.CharField(max_length=50, blank=True, null=True)
    work_vc3 = models.CharField(max_length=50, blank=True, null=True)
    work_va3 = models.CharField(max_length=50, blank=True, null=True)
    contract_index = models.IntegerField(blank=True, null=True)
    reg_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mes_workorderinputtable'


class MesWorkordertable(models.Model):
    workorder_index = models.IntegerField(primary_key=True)
    workorder_number = models.CharField(max_length=50)
    workorder_inputdate = models.DateTimeField()
    productionplan_date = models.DateTimeField()
    production_date = models.DateTimeField()
    goodsnum_index = models.IntegerField()
    customer_index = models.IntegerField()
    production_line = models.CharField(max_length=50)
    plan_amount = models.FloatField()
    plan_time = models.IntegerField()
    othercontract_index = models.IntegerField()
    order_note = models.CharField(max_length=200)
    completeyn = models.IntegerField()
    workorder_staus = models.IntegerField()
    work_no = models.CharField(max_length=50, blank=True, null=True)
    lot_no = models.CharField(max_length=50, blank=True, null=True)
    writer = models.CharField(max_length=50, blank=True, null=True)
    historyindex = models.IntegerField()
    contract_index = models.IntegerField()
    row_material_lot = models.CharField(db_column='row_material_LOT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(max_length=50, blank=True, null=True)
    forecast_time = models.CharField(max_length=50, blank=True, null=True)
    reg_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mes_workordertable'

class Spc22Inspectioninputtable(models.Model):
    inspectioninput_index = models.AutoField(primary_key=True)
    inspection_index = models.IntegerField()
    sample_type_code = models.IntegerField()
    input_datetime = models.CharField(max_length=50, blank=True, null=True)
    complete_datetime = models.CharField(max_length=50, blank=True, null=True)
    x1 = models.FloatField(blank=True, null=True)
    x2 = models.FloatField(blank=True, null=True)
    x3 = models.FloatField(blank=True, null=True)
    x4 = models.FloatField(blank=True, null=True)
    x5 = models.FloatField(blank=True, null=True)
    writer = models.CharField(max_length=50, blank=True, null=True)
    reg_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spc22_inspectioninputtable'


class Spc22Inspectiontable(models.Model):
    inspection_index = models.AutoField(primary_key=True)
    workorderinput_index = models.IntegerField()
    workorder_index = models.IntegerField()
    production_line = models.CharField(max_length=50)
    row_production_lot = models.CharField(db_column='row_production_LOT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qualityyn = models.IntegerField()
    goodsnum_index = models.IntegerField()
    goodsnum_name = models.CharField(max_length=50)
    complete_datetime = models.DateTimeField(blank=True, null=True)
    writer = models.CharField(max_length=50)
    reg_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spc22_inspectiontable'
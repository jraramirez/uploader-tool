# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class StgTransitionbw(models.Model):
    id = models.BigIntegerField(primary_key=True)
    service_month = models.TextField(db_column='Service Month', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    manager_email = models.TextField(db_column='Manager Email', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_id = models.TextField(db_column='Employee ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_name = models.TextField(db_column='Employee Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_email = models.TextField(db_column='Employee Email', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    p_g_level = models.TextField(db_column='P&G Level', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    daily_expected_hours = models.TextField(db_column='Daily Expected Hours', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_type = models.TextField(db_column='Employee Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bill_to_country = models.TextField(db_column='Bill to Country', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    geography = models.TextField(db_column='Geography', blank=True, null=True)  # Field name made lowercase.
    hp_level = models.TextField(db_column='HP Level', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seat_country_code = models.TextField(db_column='Seat Country Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seat_country = models.TextField(db_column='Seat Country', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wbs = models.TextField(db_column='WBS', blank=True, null=True)  # Field name made lowercase.
    wbs_description = models.TextField(db_column='WBS Description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aa_type = models.TextField(db_column='AA Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    attribute = models.TextField(db_column='Attribute', blank=True, null=True)  # Field name made lowercase.
    attribute_2 = models.TextField(db_column='Attribute 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    short_text = models.TextField(db_column='Short Text', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hp_labor_rate = models.TextField(db_column='HP Labor Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    usd_labor_currency = models.TextField(db_column='USD / Labor Currency', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hours = models.TextField(db_column='Hours', blank=True, null=True)  # Field name made lowercase.
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'STG_TRANSITIONBW'


class StgItoPdoEmpList(models.Model):
    id = models.BigIntegerField(primary_key=True)
    month = models.CharField(db_column='Month', max_length=255, blank=True, null=True)  # Field name made lowercase.
    employee_id = models.CharField(db_column='Employee ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    region = models.CharField(db_column='Region', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pm_name = models.CharField(db_column='PM Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_date = models.CharField(max_length=255, blank=True, null=True)
    test = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'STG_ITO_PDO_EMP_LIST'


class StgPgStructures(models.Model):
    id = models.IntegerField(primary_key=True)
    wbs_element = models.CharField(db_column='WBS element', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_code_2 = models.CharField(db_column='User code 2', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'STG_PG_STRUCTURES'


class StgHpLedActuals(models.Model):
    id = models.BigIntegerField(primary_key=True)
    record_id_field = models.CharField(db_column='Record ID#', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    period = models.CharField(db_column='Period', max_length=255, blank=True, null=True)  # Field name made lowercase.
    service_date = models.CharField(db_column='Service Date', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    initial_workgroup = models.CharField(db_column='Initial Workgroup', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    updated_workgroup_name = models.CharField(db_column='Updated Workgroup Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    initial_resource_name = models.CharField(db_column='Initial Resource Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fte = models.CharField(db_column='FTE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updated_fte = models.CharField(db_column='Updated FTE', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    initial_level = models.CharField(db_column='Initial Level', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    updated_level = models.CharField(db_column='Updated Level', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    initial_country = models.CharField(db_column='Initial Country', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    updated_country = models.CharField(db_column='Updated Country', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    initial_delivery_organization = models.CharField(db_column='Initial Delivery Organization', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    p_g_owner_response = models.CharField(db_column='P&G Owner Response', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    p_g_governance_approval = models.CharField(db_column='P&G Governance Approval', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hp_owner_investigation_done = models.CharField(db_column='HP Owner Investigation Done', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hp_service_line_approval = models.CharField(db_column='HP Service Line Approval', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    updated_workgroup_id = models.CharField(db_column='Updated Workgroup ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comments = models.CharField(db_column='Comments', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    related_billing_period_report = models.CharField(db_column='Related Billing Period Report', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_conversion_rate = models.CharField(db_column='Related Conversion Rate', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_conversion_rate_fiscal_year = models.CharField(db_column='Related Conversion Rate - Fiscal Year', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_conversion_rate_country = models.CharField(db_column='Related Conversion Rate - Country', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_conversion_rate_level = models.CharField(db_column='Related Conversion Rate - Level', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_conversion_rate_local_currency = models.CharField(db_column='Related Conversion Rate - Local Currency', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_hpld_billing_period_report = models.CharField(db_column='Related HPLD Billing Period Report', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hpld_billing_period_report_billing_period = models.CharField(db_column='HPLD Billing Period Report - Billing Period', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hpld_billing_period_report_country = models.CharField(db_column='HPLD Billing Period Report - Country', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_hourly_rate = models.CharField(db_column='Related Hourly Rate', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hourly_rate_country = models.CharField(db_column='Hourly Rate - Country', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hourly_rate_level = models.CharField(db_column='Hourly Rate - Level', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hourly_rate_rate = models.CharField(db_column='Hourly Rate - Rate', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hourly_rate_currency = models.CharField(db_column='Hourly Rate - Currency', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_wbs_element = models.CharField(db_column='Related WBS Element', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hp_led_authorized_actual_workgroup_wbs_element = models.CharField(db_column='HP Led Authorized-Actual - Workgroup - WBS Element', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hp_led_authorized_actual_workgroup_wbs_element_name = models.CharField(db_column='HP Led Authorized-Actual - Workgroup - WBS Element Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hp_led_authorized_actual_workgroup_wbs_element_service_line = models.CharField(db_column='HP Led Authorized-Actual - Workgroup - WBS Element - Service Line', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    add_hp_led_authorized_request = models.CharField(db_column='Add HP Led Authorized Request', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    admin_access_control = models.CharField(db_column='Admin - Access Control', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    admin_flag_country_level_count = models.CharField(db_column='Admin - Flag - Country/Level Count', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    admin_flag_disputed = models.CharField(db_column='Admin - Flag - Disputed', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    admin_flag_fiscal_year = models.CharField(db_column='Admin - Flag - Fiscal Year', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    admin_flag_governance_edit = models.CharField(db_column='Admin - Flag - Governance Edit', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    admin_flag_hp_owner_edit = models.CharField(db_column='Admin - Flag - HP Owner Edit', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    admin_flag_hp_sl_owner_edit = models.CharField(db_column='Admin - Flag - HP SL Owner Edit', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    admin_flag_pg_owner_edit = models.CharField(db_column='Admin - Flag - PG Owner Edit', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    admin_flag_rate_id = models.CharField(db_column='Admin - Flag - Rate ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    authorized_actual_period = models.CharField(db_column='Authorized-Actual - Period', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    billing_catw_attribute = models.CharField(db_column='Billing CATW Attribute', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    billing_catw_wbs = models.CharField(db_column='Billing CATW WBS', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    billing_cost = models.CharField(db_column='Billing Cost', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    billing_country = models.CharField(db_column='Billing Country', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    billing_delivery_organization = models.CharField(db_column='Billing Delivery Organization', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    billing_dev_ops_type = models.CharField(db_column='Billing Dev/Ops Type', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    billing_fte = models.CharField(db_column='Billing FTE', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    billing_hours = models.CharField(db_column='Billing Hours', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    billing_level = models.CharField(db_column='Billing Level', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    billing_paying_cost_center = models.CharField(db_column='Billing Paying Cost Center', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    billing_rate = models.CharField(db_column='Billing Rate', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    billing_resource_name = models.CharField(db_column='Billing Resource Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    billing_workgroup = models.CharField(db_column='Billing Workgroup', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    catw_attribute = models.CharField(db_column='CATW Attribute', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    catw_wbs = models.CharField(db_column='CATW WBS', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_catw_attribute = models.CharField(db_column='Current CATW Attribute', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_catw_wbs = models.CharField(db_column='Current CATW WBS', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_cost = models.CharField(db_column='Current Cost', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_country = models.CharField(db_column='Current Country', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_delivery_organization = models.CharField(db_column='Current Delivery Organization', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_dev_ops_type = models.CharField(db_column='Current Dev/Ops Type', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_fte = models.CharField(db_column='Current FTE', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_hours = models.CharField(db_column='Current Hours', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_level = models.CharField(db_column='Current Level', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_rate = models.CharField(db_column='Current Rate', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_resource_name = models.CharField(db_column='Current Resource Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_workgroup = models.CharField(db_column='Current Workgroup', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_created = models.CharField(db_column='Date Created', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_modified = models.CharField(db_column='Date Modified', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    extract_month = models.CharField(db_column='Extract_Month', max_length=255, blank=True, null=True)  # Field name made lowercase.
    final_country = models.CharField(db_column='Final Country', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    final_hours = models.CharField(db_column='Final Hours', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    final_level = models.CharField(db_column='Final Level', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hp_accepts_dispute = models.CharField(db_column='HP Accepts Dispute', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hp_led_authorized_requests = models.CharField(db_column='Hp led authorized requests', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hp_led_authorized_actual_workgroup_related_wbs_element = models.CharField(db_column='HP Led Authorized-Actual - Workgroup - Related WBS Element', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hp_led_authorized_actual_workgroup_wbs_element_budget_manager = models.CharField(db_column='HP Led Authorized-Actual - Workgroup - WBS Element - Budget Manager', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hp_led_authorized_actual_workgroup_wbs_element_director = models.CharField(db_column='HP Led Authorized-Actual - Workgroup - WBS Element - Director', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hp_owners = models.CharField(db_column='HP Owners', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    initial_charging_entity = models.CharField(db_column='Initial Charging Entity', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    initial_cost = models.CharField(db_column='Initial Cost', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    initial_dev_ops_type = models.CharField(db_column='Initial Dev/Ops Type', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    initial_hourly_rate = models.CharField(db_column='Initial Hourly Rate', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    initial_hours = models.CharField(db_column='Initial Hours', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    initial_paying_cost_center = models.CharField(db_column='Initial Paying Cost Center', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    initial_rate = models.CharField(db_column='Initial Rate', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    invoice_period = models.CharField(db_column='Invoice Period', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    issues = models.CharField(db_column='Issues', max_length=255, blank=True, null=True)  # Field name made lowercase.
    j_2_net_arc_rrc = models.CharField(db_column='J-2 Net ARC/RRC', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_modified_by = models.CharField(db_column='Last Modified By', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mega_application_name = models.CharField(db_column='Mega Application Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    net_arc_rrc = models.CharField(db_column='Net ARC/RRC', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    p_g_employee_id = models.CharField(db_column='P&G Employee ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    p_g_owner_approval = models.CharField(db_column='P&G Owner Approval', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pre_jul_2017 = models.CharField(db_column='Pre-Jul-2017', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quarter_fy = models.CharField(db_column='Quarter-FY', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rate_info_for_user = models.CharField(db_column='Rate Info for User', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    record_owner = models.CharField(db_column='Record Owner', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_conversion_rate_firm_fx_rate = models.CharField(db_column='Related Conversion Rate - Firm FX Rate', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_conversion_rate_hourly_local_currency = models.CharField(db_column='Related Conversion Rate - Hourly Local Currency', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_conversion_rate_hourly_rate = models.CharField(db_column='Related Conversion Rate - Hourly Rate', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_conversion_rate_j_2_country_fte = models.CharField(db_column='Related Conversion Rate - J-2 Country FTE', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_conversion_rate_monthly_local_currency_rate = models.CharField(db_column='Related Conversion Rate - Monthly Local Currency Rate', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_conversion_rate_rate = models.CharField(db_column='Related Conversion Rate - Rate', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_hp_approved_request = models.CharField(db_column='Related HP Approved Request', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_hp_authorized_actual2 = models.CharField(db_column='Related HP Authorized-Actual2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_hp_led_authorized_request = models.CharField(db_column='Related HP Led Authorized Request', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_hp_led_authorized_request2 = models.CharField(db_column='Related HP Led Authorized Request2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_hp_led_authorized_request2_hp_request_id = models.CharField(db_column='Related HP Led Authorized Request2 - HP Request ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_hp_led_authorized_request2_period = models.CharField(db_column='Related HP Led Authorized Request2 - Period', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_hp_led_authorized_request2_record_id_field = models.CharField(db_column='Related HP Led Authorized Request2 - Record ID#', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    related_hp_led_authorized_request2_related_hp_led_authorized_actual = models.CharField(db_column='Related HP Led Authorized Request2 - Related HP Led Authorized-Actual', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_hp_led_authorized_actual = models.CharField(db_column='Related HP Led Authorized-Actual', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    related_rate = models.CharField(db_column='Related Rate', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    selected_billing_period = models.CharField(db_column='Selected Billing Period', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status_test = models.CharField(db_column='Status Test', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trackback_keys = models.CharField(db_column='Trackback Keys', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    updated_catw_attribute = models.CharField(db_column='Updated CATW Attribute', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    updated_catw_wbs = models.CharField(db_column='Updated CATW WBS', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    updated_charging_entity_cost_center = models.CharField(db_column='Updated Charging Entity Cost Center', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    updated_cost = models.CharField(db_column='Updated Cost', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    updated_cost_center_ad = models.CharField(db_column='Updated Cost Center - AD', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    updated_cost_center_director = models.CharField(db_column='Updated Cost Center - Director', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    updated_cost_center_slfm = models.CharField(db_column='Updated Cost Center - SLFM', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    updated_cost_center_sub_service_line = models.CharField(db_column='Updated Cost Center - Sub Service Line', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    updated_delivery_organization = models.CharField(db_column='Updated Delivery Organization', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    updated_hourly_rate = models.CharField(db_column='Updated Hourly Rate', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    updated_hours = models.CharField(db_column='Updated Hours', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    updated_paying_cost_center = models.CharField(db_column='Updated Paying Cost Center', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    updated_rate = models.CharField(db_column='Updated Rate', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    updated_workgroup_dev_ops = models.CharField(db_column='Updated Workgroup Dev/Ops', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    workgroup_hp_owners = models.CharField(db_column='Workgroup HP Owners', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    workgroup_p_g_owners = models.CharField(db_column='Workgroup P&G Owners', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'STG_HP_LED_ACTUALS'


class StgMasterPrjPortfolio(models.Model):
    id = models.BigIntegerField(primary_key=True)
    hp_project_field = models.CharField(db_column='HP Project #', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    project_name = models.CharField(db_column='Project Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hp_project_manager = models.CharField(db_column='HP Project Manager', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hp_project_manager_email = models.CharField(db_column='HP Project Manager Email', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    project_classification = models.CharField(db_column='Project Classification', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    project_stage = models.CharField(db_column='Project Stage', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    project_actual_start_date = models.CharField(db_column='Project Actual Start Date', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    project_actual_end_date = models.CharField(db_column='Project Actual End Date', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sfdc_estimated_project_end_date = models.CharField(db_column='SFDC_Estimated Project End Date', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    compass_fmo_wbs = models.CharField(db_column='COMPASS FMO WBS', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    compass_wbs_id = models.CharField(db_column='COMPASS/WBS ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hp_lead_service_category = models.CharField(db_column='HP Lead Service Category', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'STG_MASTER_PRJ_PORTFOLIO'


class StgRawLaborBooking(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fiscal_year_period = models.CharField(db_column='Fiscal year/period', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    labor_source_1 = models.CharField(db_column='Labor Source 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    labor_source_2 = models.CharField(db_column='Labor Source 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    posting_date = models.CharField(db_column='Posting Date', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_name = models.CharField(db_column='Employee Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee = models.CharField(db_column='Employee', max_length=255, blank=True, null=True)  # Field name made lowercase.
    e_mail_address_1 = models.CharField(db_column='E-Mail Address 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    activity_type = models.CharField(db_column='Activity Type', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    legacy_location_code = models.CharField(db_column='Legacy Location Code', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    master_cost_center = models.CharField(db_column='Master Cost Center', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_region = models.CharField(db_column='Employee Region', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_country = models.CharField(db_column='Employee Country', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wbs_resp_cost_center = models.CharField(db_column='WBS Resp Cost Center', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    region = models.CharField(db_column='Region', max_length=255, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wbs_1 = models.CharField(db_column='WBS 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wbs_2 = models.CharField(db_column='WBS 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    attribute_1 = models.CharField(db_column='Attribute 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    short_text = models.CharField(db_column='Short text', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    activity_date = models.CharField(db_column='Activity Date', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    supervisor_1 = models.CharField(db_column='Supervisor 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    supervisor_2 = models.CharField(db_column='Supervisor 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    e_mail_address_2 = models.CharField(db_column='E-Mail Address 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prj_customer = models.CharField(db_column='PRJ Customer', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cost_element = models.CharField(db_column='Cost Element', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    currency_code_local = models.CharField(db_column='Currency Code Local', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    activity_hours_1 = models.CharField(db_column='Activity Hours 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_cost_1 = models.CharField(db_column='Total Cost 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    activity_hours_2 = models.CharField(db_column='Activity Hours 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_cost_2 = models.CharField(db_column='Total Cost 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'STG_RAW_LABOR_BOOKING'


class TmpNttrPgband(models.Model):
    id = models.BigIntegerField(primary_key=True)
    activity_type = models.CharField(db_column='Activity Type', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pg_band = models.CharField(db_column='PG Band', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hp_management_level = models.CharField(db_column='HP Management Level', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TMP_NTTR_PGBAND'


class TmpNttrAacodes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    aa_code = models.CharField(db_column='AA Code', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    catw_category = models.CharField(db_column='CATW Category', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fte_calculation_type = models.CharField(db_column='FTE Calculation Type', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wbs_required_field = models.CharField(db_column='WBS Required?', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)  # Field name made lowercase.
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TMP_NTTR_AACODES'


class TmpNttrCountrymapping(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pg_country = models.CharField(db_column='PG Country', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    source_country = models.CharField(db_column='Source Country', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TMP_NTTR_COUNTRYMAPPING'


class TmpNttrBwrawAm(models.Model):
    id = models.BigIntegerField(primary_key=True)
    activity_month = models.TextField(db_column='Activity Month', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    e_mail_address = models.TextField(db_column='E-Mail Address', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee = models.TextField(db_column='Employee', blank=True, null=True)  # Field name made lowercase.
    employee_1 = models.TextField(db_column='Employee_1', blank=True, null=True)  # Field name made lowercase.
    e_mail_address_1 = models.TextField(db_column='E-Mail Address_1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_level = models.TextField(db_column='Employee Level', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    daily_work_hours = models.TextField(db_column='Daily work hours', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_type = models.TextField(db_column='Employee Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country_grouping = models.TextField(db_column='Country Grouping', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    geography = models.TextField(db_column='Geography', blank=True, null=True)  # Field name made lowercase.
    activity_type = models.TextField(db_column='Activity Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_country = models.TextField(db_column='Employee Country', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_country_1 = models.TextField(db_column='Employee Country_1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wbs = models.TextField(db_column='WBS', blank=True, null=True)  # Field name made lowercase.
    wbs_1 = models.TextField(db_column='WBS_1', blank=True, null=True)  # Field name made lowercase.
    aa_type = models.TextField(db_column='AA Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    attribute_1 = models.TextField(db_column='Attribute 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    attribute_2 = models.TextField(db_column='Attribute 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    short_text = models.TextField(db_column='Short Text', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    actual_labor_rate = models.TextField(db_column='Actual Labor Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    usd_labor_currency = models.TextField(db_column='USD / Labor Currency', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    activity_hours = models.TextField(db_column='Activity Hours', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    file_name = models.TextField()
    file_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'TMP_NTTR_BWRAW_AM'


class TmpNttrBwrawApj(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    activity_month = models.TextField(db_column='Activity Month', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    e_mail_address = models.TextField(db_column='E-Mail Address', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee = models.TextField(db_column='Employee', blank=True, null=True)  # Field name made lowercase.
    employee_1 = models.TextField(db_column='Employee_1', blank=True, null=True)  # Field name made lowercase.
    e_mail_address_1 = models.TextField(db_column='E-Mail Address_1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_level = models.TextField(db_column='Employee Level', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    daily_work_hours = models.TextField(db_column='Daily work hours', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_type = models.TextField(db_column='Employee Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country_grouping = models.TextField(db_column='Country Grouping', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    geography = models.TextField(db_column='Geography', blank=True, null=True)  # Field name made lowercase.
    activity_type = models.TextField(db_column='Activity Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_country = models.TextField(db_column='Employee Country', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_country_1 = models.TextField(db_column='Employee Country_1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wbs = models.TextField(db_column='WBS', blank=True, null=True)  # Field name made lowercase.
    wbs_1 = models.TextField(db_column='WBS_1', blank=True, null=True)  # Field name made lowercase.
    aa_type = models.TextField(db_column='AA Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    attribute_1 = models.TextField(db_column='Attribute 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    attribute_2 = models.TextField(db_column='Attribute 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    short_text = models.TextField(db_column='Short Text', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    actual_labor_rate = models.TextField(db_column='Actual Labor Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    usd_labor_currency = models.TextField(db_column='USD / Labor Currency', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    activity_hours = models.TextField(db_column='Activity Hours', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    file_name = models.TextField()
    file_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'TMP_NTTR_BWRAW_APJ'


class TmpNttrBwrawEmea(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    activity_month = models.TextField(db_column='Activity Month', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    e_mail_address = models.TextField(db_column='E-Mail Address', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee = models.TextField(db_column='Employee', blank=True, null=True)  # Field name made lowercase.
    employee_1 = models.TextField(db_column='Employee_1', blank=True, null=True)  # Field name made lowercase.
    e_mail_address_1 = models.TextField(db_column='E-Mail Address_1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_level = models.TextField(db_column='Employee Level', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    daily_work_hours = models.TextField(db_column='Daily work hours', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_type = models.TextField(db_column='Employee Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country_grouping = models.TextField(db_column='Country Grouping', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    geography = models.TextField(db_column='Geography', blank=True, null=True)  # Field name made lowercase.
    activity_type = models.TextField(db_column='Activity Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_country = models.TextField(db_column='Employee Country', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_country_1 = models.TextField(db_column='Employee Country_1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wbs = models.TextField(db_column='WBS', blank=True, null=True)  # Field name made lowercase.
    wbs_1 = models.TextField(db_column='WBS_1', blank=True, null=True)  # Field name made lowercase.
    aa_type = models.TextField(db_column='AA Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    attribute_1 = models.TextField(db_column='Attribute 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    attribute_2 = models.TextField(db_column='Attribute 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    short_text = models.TextField(db_column='Short Text', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    actual_labor_rate = models.TextField(db_column='Actual Labor Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    usd_labor_currency = models.TextField(db_column='USD / Labor Currency', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    activity_hours = models.TextField(db_column='Activity Hours', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    file_name = models.TextField()
    file_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'TMP_NTTR_BWRAW_EMEA'


class TmpNttrFlexpool(models.Model):

    class Meta:
        managed = False
        db_table = 'TMP_NTTR_FLEXPOOL'


class TmpNttrStaffaug(models.Model):

    class Meta:
        managed = False
        db_table = 'TMP_NTTR_STAFFAUG'


class TmpNttrPgstructures(models.Model):
    id = models.BigIntegerField(primary_key=True)
    level = models.CharField(db_column='Level', max_length=255, blank=True, null=True)  # Field name made lowercase.
    project_def = models.CharField(db_column='Project Def', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    project_profile = models.CharField(db_column='Project Profile', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wbs_element = models.CharField(db_column='WBS element', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TMP_NTTR_PGSTRUCTURES'

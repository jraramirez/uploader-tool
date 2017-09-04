# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class TmpTransitionBw(models.Model):
    service_month = models.CharField(max_length=255, blank=True, null=True)
    manager_email = models.CharField(max_length=255, blank=True, null=True)
    employee_id = models.CharField(max_length=255, blank=True, null=True)
    employee_name = models.CharField(max_length=255, blank=True, null=True)
    employee_email = models.CharField(max_length=255, blank=True, null=True)
    pg_level = models.CharField(max_length=255, blank=True, null=True)
    daily_expected_hours = models.CharField(max_length=255, blank=True, null=True)
    employee_type = models.CharField(max_length=255, blank=True, null=True)
    bill_to_county = models.CharField(max_length=255, blank=True, null=True)
    geography = models.CharField(max_length=255, blank=True, null=True)
    hp_level = models.CharField(max_length=255, blank=True, null=True)
    seat_country_code = models.CharField(max_length=255, blank=True, null=True)
    seat_country = models.CharField(max_length=255, blank=True, null=True)
    wbs = models.CharField(max_length=255, blank=True, null=True)
    wbs_description = models.CharField(max_length=255, blank=True, null=True)
    aa_type = models.CharField(max_length=255, blank=True, null=True)
    attribute = models.CharField(max_length=255, blank=True, null=True)
    attribute_2 = models.CharField(max_length=255, blank=True, null=True)
    short_text = models.CharField(max_length=255, blank=True, null=True)
    hp_labor_rate = models.DecimalField(max_digits=38, decimal_places=15, blank=True, null=True)
    usd_labor_currency = models.DecimalField(max_digits=38, decimal_places=15, blank=True, null=True)
    hours = models.DecimalField(max_digits=38, decimal_places=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TMP_TRANSITION_BW'


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
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class TmpNcs(models.Model):
    audit_type = models.CharField(max_length=255, blank=True, null=True)
    business_unit = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    project_name = models.CharField(max_length=255, blank=True, null=True)
    project_manager = models.CharField(max_length=255, blank=True, null=True)
    auditor = models.CharField(max_length=255, blank=True, null=True)
    process_set = models.CharField(max_length=255, blank=True, null=True)
    question_set = models.CharField(max_length=255, blank=True, null=True)
    question_set_version_no = models.CharField(max_length=255, blank=True, null=True)
    planned_audit_date = models.DateTimeField(blank=True, null=True)
    actual_audit_date = models.DateTimeField(blank=True, null=True)
    criteria_code = models.CharField(max_length=255, blank=True, null=True)
    criteria_description = models.CharField(max_length=255, blank=True, null=True)
    finding_description = models.TextField(blank=True, null=True)
    high_level_root_cause = models.CharField(max_length=255, blank=True, null=True)
    low_level_root_cause = models.CharField(max_length=255, blank=True, null=True)
    corrective_action = models.TextField(blank=True, null=True)
    target_resolution_date = models.DateTimeField(blank=True, null=True)
    client = models.CharField(max_length=255, blank=True, null=True)
    auditee = models.CharField(max_length=255, blank=True, null=True)
    finding_status = models.CharField(max_length=255, blank=True, null=True)
    verification_details = models.CharField(max_length=255, blank=True, null=True)
    audit_sample_unit_no = models.CharField(max_length=255, blank=True, null=True)
    ncdescription_comment = models.TextField(blank=True, null=True)
    criteria_tasks = models.CharField(max_length=255, blank=True, null=True)
    finding_close_date = models.DateTimeField(blank=True, null=True)
    business_impact_category = models.CharField(max_length=255, blank=True, null=True)
    business_impact_description = models.CharField(max_length=255, blank=True, null=True)
    process_model = models.CharField(max_length=255, blank=True, null=True)
    finding_type = models.CharField(max_length=255, blank=True, null=True)
    tr_month = models.FloatField(blank=True, null=True)
    tr_year = models.FloatField(blank=True, null=True)
    resolved_on_time = models.CharField(max_length=255, blank=True, null=True)
    nc_age = models.FloatField(blank=True, null=True)
    col1 = models.CharField(max_length=255, blank=True, null=True)
    col2 = models.CharField(max_length=255, blank=True, null=True)
    col3 = models.CharField(max_length=255, blank=True, null=True)
    col4 = models.CharField(max_length=255, blank=True, null=True)
    col5 = models.CharField(max_length=255, blank=True, null=True)
    col6 = models.CharField(max_length=255, blank=True, null=True)
    col7 = models.CharField(max_length=255, blank=True, null=True)
    col8 = models.CharField(max_length=255, blank=True, null=True)
    col9 = models.CharField(max_length=255, blank=True, null=True)
    col10 = models.CharField(max_length=255, blank=True, null=True)
    col11 = models.CharField(max_length=255, blank=True, null=True)
    col12 = models.CharField(max_length=255, blank=True, null=True)
    col13 = models.CharField(max_length=255, blank=True, null=True)
    project_type = models.CharField(max_length=255, blank=True, null=True)
    delivery_method = models.CharField(max_length=255, blank=True, null=True)
    region1 = models.CharField(max_length=255, blank=True, null=True)
    service_line = models.CharField(max_length=255, blank=True, null=True)
    actual_month = models.FloatField(blank=True, null=True)
    actual_year = models.FloatField(blank=True, null=True)
    inclusion = models.CharField(max_length=255, blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_date = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TMP_NCS'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class TestLang(models.Model):

    class Meta:
        managed = False
        db_table = 'test_lang'

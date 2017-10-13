# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-14 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StgHpLedActuals',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('record_id_field', models.CharField(blank=True, db_column='Record ID#', max_length=255, null=True)),
                ('period', models.CharField(blank=True, db_column='Period', max_length=255, null=True)),
                ('service_date', models.CharField(blank=True, db_column='Service Date', max_length=255, null=True)),
                ('initial_workgroup', models.CharField(blank=True, db_column='Initial Workgroup', max_length=255, null=True)),
                ('updated_workgroup_name', models.CharField(blank=True, db_column='Updated Workgroup Name', max_length=255, null=True)),
                ('initial_resource_name', models.CharField(blank=True, db_column='Initial Resource Name', max_length=255, null=True)),
                ('fte', models.CharField(blank=True, db_column='FTE', max_length=255, null=True)),
                ('updated_fte', models.CharField(blank=True, db_column='Updated FTE', max_length=255, null=True)),
                ('initial_level', models.CharField(blank=True, db_column='Initial Level', max_length=255, null=True)),
                ('updated_level', models.CharField(blank=True, db_column='Updated Level', max_length=255, null=True)),
                ('initial_country', models.CharField(blank=True, db_column='Initial Country', max_length=255, null=True)),
                ('updated_country', models.CharField(blank=True, db_column='Updated Country', max_length=255, null=True)),
                ('initial_delivery_organization', models.CharField(blank=True, db_column='Initial Delivery Organization', max_length=255, null=True)),
                ('p_g_owner_response', models.CharField(blank=True, db_column='P&G Owner Response', max_length=255, null=True)),
                ('p_g_governance_approval', models.CharField(blank=True, db_column='P&G Governance Approval', max_length=255, null=True)),
                ('hp_owner_investigation_done', models.CharField(blank=True, db_column='HP Owner Investigation Done', max_length=255, null=True)),
                ('hp_service_line_approval', models.CharField(blank=True, db_column='HP Service Line Approval', max_length=255, null=True)),
                ('updated_workgroup_id', models.CharField(blank=True, db_column='Updated Workgroup ID', max_length=255, null=True)),
                ('comments', models.CharField(blank=True, db_column='Comments', max_length=2000, null=True)),
                ('related_billing_period_report', models.CharField(blank=True, db_column='Related Billing Period Report', max_length=255, null=True)),
                ('related_conversion_rate', models.CharField(blank=True, db_column='Related Conversion Rate', max_length=255, null=True)),
                ('related_conversion_rate_fiscal_year', models.CharField(blank=True, db_column='Related Conversion Rate - Fiscal Year', max_length=255, null=True)),
                ('related_conversion_rate_country', models.CharField(blank=True, db_column='Related Conversion Rate - Country', max_length=255, null=True)),
                ('related_conversion_rate_level', models.CharField(blank=True, db_column='Related Conversion Rate - Level', max_length=255, null=True)),
                ('related_conversion_rate_local_currency', models.CharField(blank=True, db_column='Related Conversion Rate - Local Currency', max_length=255, null=True)),
                ('related_hpld_billing_period_report', models.CharField(blank=True, db_column='Related HPLD Billing Period Report', max_length=255, null=True)),
                ('hpld_billing_period_report_billing_period', models.CharField(blank=True, db_column='HPLD Billing Period Report - Billing Period', max_length=255, null=True)),
                ('hpld_billing_period_report_country', models.CharField(blank=True, db_column='HPLD Billing Period Report - Country', max_length=255, null=True)),
                ('related_hourly_rate', models.CharField(blank=True, db_column='Related Hourly Rate', max_length=255, null=True)),
                ('hourly_rate_country', models.CharField(blank=True, db_column='Hourly Rate - Country', max_length=255, null=True)),
                ('hourly_rate_level', models.CharField(blank=True, db_column='Hourly Rate - Level', max_length=255, null=True)),
                ('hourly_rate_rate', models.CharField(blank=True, db_column='Hourly Rate - Rate', max_length=255, null=True)),
                ('hourly_rate_currency', models.CharField(blank=True, db_column='Hourly Rate - Currency', max_length=255, null=True)),
                ('related_wbs_element', models.CharField(blank=True, db_column='Related WBS Element', max_length=255, null=True)),
                ('hp_led_authorized_actual_workgroup_wbs_element', models.CharField(blank=True, db_column='HP Led Authorized-Actual - Workgroup - WBS Element', max_length=255, null=True)),
                ('hp_led_authorized_actual_workgroup_wbs_element_name', models.CharField(blank=True, db_column='HP Led Authorized-Actual - Workgroup - WBS Element Name', max_length=255, null=True)),
                ('hp_led_authorized_actual_workgroup_wbs_element_service_line', models.CharField(blank=True, db_column='HP Led Authorized-Actual - Workgroup - WBS Element - Service Line', max_length=255, null=True)),
                ('add_hp_led_authorized_request', models.CharField(blank=True, db_column='Add HP Led Authorized Request', max_length=255, null=True)),
                ('admin_access_control', models.CharField(blank=True, db_column='Admin - Access Control', max_length=255, null=True)),
                ('admin_flag_country_level_count', models.CharField(blank=True, db_column='Admin - Flag - Country/Level Count', max_length=255, null=True)),
                ('admin_flag_disputed', models.CharField(blank=True, db_column='Admin - Flag - Disputed', max_length=255, null=True)),
                ('admin_flag_fiscal_year', models.CharField(blank=True, db_column='Admin - Flag - Fiscal Year', max_length=255, null=True)),
                ('admin_flag_governance_edit', models.CharField(blank=True, db_column='Admin - Flag - Governance Edit', max_length=255, null=True)),
                ('admin_flag_hp_owner_edit', models.CharField(blank=True, db_column='Admin - Flag - HP Owner Edit', max_length=255, null=True)),
                ('admin_flag_hp_sl_owner_edit', models.CharField(blank=True, db_column='Admin - Flag - HP SL Owner Edit', max_length=255, null=True)),
                ('admin_flag_pg_owner_edit', models.CharField(blank=True, db_column='Admin - Flag - PG Owner Edit', max_length=255, null=True)),
                ('admin_flag_rate_id', models.CharField(blank=True, db_column='Admin - Flag - Rate ID', max_length=255, null=True)),
                ('authorized_actual_period', models.CharField(blank=True, db_column='Authorized-Actual - Period', max_length=255, null=True)),
                ('billing_catw_attribute', models.CharField(blank=True, db_column='Billing CATW Attribute', max_length=255, null=True)),
                ('billing_catw_wbs', models.CharField(blank=True, db_column='Billing CATW WBS', max_length=255, null=True)),
                ('billing_cost', models.CharField(blank=True, db_column='Billing Cost', max_length=255, null=True)),
                ('billing_country', models.CharField(blank=True, db_column='Billing Country', max_length=255, null=True)),
                ('billing_delivery_organization', models.CharField(blank=True, db_column='Billing Delivery Organization', max_length=255, null=True)),
                ('billing_dev_ops_type', models.CharField(blank=True, db_column='Billing Dev/Ops Type', max_length=255, null=True)),
                ('billing_fte', models.CharField(blank=True, db_column='Billing FTE', max_length=255, null=True)),
                ('billing_hours', models.CharField(blank=True, db_column='Billing Hours', max_length=255, null=True)),
                ('billing_level', models.CharField(blank=True, db_column='Billing Level', max_length=255, null=True)),
                ('billing_paying_cost_center', models.CharField(blank=True, db_column='Billing Paying Cost Center', max_length=255, null=True)),
                ('billing_rate', models.CharField(blank=True, db_column='Billing Rate', max_length=255, null=True)),
                ('billing_resource_name', models.CharField(blank=True, db_column='Billing Resource Name', max_length=255, null=True)),
                ('billing_workgroup', models.CharField(blank=True, db_column='Billing Workgroup', max_length=255, null=True)),
                ('catw_attribute', models.CharField(blank=True, db_column='CATW Attribute', max_length=255, null=True)),
                ('catw_wbs', models.CharField(blank=True, db_column='CATW WBS', max_length=255, null=True)),
                ('current_catw_attribute', models.CharField(blank=True, db_column='Current CATW Attribute', max_length=255, null=True)),
                ('current_catw_wbs', models.CharField(blank=True, db_column='Current CATW WBS', max_length=255, null=True)),
                ('current_cost', models.CharField(blank=True, db_column='Current Cost', max_length=255, null=True)),
                ('current_country', models.CharField(blank=True, db_column='Current Country', max_length=255, null=True)),
                ('current_delivery_organization', models.CharField(blank=True, db_column='Current Delivery Organization', max_length=255, null=True)),
                ('current_dev_ops_type', models.CharField(blank=True, db_column='Current Dev/Ops Type', max_length=255, null=True)),
                ('current_fte', models.CharField(blank=True, db_column='Current FTE', max_length=255, null=True)),
                ('current_hours', models.CharField(blank=True, db_column='Current Hours', max_length=255, null=True)),
                ('current_level', models.CharField(blank=True, db_column='Current Level', max_length=255, null=True)),
                ('current_rate', models.CharField(blank=True, db_column='Current Rate', max_length=255, null=True)),
                ('current_resource_name', models.CharField(blank=True, db_column='Current Resource Name', max_length=255, null=True)),
                ('current_workgroup', models.CharField(blank=True, db_column='Current Workgroup', max_length=255, null=True)),
                ('date_created', models.CharField(blank=True, db_column='Date Created', max_length=255, null=True)),
                ('date_modified', models.CharField(blank=True, db_column='Date Modified', max_length=255, null=True)),
                ('extract_month', models.CharField(blank=True, db_column='Extract_Month', max_length=255, null=True)),
                ('final_country', models.CharField(blank=True, db_column='Final Country', max_length=255, null=True)),
                ('final_hours', models.CharField(blank=True, db_column='Final Hours', max_length=255, null=True)),
                ('final_level', models.CharField(blank=True, db_column='Final Level', max_length=255, null=True)),
                ('hp_accepts_dispute', models.CharField(blank=True, db_column='HP Accepts Dispute', max_length=255, null=True)),
                ('hp_led_authorized_requests', models.CharField(blank=True, db_column='Hp led authorized requests', max_length=255, null=True)),
                ('hp_led_authorized_actual_workgroup_related_wbs_element', models.CharField(blank=True, db_column='HP Led Authorized-Actual - Workgroup - Related WBS Element', max_length=255, null=True)),
                ('hp_led_authorized_actual_workgroup_wbs_element_budget_manager', models.CharField(blank=True, db_column='HP Led Authorized-Actual - Workgroup - WBS Element - Budget Manager', max_length=255, null=True)),
                ('hp_led_authorized_actual_workgroup_wbs_element_director', models.CharField(blank=True, db_column='HP Led Authorized-Actual - Workgroup - WBS Element - Director', max_length=255, null=True)),
                ('hp_owners', models.CharField(blank=True, db_column='HP Owners', max_length=255, null=True)),
                ('initial_charging_entity', models.CharField(blank=True, db_column='Initial Charging Entity', max_length=255, null=True)),
                ('initial_cost', models.CharField(blank=True, db_column='Initial Cost', max_length=255, null=True)),
                ('initial_dev_ops_type', models.CharField(blank=True, db_column='Initial Dev/Ops Type', max_length=255, null=True)),
                ('initial_hourly_rate', models.CharField(blank=True, db_column='Initial Hourly Rate', max_length=255, null=True)),
                ('initial_hours', models.CharField(blank=True, db_column='Initial Hours', max_length=255, null=True)),
                ('initial_paying_cost_center', models.CharField(blank=True, db_column='Initial Paying Cost Center', max_length=255, null=True)),
                ('initial_rate', models.CharField(blank=True, db_column='Initial Rate', max_length=255, null=True)),
                ('invoice_period', models.CharField(blank=True, db_column='Invoice Period', max_length=255, null=True)),
                ('issues', models.CharField(blank=True, db_column='Issues', max_length=255, null=True)),
                ('j_2_net_arc_rrc', models.CharField(blank=True, db_column='J-2 Net ARC/RRC', max_length=255, null=True)),
                ('last_modified_by', models.CharField(blank=True, db_column='Last Modified By', max_length=255, null=True)),
                ('mega_application_name', models.CharField(blank=True, db_column='Mega Application Name', max_length=255, null=True)),
                ('net_arc_rrc', models.CharField(blank=True, db_column='Net ARC/RRC', max_length=255, null=True)),
                ('p_g_employee_id', models.CharField(blank=True, db_column='P&G Employee ID', max_length=255, null=True)),
                ('p_g_owner_approval', models.CharField(blank=True, db_column='P&G Owner Approval', max_length=255, null=True)),
                ('pre_jul_2017', models.CharField(blank=True, db_column='Pre-Jul-2017', max_length=255, null=True)),
                ('quarter_fy', models.CharField(blank=True, db_column='Quarter-FY', max_length=255, null=True)),
                ('rate_info_for_user', models.CharField(blank=True, db_column='Rate Info for User', max_length=255, null=True)),
                ('record_owner', models.CharField(blank=True, db_column='Record Owner', max_length=255, null=True)),
                ('related_conversion_rate_firm_fx_rate', models.CharField(blank=True, db_column='Related Conversion Rate - Firm FX Rate', max_length=255, null=True)),
                ('related_conversion_rate_hourly_local_currency', models.CharField(blank=True, db_column='Related Conversion Rate - Hourly Local Currency', max_length=255, null=True)),
                ('related_conversion_rate_hourly_rate', models.CharField(blank=True, db_column='Related Conversion Rate - Hourly Rate', max_length=255, null=True)),
                ('related_conversion_rate_j_2_country_fte', models.CharField(blank=True, db_column='Related Conversion Rate - J-2 Country FTE', max_length=255, null=True)),
                ('related_conversion_rate_monthly_local_currency_rate', models.CharField(blank=True, db_column='Related Conversion Rate - Monthly Local Currency Rate', max_length=255, null=True)),
                ('related_conversion_rate_rate', models.CharField(blank=True, db_column='Related Conversion Rate - Rate', max_length=255, null=True)),
                ('related_hp_approved_request', models.CharField(blank=True, db_column='Related HP Approved Request', max_length=255, null=True)),
                ('related_hp_authorized_actual2', models.CharField(blank=True, db_column='Related HP Authorized-Actual2', max_length=255, null=True)),
                ('related_hp_led_authorized_request', models.CharField(blank=True, db_column='Related HP Led Authorized Request', max_length=255, null=True)),
                ('related_hp_led_authorized_request2', models.CharField(blank=True, db_column='Related HP Led Authorized Request2', max_length=255, null=True)),
                ('related_hp_led_authorized_request2_hp_request_id', models.CharField(blank=True, db_column='Related HP Led Authorized Request2 - HP Request ID', max_length=255, null=True)),
                ('related_hp_led_authorized_request2_period', models.CharField(blank=True, db_column='Related HP Led Authorized Request2 - Period', max_length=255, null=True)),
                ('related_hp_led_authorized_request2_record_id_field', models.CharField(blank=True, db_column='Related HP Led Authorized Request2 - Record ID#', max_length=255, null=True)),
                ('related_hp_led_authorized_request2_related_hp_led_authorized_actual', models.CharField(blank=True, db_column='Related HP Led Authorized Request2 - Related HP Led Authorized-Actual', max_length=255, null=True)),
                ('related_hp_led_authorized_actual', models.CharField(blank=True, db_column='Related HP Led Authorized-Actual', max_length=255, null=True)),
                ('related_rate', models.CharField(blank=True, db_column='Related Rate', max_length=255, null=True)),
                ('selected_billing_period', models.CharField(blank=True, db_column='Selected Billing Period', max_length=255, null=True)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=255, null=True)),
                ('status_test', models.CharField(blank=True, db_column='Status Test', max_length=255, null=True)),
                ('trackback_keys', models.CharField(blank=True, db_column='Trackback Keys', max_length=255, null=True)),
                ('updated_catw_attribute', models.CharField(blank=True, db_column='Updated CATW Attribute', max_length=255, null=True)),
                ('updated_catw_wbs', models.CharField(blank=True, db_column='Updated CATW WBS', max_length=255, null=True)),
                ('updated_charging_entity_cost_center', models.CharField(blank=True, db_column='Updated Charging Entity Cost Center', max_length=255, null=True)),
                ('updated_cost', models.CharField(blank=True, db_column='Updated Cost', max_length=255, null=True)),
                ('updated_cost_center_ad', models.CharField(blank=True, db_column='Updated Cost Center - AD', max_length=255, null=True)),
                ('updated_cost_center_director', models.CharField(blank=True, db_column='Updated Cost Center - Director', max_length=255, null=True)),
                ('updated_cost_center_slfm', models.CharField(blank=True, db_column='Updated Cost Center - SLFM', max_length=255, null=True)),
                ('updated_cost_center_sub_service_line', models.CharField(blank=True, db_column='Updated Cost Center - Sub Service Line', max_length=255, null=True)),
                ('updated_delivery_organization', models.CharField(blank=True, db_column='Updated Delivery Organization', max_length=255, null=True)),
                ('updated_hourly_rate', models.CharField(blank=True, db_column='Updated Hourly Rate', max_length=255, null=True)),
                ('updated_hours', models.CharField(blank=True, db_column='Updated Hours', max_length=255, null=True)),
                ('updated_paying_cost_center', models.CharField(blank=True, db_column='Updated Paying Cost Center', max_length=255, null=True)),
                ('updated_rate', models.CharField(blank=True, db_column='Updated Rate', max_length=255, null=True)),
                ('updated_workgroup_dev_ops', models.CharField(blank=True, db_column='Updated Workgroup Dev/Ops', max_length=255, null=True)),
                ('workgroup_hp_owners', models.CharField(blank=True, db_column='Workgroup HP Owners', max_length=255, null=True)),
                ('workgroup_p_g_owners', models.CharField(blank=True, db_column='Workgroup P&G Owners', max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'STG_HP_LED_ACTUALS',
            },
        ),
        migrations.CreateModel(
            name='StgItoPdoEmpList',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('month', models.CharField(blank=True, db_column='Month', max_length=255, null=True)),
                ('employee_id', models.CharField(blank=True, db_column='Employee ID', max_length=255, null=True)),
                ('region', models.CharField(blank=True, db_column='Region', max_length=255, null=True)),
                ('pm_name', models.CharField(blank=True, db_column='PM Name', max_length=255, null=True)),
                ('file_name', models.CharField(blank=True, max_length=255, null=True)),
                ('file_date', models.CharField(blank=True, max_length=255, null=True)),
                ('test', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'STG_ITO_PDO_EMP_LIST',
            },
        ),
        migrations.CreateModel(
            name='StgMasterPrjPortfolio',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('hp_project_field', models.CharField(blank=True, db_column='HP Project #', max_length=255, null=True)),
                ('project_name', models.CharField(blank=True, db_column='Project Name', max_length=255, null=True)),
                ('hp_project_manager', models.CharField(blank=True, db_column='HP Project Manager', max_length=255, null=True)),
                ('hp_project_manager_email', models.CharField(blank=True, db_column='HP Project Manager Email', max_length=255, null=True)),
                ('project_classification', models.CharField(blank=True, db_column='Project Classification', max_length=255, null=True)),
                ('project_stage', models.CharField(blank=True, db_column='Project Stage', max_length=255, null=True)),
                ('project_actual_start_date', models.CharField(blank=True, db_column='Project Actual Start Date', max_length=255, null=True)),
                ('project_actual_end_date', models.CharField(blank=True, db_column='Project Actual End Date', max_length=255, null=True)),
                ('sfdc_estimated_project_end_date', models.CharField(blank=True, db_column='SFDC_Estimated Project End Date', max_length=255, null=True)),
                ('compass_fmo_wbs', models.CharField(blank=True, db_column='COMPASS FMO WBS', max_length=255, null=True)),
                ('compass_wbs_id', models.CharField(blank=True, db_column='COMPASS/WBS ID', max_length=255, null=True)),
                ('hp_lead_service_category', models.CharField(blank=True, db_column='HP Lead Service Category', max_length=255, null=True)),
                ('file_name', models.CharField(blank=True, max_length=255, null=True)),
                ('file_date', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'STG_MASTER_PRJ_PORTFOLIO',
            },
        ),
        migrations.CreateModel(
            name='StgPgStructures',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('wbs_element', models.CharField(blank=True, db_column='WBS element', max_length=200, null=True)),
                ('user_code_2', models.CharField(blank=True, db_column='User code 2', max_length=100, null=True)),
                ('file_name', models.CharField(blank=True, max_length=255, null=True)),
                ('file_date', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'STG_PG_STRUCTURES',
            },
        ),
        migrations.CreateModel(
            name='StgRawLaborBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'STG_RAW_LABOR_BOOKING',
            },
        ),
        migrations.CreateModel(
            name='TmpTransitionBw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_month', models.CharField(blank=True, max_length=255, null=True)),
                ('manager_email', models.CharField(blank=True, max_length=255, null=True)),
                ('employee_id', models.CharField(blank=True, max_length=255, null=True)),
                ('employee_name', models.CharField(blank=True, max_length=255, null=True)),
                ('employee_email', models.CharField(blank=True, max_length=255, null=True)),
                ('pg_level', models.CharField(blank=True, max_length=255, null=True)),
                ('daily_expected_hours', models.CharField(blank=True, max_length=255, null=True)),
                ('employee_type', models.CharField(blank=True, max_length=255, null=True)),
                ('bill_to_county', models.CharField(blank=True, max_length=255, null=True)),
                ('geography', models.CharField(blank=True, max_length=255, null=True)),
                ('hp_level', models.CharField(blank=True, max_length=255, null=True)),
                ('seat_country_code', models.CharField(blank=True, max_length=255, null=True)),
                ('seat_country', models.CharField(blank=True, max_length=255, null=True)),
                ('wbs', models.CharField(blank=True, max_length=255, null=True)),
                ('wbs_description', models.CharField(blank=True, max_length=255, null=True)),
                ('aa_type', models.CharField(blank=True, max_length=255, null=True)),
                ('attribute', models.CharField(blank=True, max_length=255, null=True)),
                ('attribute_2', models.CharField(blank=True, max_length=255, null=True)),
                ('short_text', models.CharField(blank=True, max_length=255, null=True)),
                ('hp_labor_rate', models.DecimalField(blank=True, decimal_places=15, max_digits=38, null=True)),
                ('usd_labor_currency', models.DecimalField(blank=True, decimal_places=15, max_digits=38, null=True)),
                ('hours', models.DecimalField(blank=True, decimal_places=15, max_digits=38, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'TMP_TRANSITION_BW',
            },
        ),
    ]

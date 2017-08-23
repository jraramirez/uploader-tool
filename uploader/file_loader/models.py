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
    report_month = models.CharField(max_length=255)
    employee_id = models.CharField(db_column='Employee ID', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    region = models.CharField(db_column='Region', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pm_name = models.CharField(db_column='PM Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

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

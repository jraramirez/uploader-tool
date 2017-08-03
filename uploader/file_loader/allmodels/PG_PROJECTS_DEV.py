# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

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

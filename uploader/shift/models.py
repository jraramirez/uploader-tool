from django.db import models
import json

# Create your models here.

class TestFIN005Raw(models.Model):
    id = models.CharField(max_length=255, default = '', primary_key=True)
    PERIOD = models.CharField(max_length=255, default = '')
    EMPLOYEE_NUMBER = models.CharField(max_length=255, default = '')
    EMPLOYEE_NAME = models.CharField(max_length=255, default = '')
    SUPPLEMENTAL_PAY_TYPE = models.CharField(max_length=255, default = '')
    CLAIM_MONTH = models.CharField(max_length=255, default = '')
    CLAIM_DATE = models.CharField(max_length=255, default = '')
    IS_LATE_FILING = models.CharField(max_length=255, default = '')
    REGULAR_HOURS = models.CharField(max_length=255, default = '')
    OT_TIME_IN = models.CharField(max_length=255, default = '')
    OT_TIME_OUT = models.CharField(max_length=255, default = '')
    TOTAL_OT_HOURS = models.CharField(max_length=255, default = '')
    OVERTIME_TIME_AMT_PAY = models.CharField(max_length=255, default = '')
    STANDBY_HOURS = models.CharField(max_length=255, default = '')
    STNDBY_AMT = models.CharField(max_length=255, default = '')
    SHIFT_HOURS = models.CharField(max_length=255, default = '')
    SHIFT_AMT = models.CharField(max_length=255, default = '')
    TOTAL_PAYOUT_PHP = models.CharField(max_length=255, default = '')
    TOTAL_PAYOUT_USD = models.CharField(max_length=255, default = '')
    TOTAL_PAYOUT_PERCENT = models.CharField(max_length=255, default = '')
    COMMENTS = models.CharField(max_length=255, default = '')
    PRJ_CUSTOMER = models.CharField(max_length=255, default = '')
    PRJ_CUSTOMER2 = models.CharField(max_length=255, default = '')
    PROJECT = models.CharField(max_length=255, default = '')
    PROJECT2 = models.CharField(max_length=255, default = '')
    WBS = models.CharField(max_length=255, default = '')
    WBS_DESCRIPTION = models.CharField(max_length=255, default = '')
    DCL_FINAL = models.CharField(max_length=255, default = '')
    LOCATION_CODE = models.CharField(max_length=255, default = '')
    MANAGER_ID = models.CharField(max_length=255, default = '')
    MANAGER_NAME = models.CharField(max_length=255, default = '')
    MODIFIED = models.CharField(max_length=255, default = '')

class META_SHIFT(models.Model):
    id = models.IntegerField
    sheetNames = models.CharField(max_length=255)
    colNames = models.CharField(max_length=500)
    fileName = models.CharField(max_length=255)
    fileType = models.CharField(max_length=255)
    numberOfColumns = models.IntegerField()
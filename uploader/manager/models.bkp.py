from django.db import models

# Create your models here.

class MTDTA_UPLOADER(models.Model):
    uploader = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    source_path = models.CharField(max_length=255)
    server = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=255)
    sheet_name = models.CharField(max_length=255)
    target_schema = models.CharField(max_length=255)
    target_table = models.CharField(max_length=255)
    last_update_uid = models.CharField(max_length=255)
    last_update = models.DateField()
    
class MTDTA_UPLOADER_PARAMS(models.Model):
    uploader = models.ForeignKey(MTDTA_UPLOADER, on_delete=models.CASCADE)
    parameter = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    data_type = models.CharField(max_length=255)
    is_required = models.CharField(max_length=1, default = 'N')
    default_value = models.CharField(max_length=255, default = 'N')
    format = models.CharField(max_length=255)
    last_update_uid = models.CharField(max_length=255)
    last_update = models.DateField()
    
class MTDTA_UPLOADER_COLS(models.Model):
    uploader = models.ForeignKey(MTDTA_UPLOADER, on_delete=models.CASCADE)
    column = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    data_type = models.CharField(max_length=255)
    is_required = models.CharField(max_length=1, default = 'N')
    default = models.CharField(max_length=255, default = 'N')
    format = models.CharField(max_length=255)
    last_update_uid = models.CharField(max_length=255)
    last_update = models.DateField()
from django.db import models

# Create your models here.

class MTDTA_UPLOADER(models.Model):
    uploader = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    target_schema = models.CharField(max_length=255)
    target_table = models.CharField(max_length=255)
    date_created = models.DateField()
    
class MTDTA_UPLOADER_PARAMS(models.Model):
    uploader = models.ForeignKey(MTDTA_UPLOADER, on_delete=models.CASCADE)
    parameter = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    dataType = models.CharField(max_length=255)
    isRequired = models.CharField(max_length=1, default = 'N')
    default = models.CharField(max_length=255, default = 'N')
    format = models.CharField(max_length=255)
    date_created = models.DateField()
    
class MTDTA_UPLOADER_COLS(models.Model):
    uploader = models.ForeignKey(MTDTA_UPLOADER, on_delete=models.CASCADE)
    column = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    dataType = models.CharField(max_length=255)
    isRequired = models.CharField(max_length=1, default = 'N')
    default = models.CharField(max_length=255, default = 'N')
    format = models.CharField(max_length=255)
    date_created = models.DateField()

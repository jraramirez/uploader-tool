from django.db import models

class MTDTA_UPLOADER(models.Model):
    uploader = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default = '[name]-uploader')
    description = models.CharField(max_length=255, default = 'File upload of ...')
    source_path = models.CharField(max_length=255, default = '\pg_bizops\FILE_UPLOADER\[source folder]')
    server = models.CharField(max_length=255, default = '16.179.110.132')
    file_name = models.CharField(max_length=255, default = '')
    file_type = models.CharField(max_length=255, default = '.xlsx')
    sheet_name = models.CharField(max_length=255, default = 'Sheet1')
    target_schema = models.CharField(max_length=255, default = 'FPD')
    target_table = models.CharField(max_length=255, default = 'TMP_')
    last_update_uid = models.CharField(max_length=255, default = 'username@hpe.com')
    last_update = models.DateField()

    def __str__(self):
        return 'Uploader: ' + self.name
    
    class Meta:
        managed = True
        db_table = 'MTDTA_UPLOADER'

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

    def __str__(self):
        return 'Uploader ID:' + str(self.uploader_id) + '; Parameter: ' + self.name
        
    class Meta:
        managed = True
        db_table = 'MTDTA_UPLOADER_PARAMS'
    
class MTDTA_UPLOADER_COLS(models.Model):
    uploader = models.ForeignKey(MTDTA_UPLOADER, on_delete=models.CASCADE)
    column = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default = 'Column for ...')
    data_type = models.CharField(max_length=255, default = 'str')
    is_required = models.CharField(max_length=1, default = 'N')
    default = models.CharField(max_length=255, default = 'N')
    format = models.CharField(max_length=255)
    last_update_uid = models.CharField(max_length=255)
    last_update = models.DateField()
    
    def __str__(self):
        return 'Uploader ID: ' + str(self.uploader_id) + '; Column: ' + self.name
        
    class Meta:
        managed = True
        db_table = 'MTDTA_UPLOADER_COLS'
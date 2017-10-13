from django.db import models

class MTDTA_UPLOADER(models.Model):
    uploader = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default = '[name]-uploader')
    description = models.CharField(max_length=255, default = 'File loader for ...')
    source_path = models.CharField(max_length=255, default = '\pg_bizops\FILE_UPLOADER\[source folder]')
    server = models.CharField(max_length=255, default = '16.179.110.132')
    file_name = models.CharField(max_length=255, default = '')
    file_type = models.CharField(max_length=255, default = '.xlsx')
    sheet_name = models.CharField(max_length=255, default = 'Sheet1')
    delimiter = models.CharField(max_length=255, default = ',')
    start_row = models.IntegerField(default = 0)
    target_schema = models.CharField(max_length=255, default = 'FPD')
    target_table = models.CharField(max_length=255, default = 'TMP_')
    email_sender = models.CharField(max_length=255, default = 'pg_bizopssupport@hpe.com')
    email_recipient = models.CharField(max_length=255, default = 'username@hpe.com')
    email_cc = models.CharField(max_length=255, default = 'pg_bizopssupport@hpe.com')
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
    is_required = models.CharField(max_length=1, default = 'N')
    max_length = models.CharField(max_length=255, default = '255')
    default = models.CharField(max_length=255, default = 'None')
    format = models.CharField(max_length=255, default = 'None')
    last_update_uid = models.CharField(max_length=255, default = 'username@hpe.com')
    last_update = models.DateField()
    
    def __str__(self):
        return 'Uploader ID: ' + str(self.uploader_id) + '; Column: ' + self.name
        
    class Meta:
        managed = True
        db_table = 'MTDTA_UPLOADER_COLS'

class UTL_FILE_LOADER_BOT_LOGS(models.Model):
    id = models.AutoField(primary_key=True)
    uploader_name = models.CharField(max_length=255)
    last_update_uid = models.CharField(max_length=255)
    update_start_timestamp = models.DateTimeField()
    update_end_timestamp = models.DateTimeField()
    status = models.CharField(max_length=255)
    error_details = models.CharField(max_length=4000, null=True)
    warning_details = models.CharField(max_length=4000, null=True)
    input_file = models.CharField(max_length=4000, null=True)
    email_sent = models.CharField(max_length=255)
    table_truncated = models.CharField(max_length=255)
    
    class Meta:
        managed = True
        db_table = 'UTL_FILE_LOADER_BOT_LOGS'
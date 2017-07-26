## Setting Up a New Uploader

### Target Table Setup

1. Make sure that the target table is properly setup. The table should use a column named id as primary key

2. Make the file loader bot recognize the target table 
    - run the script recognize.bat

    recognize.bat:
        C:\Python27\python.exe D:\PG_BIZOPS\Developers\upload-to-db\uploader\manage.py inspectdb > D:\PG_BIZOPS\Developers\upload-to-db\uploader\file_loader/models.py

### Metadata Table Setup

1. Create an entry for the new uploader into the metadata tables

    Use template.sql
    or go to http://a4pgbizopsdev.svcs.entsvcs.net/admin
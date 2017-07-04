# Uploader Tool
    DEV Version: http://a4pgbizopsdev.svcs.entsvcs.net/uploader
    PROD Version:

### About Uploader Tool

    The tool used to upload reports in excel or csv format to DNA databases. This tool can be used to standardize all loads of database tables from files across the production environment. It can be leveraged by all existing and future developments which involves file loading mechanism. It will greatly benefit the business as this will speed up development, utilize available infrastructure resource, reduce support costs, and reduce feature upgrade costs. 

### Features

    - Report errors in the file if not in the expected state. 
    - Detect Null values for required columns.
    - Detect columns if they follow expected data types.

### Deployment
    https://github.hpe.com/TTT/uploader-tool/blob/master/deployment.md

### Running in the Server
    1. Go to the directory uploader-tool/uploader
    2. Run the command python manage.py 0.0.0.0:80
    3. Access the web client at http://a4pgbizopsdev.svcs.entsvcs.net/uploader


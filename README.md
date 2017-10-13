# File Loader Bot

DEV Version: http://a4pgbizopsdev.svcs.entsvcs.net/uploader

PROD Version: http://a4pgbizops.svcs.entsvcs.net/uploader

### About File Loader Bot

The tool used to upload reports in excel or csv format to databases. This tool is used to standardize all loads of database tables from files across the production environment. It can be leveraged by all existing and future developments which involves file loading mechanism. It will greatly benefit the business as this will speed up development, utilize available infrastructure resource, reduce support costs, and reduce feature upgrade costs.

In order to operate properly, the file loader bot will utilize database tables called metadata tables. These tables, after setting up properly, will direct the bot on how the files are loaded into target tables. The file loader bot will communicate everything it does with the users via email.

### Process Flow

#### Overview
![Simple](https://github.hpe.com/TTT/uploader-tool/blob/master/images/simple.png)

#### Detailed View
![Detailed](https://github.hpe.com/TTT/uploader-tool/blob/master/images/detailed.png)

### File Loader Bot Features

* Scheduled file upload to databases using SQL Server Agent jobs
* Setup of file upload metadata using the File Loader Administration Page
* Email notifications for all the file upload activities
* Logging of all the file upload activities into a database table

### [About Metadata Tables](https://github.hpe.com/TTT/uploader-tool/blob/master/metadata-tables.md)

### [Setting Up a New Uploader](https://github.hpe.com/TTT/uploader-tool/blob/master/setup-new-uploader.md)

### [File Loader Bot Usage](https://github.hpe.com/TTT/uploader-tool/blob/master/file-loader-bot-usage.md)

### [Setting Up the Metadata Tables](https://github.hpe.com/TTT/uploader-tool/blob/master/setup-metadata-tables.md)

### [Scheduling an Automated Upload Using SQL Server Agent](https://github.hpe.com/TTT/uploader-tool/blob/master/setup-upload-schedule.md)

### [About File Loader Administrator Page](https://github.hpe.com/TTT/uploader-tool/blob/master/setup-django-admin.md)

### [Setting Up settings.py](https://github.hpe.com/TTT/uploader-tool/blob/master/setup-settings-py.md)

### [Deployment](https://github.hpe.com/TTT/uploader-tool/blob/master/deployment.md)

### Other Features

The bot will always provide useful messages/notifications if file upload activities have something to report or if there are errors. The possible reports/errors are enumerated below.
* The bot can verify if the source path where the input file is expected by the upload exists.
* The bot can verify if the expected input file exists in the source path.
* The bot can verify if the expected input file has the correct file type. If the file does not have the expected file type.
* The bot can verify if the a file uploader has no instructions/setup yet.
* The bot can verify if if all source fields expected are in the input file.
* The bot can verify if the source fields expected has missing fields.
* The bot can verify if the source fields expected has extra fields.
* The bot can verify if the specified target table is existing in the database schema.
* The bot can verify if the specified database schema is exsisting.
* The bot can handle data in the file with commas for CSV files.
* The bot is able to transfer the file to the archive folder if the file loading is successful.
* The bot is able to transfer the file to the error folder if the file loading is unsuccessful.
* Start row metadata – Uploader setup can now set the start row from the file where the uploader will start reading data
* Max length metadata – Uploader setup can now set the maximum length of column values
* Email sender/recipient/cc metadata – Uploader setup can now set the email of the sender/recipient/cc of the notifications
* Recognition of target tables – Improved method of recognizing new/updated target tables. List of target tables are no longer maintained in a file. They are now maintained in the metadata tables
* Detect input file based on the file name format
* Saving of the upload file name and file date information to the target table
* Validation of target table column names
* File loader bot can now be scheduled using SQL Server Agent jobs

### New Features
* Logging of all uploads into ```[FPD].[UTL_FILE_LOADER_BOT_LOGS]```

### Removed Features
* Max length of values validation – Validates a column if it includes values that exceed the maximum allowed length
* The bot can verify if there are null records in the source file that is expected to have a value.
* MTDTA_UPLOADER_PARAMS Metadata Table

### In Progress
* Verify that the number of rows loaded into the table is matching with the contents of the file.
* Provide a useful message if the number of rows are not matching. Show the number of rows loaded to the table and number of rows in the source file.
* Check that the file is reasonable depending on the count of records in the file compared to the count of the previous files that were successfully loaded.
* Check that the file is reasonable depending on fields from the file and the destination table.
* Check that the file is reasonable depending on file size compared to the file size of the previous files that were successfully loaded.
* The bot will send an email to the support team if the load was successful or not.

### Architecture
#### Technologies:
* Python 3.5.x
* Django 1.11.2 Framework

The implementation will utilize python libraries that can read any type of csv or excel files and can perform file operations. Django framework will handle the application’s server connection configurations.

#### Python and Django Libraries:
* django-pyodbc and django-pyodbc-azure – for connecting to server databases using ODBC connection
* django-db-models – for creating/modifying db tables within the application
* django-db-transactions – for doing sql transactions within the application
* openpyxl – for spreadsheet file operations
* os – for file and directory operations
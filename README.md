# File Loader Bot

DEV Version: http://a4pgbizopsdev.svcs.entsvcs.net/uploader

PROD Version:

### About File Loader Bot

The tool used to upload reports in excel or csv format to databases. This tool is used to standardize all loads of database tables from files across the production environment. It can be leveraged by all existing and future developments which involves file loading mechanism. It will greatly benefit the business as this will speed up development, utilize available infrastructure resource, reduce support costs, and reduce feature upgrade costs.

In order to operate properly, the file loader bot will utilize database tables called metadata tables. These tables, after setting up properly, will direct the bot on how the files are loaded into target tables. The file loader bot will communicate everything it does with the users via email.

### Process Flow

#### Overview
![Simple](https://github.hpe.com/TTT/uploader-tool/blob/master/images/simple.png)

#### Detailed View
![Detailed](https://github.hpe.com/TTT/uploader-tool/blob/master/images/detailed.png)

### Metadata Tables

https://github.hpe.com/TTT/uploader-tool/blob/master/metadata-tables.md

### Setting Up a New Uploader

https://github.hpe.com/TTT/uploader-tool/blob/master/setup-new-uploader.md

### File Loader Bot Usage

https://github.hpe.com/TTT/uploader-tool/blob/master/file-loader-bot-usage.md

### File Loader Bot Features

* Verify that source path exists.
* Verify that the file exists in the source path.
* Verify if the file to upload is in the correct file type. If the file is not in the expected file type, provide a useful message.
* Provide useful message if the file upload has no instructions/setup yet.
* Validate that the parameters from the caller meet expectations.
* Check if all source fields expected is in the file.
* Provide a useful message if the source fields expected has missing fields.
* Provide a useful message if the source fields expected has extra fields.
* Provide a useful message specifying the missing or extra fields. The user should know what to correct in the file.
* Detect if the data type of a field source is not matching with the target column of the target table.
* Provide a useful message if the data type of the source is not matching with data type of the column in the target table.
* Check if the target table is existing in the database schema.
* Provide a useful message if the target table is not existing in the database.
* Detect if there are null records in the source file that is expected to have a value.
* Provide a useful message for null records that should have a value.

### New

* Handle data in the file with commas for CSV files.
* The bot should be able to transfer the file to the archive folder if the file loading is successful.
* The bot should provide an error message for unsuccessful file load and transfer the file to the error folder.
* The bot will send an email to the support team if the load was successful or not.

#### In Progress
* Verify that the number of rows loaded into the table is matching with the contents of the file.
* Provide a useful message if the number of rows are not matching. Show the number of rows loaded to the table and number of rows in the source file.
* Check that the file is reasonable depending on the count of records in the file compared to the count of the previous files that were successfully loaded.
* Check that the file is reasonable depending on fields from the file and the destination table.
* Check that the file is reasonable depending on file size compared to the file size of the previous files that were successfully loaded.

### Deployment

https://github.hpe.com/TTT/uploader-tool/blob/master/deployment.md

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
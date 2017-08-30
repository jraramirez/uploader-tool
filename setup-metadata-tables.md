## Setting Up Metadata Tables

When a new uploader is prepared, one of the requirements is to setup its metadata tables. There are two ways to setup the metadata tables of a new uploader.

### Method 1 - Use the Template
The metadata tables are setup by simply inserting values to the tables. There is a template ```template.sql``` that can be found here: https://github.hpe.com/TTT/uploader-tool/tree/master/sql

There are also samples that can be found in the link. When the template is completed, run it into the SQL server.

### Method 2 - Use the Django Admin Page
Insert values to the metadata tables by using the django admin page. Go to http://a4pgbizopsdev.svcs.entsvcs.net/admin

How to use the Django admin page:
https://github.hpe.com/TTT/uploader-tool/blob/master/setup-django-admin.md
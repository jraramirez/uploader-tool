## Setting Up a New Uploader

### A. Target Table Setup

1. Make sure that the target table is properly setup. The table should use a column named ```id``` as primary key and as the first column. All other columns should use ```nvarchar``` as data type and are NULLABLE. There should be last two additional columns with names ```file_name``` and ```file_date```.

    Sample create script of a proper table:
    ```sql
    CREATE TABLE STG_TARGET_TABLE(
    	[id] [bigint] NOT NULL,             -- REQUIRED
    	[col1] [nvarchar](255) NULL,
    	[col2] [nvarchar](255) NULL,
    	[file_name] [nvarchar](255) NULL,   -- REQUIRED
    	[file_date] [nvarchar](255) NULL,   -- REQUIRED
            PRIMARY KEY (id)
    )
    ```

2. Make the file loader bot recognize the new target table.

    Simply visit this url: http://a4pgbizopsdev.svcs.entsvcs.net/uploader/refresh

    Visit this url whenever there are new changes in the target table and metadata table.

### B. Metadata Table Setup

1. Create an entry for the new uploader into the metadata tables. Follow the instructions [here](https://github.hpe.com/TTT/uploader-tool/blob/master/setup-metadata-tables.md).

### C. Source Folder Setup

1. Create the actual corresponding folder for the new uploader under ```\\[server]\pg_bizops\FILE_UPLOADER\[folder name]```.

    Make sure that ```[folder name]``` is equivalent to your input on the metadata table under ```[source path]``` field when ```step B``` was performed.

2. Under the folder you have created in ```step 1```, ```\\[server]\pg_bizops\FILE_UPLOADER\[folder name]```, create 3 folders named ```New```, ```Archive```, and ```Error```. The files to be uploaded will be put to ```New``` folder.
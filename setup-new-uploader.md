## Setting Up a New Uploader

#### A. Target Table Setup

1. Make sure that the target table is properly setup. The table should use a column named ```id``` as primary key.

2. Make the file loader bot recognize the new target table.
    1. Add the name of the target table to the list of target tables: ```target-tables.csv```
    
        The location of this list is here: ```\\[server]\pg_bizops\uploader-tool\maintenance\target-tables.csv```

    2. Run the script ```recognize-tables.bat``` while remotely connected to the server.
    
        The location of this script is here: ```D:\pg_bizops\uploader-tool\executables\recognize-tables.bat```

#### B. Metadata Table Setup

1. Create an entry for the new uploader into the metadata tables. Follow the instructions here:

    https://github.hpe.com/TTT/uploader-tool/blob/master/setup-metadata-tables.md

#### C. Source Folder Setup

1. Create the actual corresponding folder for the new uploader under ```\\[server]\pg_bizops\FILE_UPLOADER\[folder name]```.

    Make sure that ```[folder name]``` is equivalent to your input on the metadata table under ```[source path]``` field when ```step B``` was performed.

2. Under the folder you have created in ```step 1```, ```\\[server]\pg_bizops\FILE_UPLOADER\[folder name]```, create 3 folders named ```New```, ```Archive```, and ```Error```.
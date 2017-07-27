## Setting Up a New Uploader

#### A. Target Table Setup

1. Make sure that the target table is properly setup. The table should use a column named id as primary key.

2. Make the file loader bot recognize the new target table.
    1. Add the name of the target table to the list of target tables: 'target-tables.csv'
    \\[server]\pg_bizops\uploader-tool\executables\target-tables.csv

    2. Run the script 'recognize-tables.bat'
    https://github.hpe.com/TTT/uploader-tool/tree/master/uploader/executables/recognize-tables.bat

#### B. Metadata Table Setup

1. Create an entry for the new uploader into the metadata tables
https://github.hpe.com/TTT/uploader-tool/blob/master/setup-metadata-tables.md
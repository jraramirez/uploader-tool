## Setting Up Metadata Tables Using the Django Admin Page

#### A. Access the Django Admin Page
1. Go to http://a4pgbizopsdev.svcs.entsvcs.net/admin
2. Ask the developers for the credentials to use.

#### B. Add a New Uploader in Metadata Uploader Table
To add a new uploader, add a new row in the metadata uploader table using the following steps.

Use the information here as guide in filling up the fields: https://github.hpe.com/TTT/uploader-tool/blob/master/metadata-tables.md
1. On the django admin page, click the ```Mtdta_ploaders``` under MANAGER.
2. On the resulting page in ```step 1```, click the ```ADD MTDTA_UPLOADER +``` button on the upper right.
3. Fill up the fields with the desired values and click ```SAVE``` when finished.

#### C. Add Parameters in Metadata Uploader Parameters Table
To add new parameters for the new uploader, add new rows in the metadata uploader parameters table using the following steps.

Use the information here as guide in filling up the fields: https://github.hpe.com/TTT/uploader-tool/blob/master/metadata-tables.md
1. On the django admin page, click the ```Mtdta_uploader_paramss``` under MANAGER.
2. On the resulting page in ```step 1```, click the ```ADD MTDTA_UPLOADER_PARAMS +``` button on the upper right.
3. Select the name of the uploader you have created in ```step B```.
4. Fill up the fields with the desired values and click ```SAVE``` when finished.
5. Repeat the previous steps to add another row for another parameter.

#### D. Add Parameters in Metadata Uploader Parameters Table
To add new columns for the new uploader, add new rows in the metadata uploader columns table using the following steps.

Use the information here as guide in filling up the fields: https://github.hpe.com/TTT/uploader-tool/blob/master/metadata-tables.md
1. On the django admin page, click the ```Mtdta_uploader_colss``` under MANAGER.
2. On the resulting page in ```step 1```, click the ```ADD MTDTA_UPLOADER_COLS +``` button on the upper right.
3. Select the name of the uploader you have created in ```step B```.
4. Fill up the fields with the desired values and click ```SAVE``` when finished.
5. Repeat the previous steps to add another row for another column.

#### E. Editing the Metadata Tables
1. Should you wish to edit the values of the metadata tables, go to the desired table under MANAGER.
2. On the resulting page in ```step 1```, Find the row to be edited.
3. Fill up the fields with the desired new values and click ```SAVE``` when finished.
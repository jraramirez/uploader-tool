## Metadata Tables

### Overview
![Metadata Tables](https://github.hpe.com/TTT/uploader-tool/blob/master/images/metadata-tables.png)

These tables are found in the **Future Proof Database (FPD)** with the following names:
* ```MTDTA_UPLOADER``` - Uploaders Metadata Table
* ```MTDTA_UPLOADER_COLS``` - Columns Metadata Table

### Uploaders Metadata Table

This table has the data that an uploader needs to properly upload a file to a target table

* **Name** - Name of the uploader
* **Description** - Description of the uploader
* **Source path** - The path to the directory where the uploader will expect the source file.
* **Server** - The server where the file loader bot is deployed and where the source file will be retrieved 
* **File Name** - The file name format that the uploader will expect in the name of the source file
* **File Type** - The file extension that the uploader will expect in the name of the source file
* **Sheet Name** - The sheet name that the uploader will expect in the source file.
* **Start Row** - The row number that indicates where the uploader should start reading data (0 means first row)
* **Target Schema** - The schema where the uploader will expect the target table
* **Target Table** - The target table where the uploader will send the source file data
* **Email Sender** - The email address of the sender of uploader notifications 
* **Email Recipient** - The email address of the recipient of uploader notifications 
* **Email CC** - The email address of the other recipient of uploader notifications 
* **Last Update UID** - ID of the user that most recently updated the metadata table 
* **Last Update** - Date when the metadata table was last updated
<!-- 
#### Parameters Metadata Table
This table has the data that an uploader needs to properly validate a file by its parameters before it is uploaded to a target table
* Uploader - ID of the uploader where this parameter is associated
* Name - Name of the parameter
* Description - Description of the parameter
* Data Type - Data type of the parameter
* Is Required - Indicator that says if the parameter is required or not
* Default Value - The default value set for the parameter
* Format - The format that the parameter is expected to follow
* Last Update UID - ID of the user that most recently updated the parameter metadata table 
* Last Update - Date when the parameter metadata table was last updated -->

### Columns Metadata Table
This table has the data that an uploader needs to properly validate a file by its columns before it is uploaded to a target table
* **Uploader** - ID of the uploader where this column is associated
* **Name** - Name of the column
* **Description** - Description of the column
* **Is Required** - Indicator that says if the column is required or not
* **Max Length** - The maximum length of the value allowed in the column
* **Default** - The default value set for the column
* **Format** - The format that the column is expected to follow
* **Last Update UID** - ID of the user that most recently updated the column metadata table 
* **Last Update** - Date when the column metadata table was last updated

### Notes on the Metadata Table Fields

###### Sheet Name Field
Leave this field blank if the input file is a ```.csv``` file

###### Source Path Field
Make sure that this folder exists under ```\\[server]\pg_bizops\FILE_UPLOADER\```

###### Is Required Field
The Is Required field should only have values ```'Y'``` or ```'N'```

###### Max Length Field
The values read by the uploader are all treated as string by default. This is the maximum lenght of the string values

###### Format Field
This is not required. There is no format validation implemented yet.

###### Default Value Field
This is not required. There is no default values validation implemented yet.

Learn how to setup metadata tables [here](https://github.hpe.com/TTT/uploader-tool/blob/master/setup-metadata-tables.md).

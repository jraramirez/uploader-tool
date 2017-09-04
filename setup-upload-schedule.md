## Setting Up Schedule of File Upload

The SQL Server Agent can use the file loader bot to setup file uploads with any desired schedule. The uploads are treated as Jobs using this technology.

#### Setup Using Microsoft SQL Server Management Studio
1. After connecting to the server, look for ```SQL Server Agent```

    Right click ```SQL Server Agent``` and select ```New```, then ```Job...```
2. Under ```General``` tab, provide a descriptive name for the new Job and set the owner to ```A4PGBIZOPS\Administrator```
3. Under ```Steps``` tab, click ```New```, then provide a descriptive name for the new step.
    
    Change the ```Type``` to ```Operating System (CmdExec)```

    Under command text area, input the following:
    ```py -2.7 D:\pg_bizops\uploader-tool\scheduler\run-auto.py [uploader-name]```
    
    Click ```OK```
4. Under ```Schedules``` tab, setup new schedule for the upload by selecting ```New...```. An existing schedule can be used by selecting ```Pick...```
    
    Adjust the appropriate schedule type, frequency, and duration for the file upload.
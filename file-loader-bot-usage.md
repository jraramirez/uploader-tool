## Using the File Loader Bot

### Running in the Server
Make sure that the file loader bot is running in the server. The methods below will not work if the file loader bot is not running.

Connect to the server remotely and run the script 
 ```runserver.bat```.

The location of this script in the server is: 

```D:\pg_bizops\uploader-tool\executables\runserver.bat```

### Manually Trigger an Upload
The file loader bot can be used to manually trigger an upload by visiting a url in a web browser.
When an uploader is properly setup, visit the url with this format in a web browser to trigger an upload for ```[uploader name]``` uploader:

 ```http://a4pgbizopsdev.svcs.entsvcs.net/uploader/auto/[uploader name]```

### Automated Upload
Use the SQL Server Agent to schedule the automated upload. On the job setup of the SQL Server Agent, use python run the file

```\pg_bizops\uploader-tool\scheduler\run-auto.py [uploader name]```

Learn how to schedule an automated upload using Using SQL Server Agent [here](https://github.hpe.com/TTT/uploader-tool/blob/master/setup-upload-schedule.md).

### Assisted Upload
The file loader bot has a simple user interface where the upload can be performed.
The user interface can be found here: 

```http://a4pgbizopsdev.svcs.entsvcs.net/uploader/assisted/[uploader name]```

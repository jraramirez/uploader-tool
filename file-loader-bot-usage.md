## Using the File Loader Bot

#### Running in the Server
Make sure that the file loader bot is running in the server. The methods below will not work if the file loader bot is not running.

Connect to the server remotely and run the script ```runserver.bat```

The location of this script is here: ```D:\pg_bizops\uploader-tool\executables\runserver.bat```

#### Manually Trigger an Upload
The file loader bot can be used to manually trigger an upload by visiting a url in a web browser.
When an uploader is properly setup, visit the url with this format in a web browser: ```http://a4pgbizopsdev.svcs.entsvcs.net/uploader/auto/[uploader name]```

#### Automated Upload
The file loader bot maintains a list of active uploaders and has a simple scheduler that triggers them every hour. When an uploader is properly setup, the bot includes this uploader to its set of active uploaders. For now, kindly ask a developer if you wish to add an uploader to the list of active uploaders.

#### Assisted Upload
The file loader bot has a simple user interface where the upload can be performed.
The user interface can be found here ```http://a4pgbizopsdev.svcs.entsvcs.net/uploader``` [The Site is Under Construction]

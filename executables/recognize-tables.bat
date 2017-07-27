set /p tables=<target-tables.csv
set tables=%tables:,=%
python ..\uploader\manage.py inspectdb %tables% > ..\uploader\file_loader\models.py

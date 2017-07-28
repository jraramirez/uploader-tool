import requests
import time

while True:
    
    r = requests.get("http://a4pgbizopsdev.svcs.entsvcs.net/uploader/auto/shift/")
    time.sleep(60)

import requests

while True:
    
    r = requests.get("http://localhost:8000/uploader/auto/shift/")
    time.sleep(60)

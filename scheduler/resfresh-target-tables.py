import requests
import sys

uploader = str(sys.argv[1])

r = requests.get("http://a4pgbizopsdev.svcs.entsvcs.net/uploader/refresh/")
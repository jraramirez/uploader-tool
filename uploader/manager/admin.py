from django.contrib import admin
from .models import MTDTA_UPLOADER
from .models import MTDTA_UPLOADER_PARAMS
from .models import MTDTA_UPLOADER_COLS

# Register your models here.

admin.site.register(MTDTA_UPLOADER)
admin.site.register(MTDTA_UPLOADER_PARAMS)
admin.site.register(MTDTA_UPLOADER_COLS)
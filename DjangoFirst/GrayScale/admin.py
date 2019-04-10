from django.contrib import admin

# Register your models here.
from .models import Document

# modelを管理対象にする
admin.site.register(Document)

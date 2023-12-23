from django.contrib import admin
from Frontend.models import contactmedb
from Frontend.models import Resume
import Frontend

# Register your models here.

admin.site.register(contactmedb),
admin.site.register(Resume)

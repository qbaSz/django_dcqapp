from django.contrib import admin

# Register your models here.
from .models import DCAuthor, DCEntry

admin.site.register(DCAuthor)
admin.site.register(DCEntry)

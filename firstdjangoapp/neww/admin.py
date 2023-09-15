from django.contrib import admin
from neww.models import Neww

class NewwAdmin(admin.ModelAdmin):
    list_display=('title', 'description', 'news_image')

admin.site.register(Neww, NewwAdmin)

# Register your models here.

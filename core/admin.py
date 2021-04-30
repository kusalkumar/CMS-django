from django.contrib import admin

#n Register your models here.
from .models import Core


@admin.register(Core)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',), }
#admin.site.register(Core)

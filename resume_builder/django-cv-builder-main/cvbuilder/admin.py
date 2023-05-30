from django.contrib import admin
from .models import Resume, Experience, Template

# Register your models here.

admin.site.register(Resume)
admin.site.register(Experience)
admin.site.register(Template)
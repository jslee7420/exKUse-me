from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, NativeLanguage, StudyingLanguage

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(NativeLanguage)
admin.site.register(StudyingLanguage)
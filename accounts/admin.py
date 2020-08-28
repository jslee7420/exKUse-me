from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, NativeLanguage, StudyingLanguage

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(NativeLanguage)
admin.site.register(StudyingLanguage)



class CustomUserAdmin(UserAdmin):
    # fieldsets : 관리자 리스트 화면에서 출력될 폼 설정 부분
    UserAdmin.fieldsets[1][1]['fields']+=('country','phone_number','major','introduction', 'online_letter','profile_picture')
    # add_fieldsets : User 객체 추가 화면에 출력될 입력 폼 설정 부분
    UserAdmin.add_fieldsets += (
        (('Additional Info'),{'fields':('country','phone_number','major','introduction', 'online_letter','profile_picture')}),
    )
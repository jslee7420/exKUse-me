# Generated by Django 3.1 on 2020-08-28 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_native_language_studying_language'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='native_language',
            new_name='NativeLanguage',
        ),
        migrations.RenameModel(
            old_name='studying_language',
            new_name='StudyingLanguage',
        ),
    ]

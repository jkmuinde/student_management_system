# Generated by Django 3.0.7 on 2021-02-19 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210218_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='reg_no',
            new_name='regno',
        ),
    ]

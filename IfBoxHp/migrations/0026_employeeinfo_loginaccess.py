# Generated by Django 3.0.6 on 2020-09-30 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IfBoxHp', '0025_auto_20200930_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeinfo',
            name='loginaccess',
            field=models.BooleanField(default=True),
        ),
    ]
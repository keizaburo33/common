# Generated by Django 3.0.6 on 2020-09-24 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IfBoxHp', '0019_auto_20200924_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admininformation',
            old_name='aduminname',
            new_name='adminname',
        ),
    ]

# Generated by Django 3.0.6 on 2020-09-24 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IfBoxHp', '0017_admininformation_aduminname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admininformation',
            name='adminid',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='admininformation',
            name='adminpass1',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='admininformation',
            name='aduminname',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='admininformation',
            name='aduminpass2',
            field=models.CharField(max_length=1000),
        ),
    ]
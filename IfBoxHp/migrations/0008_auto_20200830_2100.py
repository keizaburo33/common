# Generated by Django 3.0.6 on 2020-08-30 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IfBoxHp', '0007_userfriends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfriends',
            name='friendid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IfBoxHp.User'),
        ),
    ]

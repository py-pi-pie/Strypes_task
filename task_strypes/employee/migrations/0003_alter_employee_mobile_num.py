# Generated by Django 3.2.9 on 2022-04-08 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20220408_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='mobile_num',
            field=models.PositiveIntegerField(),
        ),
    ]

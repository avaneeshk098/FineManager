# Generated by Django 2.1.3 on 2018-11-19 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0002_auto_20181119_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fine',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.ManagerUser'),
        ),
    ]

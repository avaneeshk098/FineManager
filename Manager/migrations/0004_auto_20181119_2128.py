# Generated by Django 2.1.3 on 2018-11-19 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Manager', '0003_auto_20181119_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='fine',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.EmployeeUser'),
        ),
    ]
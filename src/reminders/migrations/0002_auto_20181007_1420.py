# Generated by Django 2.0.8 on 2018-10-07 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='documents.Document'),
        ),
    ]

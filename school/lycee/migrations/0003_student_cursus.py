# Generated by Django 3.0.7 on 2020-06-24 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0002_auto_20200624_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='cursus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lycee.Cursus'),
        ),
    ]

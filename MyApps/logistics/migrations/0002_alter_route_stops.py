# Generated by Django 5.0.9 on 2024-10-19 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='stops',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='stops'),
        ),
    ]

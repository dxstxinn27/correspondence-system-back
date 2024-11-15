# Generated by Django 5.0.9 on 2024-10-19 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameB', models.CharField(max_length=100, verbose_name='branch name')),
                ('location', models.CharField(max_length=255, verbose_name='branch location')),
            ],
            options={
                'verbose_name': 'branch',
                'verbose_name_plural': 'branches',
            },
        ),
    ]
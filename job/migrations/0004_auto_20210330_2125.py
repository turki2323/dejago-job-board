# Generated by Django 3.1.7 on 2021-03-30 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='publised_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]

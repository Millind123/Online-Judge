# Generated by Django 4.0.5 on 2022-07-04 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_alter_submission_submission_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submission_code',
            field=models.FileField(upload_to=''),
        ),
    ]

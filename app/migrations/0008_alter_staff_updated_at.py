# Generated by Django 4.2 on 2023-04-19 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_staff_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

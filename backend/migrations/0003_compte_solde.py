# Generated by Django 4.1.5 on 2023-01-14 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_client_code_cli_compte'),
    ]

    operations = [
        migrations.AddField(
            model_name='compte',
            name='solde',
            field=models.FloatField(default=250),
        ),
    ]
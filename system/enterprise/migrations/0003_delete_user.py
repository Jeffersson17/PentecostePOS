# Generated by Django 5.1.2 on 2024-12-03 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0002_remove_user_enterprise_alter_enterprise_options'),
        ('sales', '0003_alter_sales_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
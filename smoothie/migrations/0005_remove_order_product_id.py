# Generated by Django 3.2.5 on 2021-08-02 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smoothie', '0004_alter_products_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_id',
        ),
    ]
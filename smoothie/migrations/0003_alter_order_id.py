# Generated by Django 3.2.5 on 2021-08-02 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smoothie', '0002_auto_20210728_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

# Generated by Django 4.0 on 2021-12-18 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_order_alter_menu_category_alter_menu_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='quantity',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
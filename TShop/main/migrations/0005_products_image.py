# Generated by Django 4.1 on 2022-09-09 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_categories_options_alter_products_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]

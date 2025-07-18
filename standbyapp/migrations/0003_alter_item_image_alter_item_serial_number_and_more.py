# Generated by Django 5.2.4 on 2025-07-15 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standbyapp', '0002_alter_item_image_alter_item_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='serial_number',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]

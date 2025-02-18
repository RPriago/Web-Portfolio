# Generated by Django 5.0.7 on 2024-07-26 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_rename_catagory_category_alter_item_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='link',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default=2, upload_to='item_image'),
            preserve_default=False,
        ),
    ]

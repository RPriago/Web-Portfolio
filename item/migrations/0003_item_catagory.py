# Generated by Django 5.0.7 on 2024-07-23 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_item_alter_catagory_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='catagory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='item.catagory'),
            preserve_default=False,
        ),
    ]

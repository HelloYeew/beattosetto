# Generated by Django 3.2.8 on 2021-10-23 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beatmap_collections', '0011_alter_collection_collection_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='edit_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

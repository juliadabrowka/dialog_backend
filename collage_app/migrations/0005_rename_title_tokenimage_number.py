# Generated by Django 3.2.5 on 2021-07-20 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collage_app', '0004_rename_number_tokenimage_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tokenimage',
            old_name='title',
            new_name='number',
        ),
    ]

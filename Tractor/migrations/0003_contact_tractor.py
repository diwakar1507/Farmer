# Generated by Django 4.1.3 on 2022-11-20 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tractor', '0002_rename_comment_contact_details_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='tractor',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
# Generated by Django 4.2.7 on 2023-12-02 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_main_dirchairs_main_gamechairs_main_officechairs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_officechairs',
            name='image_right',
            field=models.ImageField(blank=True, null=True, upload_to='images/content/main/officeChairs/right'),
        ),
        migrations.AlterField(
            model_name='main_officechairs',
            name='image_left',
            field=models.ImageField(blank=True, null=True, upload_to='images/content/main/officeChairs/left'),
        ),
    ]
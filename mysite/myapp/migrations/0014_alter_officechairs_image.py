# Generated by Django 4.2.7 on 2023-11-25 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_officechairs_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officechairs',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/content/products/chairs/officeChairs/preview/'),
        ),
    ]

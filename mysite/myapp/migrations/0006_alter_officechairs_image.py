# Generated by Django 4.2.7 on 2023-11-20 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_officechairs_image_alter_gamechairs_description1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officechairs',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/content/products/chairs/office-chairs/previews'),
        ),
    ]
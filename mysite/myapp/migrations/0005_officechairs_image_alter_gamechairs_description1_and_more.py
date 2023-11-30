# Generated by Django 4.2.7 on 2023-11-20 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_delete_chairs_alter_gamechairs_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='officechairs',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/content/products/chairs/office-chairs/'),
        ),
        migrations.AlterField(
            model_name='gamechairs',
            name='description1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='gamechairs',
            name='description2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='officechairs',
            name='description1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='officechairs',
            name='description2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ortchairs',
            name='description1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ortchairs',
            name='description2',
            field=models.CharField(max_length=50),
        ),
    ]

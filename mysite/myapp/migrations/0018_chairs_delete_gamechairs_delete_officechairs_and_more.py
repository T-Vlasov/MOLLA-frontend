# Generated by Django 4.2.7 on 2024-07-15 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_main_officechairs_image_right_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chairs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('description1', models.CharField(max_length=50)),
                ('description2', models.CharField(max_length=50)),
                ('group', models.CharField(choices=[('ort', 'ортопедическое'), ('office', 'офисное'), ('game', 'игровое')], max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/content/products/chairs/officeChairs/preview/')),
            ],
        ),
        migrations.DeleteModel(
            name='GameChairs',
        ),
        migrations.DeleteModel(
            name='OfficeChairs',
        ),
        migrations.DeleteModel(
            name='OrtChairs',
        ),
    ]

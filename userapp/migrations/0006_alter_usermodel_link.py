# Generated by Django 4.2.5 on 2023-10-11 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_usermodel_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='link',
            field=models.URLField(blank=True, default='Link Bulunamadı', null=True, verbose_name='Linkler'),
        ),
    ]

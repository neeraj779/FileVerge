# Generated by Django 4.1.7 on 2023-04-01 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FileVerge', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='file',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-30 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('up_data', '0003_alter_mydata_myid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydata',
            name='description',
            field=models.CharField(max_length=50),
        ),
    ]

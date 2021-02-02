# Generated by Django 3.1.4 on 2021-01-25 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20210125_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutdata',
            name='github',
            field=models.CharField(default='https://github.com/JorgeVidalCano', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aboutdata',
            name='email',
            field=models.EmailField(max_length=35),
        ),
    ]
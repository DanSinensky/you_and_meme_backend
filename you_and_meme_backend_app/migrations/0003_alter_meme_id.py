# Generated by Django 4.2.4 on 2023-08-31 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('you_and_meme_backend_app', '0002_meme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

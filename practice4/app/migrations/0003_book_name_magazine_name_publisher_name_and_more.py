# Generated by Django 5.0.2 on 2024-02-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_book_title_remove_magazine_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.CharField(default='default', max_length=20),
        ),
        migrations.AddField(
            model_name='magazine',
            name='name',
            field=models.CharField(default='default', max_length=20),
        ),
        migrations.AddField(
            model_name='publisher',
            name='name',
            field=models.CharField(default='default', max_length=20),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(default='default', max_length=20),
        ),
    ]
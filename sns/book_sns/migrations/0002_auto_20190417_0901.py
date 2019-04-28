# Generated by Django 2.1.7 on 2019-04-17 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_sns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Not_Yet_Read_Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('days', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('response', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='already_book',
            name='good',
            field=models.IntegerField(default=0),
        ),
    ]
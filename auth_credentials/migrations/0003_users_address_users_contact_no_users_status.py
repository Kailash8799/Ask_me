# Generated by Django 4.1.4 on 2023-02-19 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_credentials', '0002_users_gender_users_user_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='address',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='users',
            name='contact_no',
            field=models.CharField(default='', max_length=13),
        ),
        migrations.AddField(
            model_name='users',
            name='status',
            field=models.CharField(default='Active', max_length=20),
        ),
    ]

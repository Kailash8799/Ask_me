# Generated by Django 4.1.4 on 2023-02-19 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_ans', '0002_question_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='total_ans',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='total_views',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 4.1.4 on 2023-02-20 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_ans', '0004_tags_contact_alter_question_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.CharField(default='Programming', max_length=500),
        ),
    ]

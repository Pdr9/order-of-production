# Generated by Django 4.1.7 on 2023-04-09 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_pessoa_approval_date_pessoa_date_payment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='article',
            field=models.CharField(default='', max_length=50),
        ),
    ]

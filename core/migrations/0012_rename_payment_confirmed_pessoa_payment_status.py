# Generated by Django 4.2 on 2023-04-12 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_pessoa_payment_confirmed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='payment_confirmed',
            new_name='payment_status',
        ),
    ]

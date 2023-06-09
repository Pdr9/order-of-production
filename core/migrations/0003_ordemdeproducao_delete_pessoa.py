# Generated by Django 4.1.7 on 2023-04-08 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pessoa_numero'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdemdeProducao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('op', models.IntegerField()),
                ('article', models.CharField(max_length=5)),
                ('nf_fornecida', models.IntegerField()),
                ('nf_ret', models.IntegerField()),
                ('nf_ind', models.IntegerField()),
                ('total_received', models.IntegerField()),
                ('first_quality', models.IntegerField()),
                ('second_quality', models.IntegerField()),
                ('third_quality', models.IntegerField()),
                ('timemoney', models.DecimalField(decimal_places=2, max_digits=10)),
                ('value_pieces', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_confirmed', models.BooleanField(default=False)),
                ('date_shipment', models.DateField()),
                ('approval_date', models.DateField()),
                ('preview_payment', models.DateField()),
                ('date_payment', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='pessoa',
        ),
    ]

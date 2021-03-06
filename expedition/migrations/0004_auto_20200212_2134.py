# Generated by Django 3.0.3 on 2020-02-12 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expedition', '0003_auto_20200211_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='seferler',
            name='musteri_adress',
            field=models.CharField(max_length=100, null=True, verbose_name='Müşterinin Adresi'),
        ),
        migrations.AlterField(
            model_name='seferler',
            name='firma',
            field=models.CharField(max_length=100, null=True, verbose_name='Firma Adı'),
        ),
        migrations.AlterField(
            model_name='seferler',
            name='musteri',
            field=models.CharField(max_length=100, verbose_name='Müşteri Adı'),
        ),
    ]

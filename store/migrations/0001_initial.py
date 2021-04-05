# Generated by Django 3.1.7 on 2021-04-05 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('slug', models.CharField(max_length=150, unique=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store.category')),
            ],
        ),
    ]
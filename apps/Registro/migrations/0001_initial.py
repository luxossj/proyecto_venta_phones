# Generated by Django 3.2.3 on 2021-06-21 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(choices=[('black', 'black'), ('red', 'red'), ('white', 'white')], default='black', max_length=20)),
                ('cantidad', models.CharField(choices=[('64', '64GB'), ('128', '128GB')], default='64', max_length=5)),
            ],
        ),
    ]

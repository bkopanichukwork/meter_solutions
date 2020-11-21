# Generated by Django 3.1.3 on 2020-11-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Включен'), (2, 'Выключен'), (3, 'Неизвестно')], default=3)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('device_connection_id', models.CharField(max_length=255)),
            ],
        ),
    ]

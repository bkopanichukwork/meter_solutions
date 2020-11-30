# Generated by Django 3.1.3 on 2020-11-26 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement', models.CharField(max_length=64)),
                ('designation', models.CharField(max_length=5)),
            ],
        ),
        migrations.RenameField(
            model_name='device',
            old_name='device_connection_id',
            new_name='mqtt_id',
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=127)),
                ('main_indication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meter.indication')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_switchable', models.BooleanField(default=True)),
                ('indications', models.ManyToManyField(to='meter.Indication')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meter.devicetype')),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now=True)),
                ('value', models.DecimalField(decimal_places=4, max_digits=16)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meter.device')),
                ('indication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meter.indication')),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='device_model',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meter.devicemodel'),
            preserve_default=False,
        ),
    ]
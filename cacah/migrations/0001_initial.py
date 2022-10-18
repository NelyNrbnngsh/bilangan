# Generated by Django 4.1.1 on 2022-10-06 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dosen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nip', models.CharField(max_length=200)),
                ('nama', models.CharField(max_length=200)),
                ('tanggal_lahir', models.CharField(max_length=200)),
                ('foto', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('fakultas', models.CharField(max_length=200)),
                ('prodi', models.CharField(max_length=200)),
                ('alamat', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.CharField(max_length=200)),
                ('nama', models.CharField(max_length=200)),
                ('tanggal_lahir', models.CharField(max_length=200)),
                ('foto', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('fakultas', models.CharField(max_length=200)),
                ('prodi', models.CharField(max_length=200)),
                ('alamat', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Staf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nip', models.CharField(max_length=200)),
                ('nama', models.CharField(max_length=200)),
                ('tanggal_lahir', models.CharField(max_length=200)),
                ('foto', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('unit', models.CharField(max_length=200)),
                ('alamat', models.TextField()),
            ],
        ),
    ]

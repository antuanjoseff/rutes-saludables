# Generated by Django 5.1.1 on 2024-10-08 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True, null=True)),
                ('style', models.CharField(choices=[('rock', 'Rock'), ('funk', 'Funk'), ('jazz', 'Jazz')], max_length=100)),
                ('agent', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rutes.band')),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rutes.band')),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('specialty', models.CharField(choices=[('vocal', 'Vocal'), ('guitar', 'Guitar'), ('bass', 'Bass'), ('drums', 'Drums')], max_length=100)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rutes.band')),
            ],
        ),
        migrations.RemoveField(
            model_name='trail',
            name='campus',
        ),
        migrations.DeleteModel(
            name='InterestPoint',
        ),
        migrations.AlterUniqueTogether(
            name='point',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='point',
            name='trail',
        ),
        migrations.RemoveField(
            model_name='trail',
            name='type',
        ),
        migrations.AddField(
            model_name='album',
            name='band',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rutes.band'),
        ),
        migrations.DeleteModel(
            name='Campus',
        ),
        migrations.DeleteModel(
            name='Point',
        ),
        migrations.DeleteModel(
            name='Trail',
        ),
        migrations.DeleteModel(
            name='TrailType',
        ),
    ]

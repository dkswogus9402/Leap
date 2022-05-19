# Generated by Django 3.2.12 on 2022-05-18 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CEO', models.CharField(max_length=100)),
                ('site', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('content', models.TextField()),
                ('training_period', models.DateTimeField()),
                ('teacher', models.CharField(max_length=45)),
                ('teacher_info', models.TextField()),
                ('location', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academys.category')),
            ],
        ),
    ]

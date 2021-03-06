# Generated by Django 3.2.6 on 2022-05-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academys', '0002_initial'),
        ('companys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('edu_certification', models.ManyToManyField(related_name='certification_edu', to='academys.Education')),
                ('posting_certification', models.ManyToManyField(related_name='certification_posting', to='companys.JobPosting')),
            ],
        ),
    ]

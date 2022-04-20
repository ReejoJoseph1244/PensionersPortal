# Generated by Django 4.0.3 on 2022-03-22 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0003_nsap_deatils_delete_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='CENSUS_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Total_Males', models.IntegerField()),
                ('Total_Females', models.IntegerField()),
                ('Rural_Males', models.IntegerField()),
                ('Rural_Females', models.IntegerField()),
                ('Urban_Males', models.IntegerField()),
                ('Urban_Females', models.IntegerField()),
            ],
        ),
    ]
# Generated by Django 4.2.1 on 2023-05-24 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('part_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('manufacturer', models.CharField(max_length=100)),
                ('Landfill_Waste_Saved', models.IntegerField(default=0)),
                ('Energy_Saved', models.IntegerField(default=0)),
                ('New_Parts_Carbon_Footprint', models.IntegerField(default=0)),
                ('Recycled_Parts_Carbon_Footprint', models.IntegerField(default=0)),
                ('Energy_Consumption_New_Parts', models.IntegerField(default=0)),
                ('Renewable_Material_Content', models.FloatField(default=0)),
                ('Carbon_Footprint_Saved', models.IntegerField(default=0)),
                ('Energy_Consumption_Saved', models.IntegerField(default=0)),
                ('Remanufacturing_Potential', models.FloatField(default=0)),
                ('is_Sold', models.BooleanField(default=False)),
                ('Percentage_recycled', models.FloatField(default=0.0)),
            ],
        ),
    ]

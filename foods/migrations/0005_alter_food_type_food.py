# Generated by Django 3.2.3 on 2021-10-24 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_alter_food_type_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='type_food',
            field=models.CharField(choices=[('breakfast', 'صبحانه'), ('drinks', 'نوشیدنی'), ('dinner', 'شام'), ('lunch', 'ناهار')], default='drinks', max_length=10, verbose_name='نوع غذا'),
        ),
    ]

# Generated by Django 2.1 on 2019-01-06 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_problem', models.CharField(max_length=20)),
                ('order_algorithm', models.CharField(max_length=20)),
                ('order_group', models.CharField(max_length=20)),
                ('order_teacher', models.CharField(max_length=20)),
                ('order_student', models.CharField(max_length=20)),
                ('order_person', models.CharField(max_length=20)),
            ],
        ),
    ]

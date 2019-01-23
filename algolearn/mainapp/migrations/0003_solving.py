# Generated by Django 2.1 on 2019-01-06 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solving',
            fields=[
                ('so_id', models.AutoField(primary_key=True, serialize=False)),
                ('so_res', models.IntegerField(default=-1)),
                ('so_todaydate', models.DateTimeField()),
                ('so_problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Problem')),
                ('so_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Student')),
            ],
        ),
    ]
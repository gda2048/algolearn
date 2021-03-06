# Generated by Django 2.1 on 2019-01-16 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('al_id', models.AutoField(primary_key=True, serialize=False)),
                ('al_type', models.CharField(max_length=20)),
                ('al_name', models.CharField(max_length=20)),
                ('al_comment', models.CharField(max_length=200, null=True)),
                ('al_theory', models.URLField(null=True)),
                ('al_visualization', models.URLField(null=True)),
            ],
            options={
                'ordering': ['al_name'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('gr_id', models.AutoField(primary_key=True, serialize=False)),
                ('gr_name', models.CharField(max_length=20)),
            ],
        ),
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
        migrations.CreateModel(
            name='Person',
            fields=[
                ('pe_id', models.AutoField(primary_key=True, serialize=False)),
                ('pe_login', models.CharField(max_length=20)),
                ('pe_name', models.CharField(max_length=20)),
                ('pe_surname', models.CharField(max_length=20)),
                ('pe_patronymic', models.CharField(max_length=20, null=True)),
                ('pe_email', models.EmailField(max_length=254)),
                ('pe_birthdate', models.DateTimeField()),
                ('pe_todaydate', models.DateTimeField()),
                ('pe_status', models.CharField(choices=[('s', 'Студент'), ('t', 'Преподаватель')], default='s', help_text='your status', max_length=20)),
                ('pe_admin', models.BooleanField(default=False, null=True)),
                ('pe_password', models.CharField(max_length=20)),
                ('pe_query', models.TextField(default='')),
            ],
            options={
                'ordering': ['pe_name'],
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('pr_id', models.AutoField(primary_key=True, serialize=False)),
                ('pr_name', models.CharField(max_length=20)),
                ('pr_checkdate', models.DateTimeField()),
                ('pr_algo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='algo_learn.Algorithm')),
                ('pr_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='algo_learn.Group')),
            ],
            options={
                'ordering': ['pr_name'],
            },
        ),
        migrations.CreateModel(
            name='Solving',
            fields=[
                ('so_id', models.AutoField(primary_key=True, serialize=False)),
                ('so_res', models.IntegerField(default=-1)),
                ('so_todaydate', models.DateTimeField()),
                ('so_problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='algo_learn.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('st_id', models.AutoField(primary_key=True, serialize=False)),
                ('st_rate', models.IntegerField(default=0)),
                ('st_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='algo_learn.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('te_id', models.AutoField(primary_key=True, serialize=False)),
                ('te_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='algo_learn.Person')),
            ],
        ),
        migrations.AddField(
            model_name='solving',
            name='so_student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='algo_learn.Student'),
        ),
        migrations.AddField(
            model_name='group',
            name='gr_students',
            field=models.ManyToManyField(to='algo_learn.Student'),
        ),
        migrations.AddField(
            model_name='group',
            name='gr_teachers',
            field=models.ManyToManyField(to='algo_learn.Teacher'),
        ),
    ]

# Generated by Django 3.0.5 on 2020-05-08 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('Garcon', 'Garcon'), ('Fille', 'Fille')], max_length=10)),
                ('birthday', models.DateField(blank=True, verbose_name='birthday Date(mm/dd/yy)')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_register.Level')),
            ],
        ),
    ]

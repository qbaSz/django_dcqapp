# Generated by Django 2.0.7 on 2019-02-18 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DCAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50)),
                ('dc_value', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DCEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commit_id', models.CharField(max_length=50)),
                ('change_id', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('author_name', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(verbose_name='date pushed')),
                ('verified', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='dcauthor',
            name='dc_entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcqapp.DCEntry'),
        ),
    ]
# Generated by Django 3.2.4 on 2021-11-22 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Username')),
                ('password', models.CharField(db_index=True, max_length=500, verbose_name='Password')),
                ('email', models.EmailField(db_index=True, max_length=254, verbose_name='Email')),
                ('token', models.CharField(blank=True, db_index=True, max_length=500, null=True, verbose_name='Token')),
                ('token_expires_at', models.DateTimeField(blank=True, null=True, verbose_name='Token Expires At')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified At')),
            ],
            options={
                'db_table': 'userdb',
            },
        ),
    ]

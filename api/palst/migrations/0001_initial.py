# Generated by Django 3.1.2 on 2021-08-05 08:48

from django.db import migrations, models
import palst.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveSmallIntegerField()),
                ('open', models.DecimalField(decimal_places=10, max_digits=20)),
                ('close', models.DecimalField(decimal_places=10, max_digits=20)),
                ('high', models.DecimalField(decimal_places=10, max_digits=20)),
                ('low', models.DecimalField(decimal_places=10, max_digits=20)),
                ('volume', models.DecimalField(decimal_places=10, max_digits=20)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100, verbose_name='Content')),
                ('completed', models.BooleanField(default=False)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='mUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('auth0_id', models.CharField(max_length=255, unique=True, verbose_name='Auth0Id')),
                ('auth0_name', models.CharField(max_length=255, verbose_name='Auth0Name')),
                ('username', models.CharField(blank=True, max_length=70, null=True, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=70, unique=True, verbose_name='Email')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('deleted', models.BooleanField(default=False, help_text='Designates whether the user was deleted or not', verbose_name='Delete Flag')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='Staff Status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='Active Flag')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', palst.models.UserManager()),
            ],
        ),
    ]
# Generated by Django 4.1.7 on 2023-04-30 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_categry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
        migrations.AlterField(
            model_name='post',
            name='categry',
            field=models.CharField(choices=[('programming', 'programming'), ('Ethical Hacking', 'Ethical Hacking'), ('Marketing', 'Marketing'), ('Another', 'Another')], default='Another', max_length=50, null=True),
        ),
    ]

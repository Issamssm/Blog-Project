# Generated by Django 4.1.7 on 2023-04-29 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_options_post_categry'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default_post.jpg', upload_to='post_pics'),
        ),
    ]

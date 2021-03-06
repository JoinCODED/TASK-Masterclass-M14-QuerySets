# Generated by Django 4.0.5 on 2022-06-29 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_album_created_at_album_modified_at_song_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='albums.album'),
            preserve_default=False,
        ),
    ]

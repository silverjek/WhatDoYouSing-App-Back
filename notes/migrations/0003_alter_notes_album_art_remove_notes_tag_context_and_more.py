# Generated by Django 4.2.17 on 2025-02-21 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_notes_emotion_alter_notes_location_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='album_art',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.RemoveField(
            model_name='notes',
            name='tag_context',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='tag_season',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='tag_time',
        ),
        migrations.AlterField(
            model_name='plinotes',
            name='plis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plinotes', to='notes.plis'),
        ),
        migrations.RemoveField(
            model_name='plis',
            name='tag_context',
        ),
        migrations.RemoveField(
            model_name='plis',
            name='tag_season',
        ),
        migrations.RemoveField(
            model_name='plis',
            name='tag_time',
        ),
        migrations.AddField(
            model_name='notes',
            name='tag_context',
            field=models.ManyToManyField(blank=True, null=True, related_name='tag_context', to='notes.contexts'),
        ),
        migrations.AddField(
            model_name='notes',
            name='tag_season',
            field=models.ManyToManyField(blank=True, null=True, related_name='tag_season', to='notes.seasons'),
        ),
        migrations.AddField(
            model_name='notes',
            name='tag_time',
            field=models.ManyToManyField(blank=True, null=True, related_name='tag_time', to='notes.times'),
        ),
        migrations.AddField(
            model_name='plis',
            name='tag_context',
            field=models.ManyToManyField(blank=True, null=True, related_name='pli_tag_context', to='notes.contexts'),
        ),
        migrations.AddField(
            model_name='plis',
            name='tag_season',
            field=models.ManyToManyField(blank=True, null=True, related_name='pli_tag_season', to='notes.seasons'),
        ),
        migrations.AddField(
            model_name='plis',
            name='tag_time',
            field=models.ManyToManyField(blank=True, null=True, related_name='pli_tag_time', to='notes.times'),
        ),
    ]

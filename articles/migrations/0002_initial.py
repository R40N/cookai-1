# Generated by Django 4.2.2 on 2023-06-22 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("taggit", "0005_auto_20220424_2025"),
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="like",
            field=models.ManyToManyField(
                blank=True, related_name="like_comments", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="bookmark",
            field=models.ManyToManyField(
                blank=True, related_name="bookmarks", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="articles.category"
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="like",
            field=models.ManyToManyField(
                blank=True, related_name="likes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]

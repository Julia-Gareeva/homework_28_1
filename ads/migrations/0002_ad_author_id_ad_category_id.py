# Generated by Django 4.1.3 on 2022-11-29 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
        ("ads", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ad",
            name="author_id",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="users.user"
            ),
        ),
        migrations.AddField(
            model_name="ad",
            name="category_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="ads.category",
            ),
        ),
    ]

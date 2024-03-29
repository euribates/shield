# Generated by Django 4.2.1 on 2023-05-16 11:11

from django.db import migrations, models
import django.db.models.deletion
import metahumans.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Identity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=130)),
                ("last_name", models.CharField(blank=True, max_length=270)),
            ],
        ),
        migrations.CreateModel(
            name="Power",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=80, unique=True)),
                ("description", models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("headquarter", models.CharField(blank=True, max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name="Metahuman",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100, unique=True)),
                (
                    "level",
                    models.PositiveIntegerField(
                        default=1, validators=[metahumans.models.up_to_one_hundred]
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="metahumans"),
                ),
                (
                    "identity",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="alter_ego",
                        to="metahumans.identity",
                    ),
                ),
                ("powers", models.ManyToManyField(to="metahumans.power")),
                (
                    "team",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="components",
                        to="metahumans.team",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-19 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BrandName",
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
                ("brand_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="StoreName",
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
                ("store_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Wish",
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
                ("item", models.CharField(max_length=200)),
                ("picture", models.URLField(blank=True, null=True)),
                ("link", models.URLField(blank=True, null=True)),
                ("color", models.CharField(blank=True, max_length=100, null=True)),
                ("style", models.CharField(blank=True, max_length=100, null=True)),
                ("size", models.CharField(blank=True, max_length=100, null=True)),
                ("notes", models.TextField(blank=True, max_length=100, null=True)),
                ("bought", models.BooleanField()),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="wish",
                        to="gifti.brandname",
                    ),
                ),
                (
                    "store",
                    models.ManyToManyField(related_name="wish", to="gifti.storename"),
                ),
            ],
        ),
    ]
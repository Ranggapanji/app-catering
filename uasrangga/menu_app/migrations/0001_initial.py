# Generated by Django 4.1.2 on 2022-11-01 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Jenis",
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
                ("jenis", models.CharField(max_length=30)),
                ("macamnya", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Menu",
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
                ("no", models.IntegerField(null=True)),
                ("paket", models.CharField(max_length=40)),
                ("harga", models.IntegerField(null=True)),
                ("gambar", models.CharField(max_length=50, null=True)),
                ("pilihanmenu", models.TextField()),
                (
                    "jenis_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="menu_app.jenis",
                    ),
                ),
            ],
        ),
    ]

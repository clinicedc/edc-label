# Generated by Django 4.2.7 on 2023-12-03 00:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_label", "0003_alter_zpllabeltemplates_device_created_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="zpllabeltemplates",
            options={
                "default_manager_name": "objects",
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Label template",
                "verbose_name_plural": "Label templates",
            },
        ),
        migrations.AddField(
            model_name="zpllabeltemplates",
            name="locale_created",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale created",
            ),
        ),
        migrations.AddField(
            model_name="zpllabeltemplates",
            name="locale_modified",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale modified",
            ),
        ),
        migrations.AddIndex(
            model_name="zpllabeltemplates",
            index=models.Index(
                fields=["-modified", "-created"], name="edc_label_z_modifie_79a6b3_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="zpllabeltemplates",
            index=models.Index(
                fields=["user_modified", "user_created"],
                name="edc_label_z_user_mo_9865fd_idx",
            ),
        ),
    ]

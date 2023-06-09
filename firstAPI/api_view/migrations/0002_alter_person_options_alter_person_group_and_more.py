# Generated by Django 4.2.1 on 2023-06-09 10:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api_view', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='person',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_view.group'),
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='ID único para la entidad Person', primary_key=True, serialize=False),
        ),
    ]

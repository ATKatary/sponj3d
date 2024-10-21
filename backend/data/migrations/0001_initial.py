# Generated by Django 5.1.2 on 2024-10-21 02:34

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('src', models.TextField()),
                ('type', models.CharField(choices=[('img', 'image'), ('txt', 'text'), ('mes', 'mesh')], max_length=26)),
                ('title', models.CharField(default='Unnamed Playground', max_length=26)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('position', models.JSONField()),
                ('type', models.CharField(choices=[('img', 'image'), ('txt', 'text'), ('mes', 'mesh'), ('remesh', 're-mesh'), ('sketch', 'sketch'), ('segment', 'segment'), ('texture', 'texture'), ('playground', 'playground'), ('generatedImg', 'generated image')], max_length=26)),
                ('status', models.CharField(choices=[('done', 'done'), ('ready', 'ready'), ('error', 'error'), ('static', 'static'), ('running', 'running'), ('pending', 'pending')], default='ready', max_length=26)),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.data')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sourceHandle', models.CharField(max_length=26)),
                ('targetHandle', models.CharField(max_length=26)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='data.node')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target', to='data.node')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

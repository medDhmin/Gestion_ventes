# Generated by Django 4.2.4 on 2023-08-08 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=50, unique=True)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('date_naiss', models.DateField()),
                ('lieu_naiss', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Etablissement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_etablissement', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materiel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('type', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=200)),
                ('marque', models.CharField(max_length=100)),
                ('caracteristique', models.TextField()),
                ('etat', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Emplacement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=200)),
                ('id_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee')),
                ('id_etablissement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.etablissement')),
            ],
        ),
        migrations.CreateModel(
            name='Affectation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('id_emplacement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.emplacement')),
                ('id_materiel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.materiel')),
            ],
        ),
    ]

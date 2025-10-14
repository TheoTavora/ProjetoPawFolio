# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agendamento(models.Model):
    id_agendamento = models.AutoField(primary_key=True)
    id_petshop_agendamento = models.ForeignKey('Petshop', models.DO_NOTHING, db_column='id_petshop_agendamento', blank=True, null=True)
    data_agendamento = models.DateField()

    class Meta:
        managed = False
        db_table = 'agendamento'


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    senha = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cliente'


class Pet(models.Model):
    id_dono = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_dono', blank=True, null=True)
    nome = models.CharField(max_length=100)
    comportamento = models.CharField(max_length=100, blank=True, null=True)
    raca = models.CharField(max_length=100, blank=True, null=True)
    diferencial = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pet'


class Petshop(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'petshop'


class Servicos(models.Model):
    pshop_related = models.ForeignKey(Petshop, models.DO_NOTHING, db_column='pshop_related', blank=True, null=True)
    descricao = models.CharField(max_length=100)
    preco = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'servicos'

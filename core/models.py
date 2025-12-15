from django.db import models


# Create your models here.

class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True
    )
    created = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        null=True
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified',
        auto_now=True,
        null=True
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True
    )

    class Meta:
        abstract = True
        managed = True


class Product(ModelBase):
    description = models.TextField(
        db_column='description',
        null=False
    )

    quantity = models.IntegerField(
        db_column='quantity',
        null=False,
        default=0
    )

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'product'


class Client(ModelBase):
    name = models.CharField(
        db_column='description',
        max_length=70,
        null=False
    )

    age = models.IntegerField(
        db_column='age',
        null=False
    )

    rg = models.CharField(
        db_column='rg',
        max_length=12,
        null=False
    )

    cpf = models.CharField(
        db_column='cpf',
        max_length=12,
        null=False
    )

    def __str__(self):
        return '{} - {}'.format(self.cpf, self.name)

    class Meta:
        db_table = 'client'


class Employee(ModelBase):
    name = models.CharField(
        db_column='name',
        max_length=70,
        null=False
    )

    registration = models.CharField(
        db_column='registration',
        max_length=15,
        null=False,
        default=0
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employee'


class Sale(ModelBase):
    product = models.ForeignKey(
        Product,
        db_column='id_product',
        null=False,
        on_delete=models.DO_NOTHING
    )

    client = models.ForeignKey(
        Client,
        db_column='id_client',
        null=False,
        on_delete=models.DO_NOTHING
    )

    employee = models.ForeignKey(
        Employee,
        db_column='id_employee',
        null=False,
        on_delete=models.DO_NOTHING
    )

    nrf = models.CharField(
        db_column='nrf',
        max_length=255,
        null=False
    )

    class Meta:
        db_table = 'sale'

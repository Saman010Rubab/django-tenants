from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
# Create your models here.


class Client(TenantMixin):
    name = models.CharField( max_length=150, unique=True)
    email = models.EmailField(max_length=254, null=True, unique=True)
    password = models.CharField( max_length=10, null=True)
    created_on = models.DateField( auto_now_add=True)

class Domain(DomainMixin):
    pass
from django.db import models

class Company(models.Model):
    odoo_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class User(models.Model):
    odoo_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField()
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    default_company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=True, related_name='default_users'
    )
    companies = models.ManyToManyField(Company, through='UserCompanyAccess')

    def __str__(self):
        return self.username


class UserCompanyAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_default = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'company')

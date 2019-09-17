from django.db import models


# Create your models here.

class Good(models.Model):
    name = models.CharField(max_length=255, unique=True)
    status = models.IntegerField(default=0)

    class Meta:
        # model 级别的权限控制，增删改查
        default_permissions = ('add', 'change', 'delete', 'view_good')
        permissions = (
            ("deploy_good", "can deploy good"),
        )

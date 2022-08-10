from django.db import models

# Create your models here.
class Product(models.Model):  
        id      = models.IntegerField(primary_key = True)
        pname  = models.CharField(max_length=100,null=True,blank=True, default=False)
        pdesc=models.TextField()
        pcat_id=models.IntegerField()
        pimages=models.TextField()
        


        


        class Meta:
                  db_table = "products"
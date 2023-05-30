from django.db import models

class Product(models.Model):
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=200)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return  self.product_name

class Order(models.Model):
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=200)
    pub_date=models.DateField()

    def __str__(self):
        return  self.product_name
  
class Feedback(models.Model):
    name=models.CharField(max_length=100)
    feedback=models.CharField(max_length=1000)
    date=models.CharField(max_length=50)
    
    def __str__(self):
        if self.name:
            return  self.name 
        else:
            return 'blank'
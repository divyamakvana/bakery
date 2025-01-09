from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField( max_length=250)
    email = models.CharField( max_length=250)
    phone = models.CharField(max_length=14 )
    content = models.TextField()
    timestamp = models.DateTimeField( auto_now_add=True, blank=True)


    def __str__(self):
        return " Message from  " + self.name 
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    product_category = models.CharField( max_length=250, default=0)
    product_price = models.IntegerField(default=0)
    description = models.CharField( max_length=350)
    used_by = models.DateField()
    image = models.ImageField(upload_to="home/images",default="")
   
    Net_Quantity = models.IntegerField(default=0)
    
    
def __str__(self):
    return self.product_name

class Order(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone = models.CharField( max_length=15, default="")

def __str__(self):
        return f"Order {self.order_id} by {self.name}"




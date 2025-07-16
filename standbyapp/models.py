from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images/')

    
    def __str__(self):
        return self.name


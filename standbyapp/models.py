from django.db import models

class Item(models.Model):
    serial_number = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.serial_number = self.serial_number.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name  # ✅ Indented correctly


class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="item_images/")

    def __str__(self):
        return f"Image for {self.item.name}"
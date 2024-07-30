from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank= False, )
    subtitle = models.CharField(max_length=100)
    description = models.TextField(blank= False, null= False)
    date = models.DateField(auto_created= False)
    image = models.ImageField(upload_to='item_image', blank=False, null=False)
    link = models.TextField(blank=False, null=False)

    class Meta:
        ordering = ('category',)

    def __str__(self):
        return self.name
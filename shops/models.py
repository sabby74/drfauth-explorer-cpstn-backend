from django.db import models

# Create your models here.


class Shops(models.Model):
    name = models.CharField(max_length=100, default=None)
    description = models.TextField(default=None)
    location = models.CharField(max_length=255, default=None)  
    sells = models.CharField(max_length=255, default=None)
    rating = models.FloatField(default=0.0)
    is_OpenSundays = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        'users.User', related_name='shops', on_delete=models.CASCADE,default=None)
      
    
    def __str__(self):
            return self.name
    
   
    


class Review(models.Model):
      title = models.CharField(max_length=100)
      shop = models.ForeignKey(Shops, on_delete=models.CASCADE,related_name='reviews')
      body = models.CharField(max_length=500)   
      owner = models.ForeignKey(
        'users.User', related_name='reviews', on_delete=models.CASCADE, default=None)

      def __str__(self):
            return self.title
      
      
      
      

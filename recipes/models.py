from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) #for me to explain this, if a user is deleted, it deletes all of their recipes that the user created.
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='recipe_pics') #This is for the images to show up on the homepage
    


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("recipe-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name #whatever I return in this function is what it will show up in the admin 
    
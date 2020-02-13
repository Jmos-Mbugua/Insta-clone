from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='profile/')
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followers", blank=True)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="following", blank=True)


    def __str__(self):
        return self.user.username

    def save_profile(self):
        '''
        This method saves the user profile
        '''
        return self.save()

class Location(models.Model):
    image_location = models.CharField(max_length=200)

    def __str__(self):
        return self.image_location

    def save_location(self):
        '''
        This method saves the post's location
        '''
        return self.save()

    

class Post(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')    
    caption = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location_posted = models.ForeignKey(Location, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('images')

    def save_image(self):
        '''
        This method saves the post
        '''
        return self.save()

    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()

    @classmethod
    def delete_image(cls, id):
        '''
        Method that deletes a post
        '''
        return cls.objects.filter(id = id).delete()




class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment

    def save_comment(self):
        '''
        This method saves the comment
        '''
        return self.save()




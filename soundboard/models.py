from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Genre(models.Model):
    """
    Model representing music genre
    """

    name = models.CharField(max_length=200, help_text="Enter music genre (e.g. Rock, Psychedelic, Trance, etc.")

    
    def __str__(self):
        return self.name

class Component(models.Model):
    """
    Model representing different components in a music
    """

    name = models.CharField(max_length=200, help_text="Enter music component (e.g. Guitar, Piano, Drums, Bass, etc.")

    def __str__(self):
        return self.name




class Contributor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    preferences = models.ManyToManyField(Genre)
    skills = models.ManyToManyField(Component)

@receiver(post_save, sender=User)
def create_contrib_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_contrib_profile(sender, instance, **kwargs):
    instance.profile.save()


class Sound(models.Model):
    title = models.CharField(max_length=500, default='DazedNConfused', unique=True, help_text="Enter title for music piece")
    created_by = models.ForeignKey(Contributor, on_delete = models.CASCADE, related_name="sounds")
    created_on = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="sounds")
    components = models.ManyToManyField(Component)
    contributors = models.ManyToManyField(Contributor)



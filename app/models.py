from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.db.models import ImageField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm
# Create your models here


class Personne(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    naissance = models.CharField(max_length=200,
                             blank=True,null=True,
                             default='(no title)')
    description = models.TextField(blank=True,
                                   null=True,
                                   default=None)
    tags = models.ManyToManyField("Tag", related_name="Personne", blank=False)

    def __str__(self):
        return '{} ({})'.format(self.user, ' / '.join([str(c) for c in self.tags.all()]))


class Example(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    image = ImageField(upload_to="gallery", height_field=None, width_field=None)

    def __str__(self):
        result = self.title
        return result


class UserForm(ModelForm):
    class RegisterForm(forms.Form):
        first_name = forms.CharField(label="First name",
                                     max_length=100)
        last_name = forms.CharField(label="Last name",
                                    max_length=100)
        password = forms.CharField(widget=forms.PasswordInput)
        password_2 = forms.CharField(widget=forms.PasswordInput)


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#
#
# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
#
#
# class SignUpForm(UserCreationForm):
#     birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
#
#     class Meta:
#         model = User
#         fields = ('username', 'birth_date', 'password1', 'password2', )
from typing import BinaryIO
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
   # 1. profile.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name="profile")
    profile_picture = CloudinaryField('image')
    bio= models.TextField()
    contact = models.CharField(max_length=60,blank=True)
    
    #profile  class methods
    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile

    @classmethod
    def update_profile(cls, id, profile_picture,bio):
        cls.objects.filter(id=id).update(profile_picture=profile_picture,bio=bio)    
    
   # 2. project.
class Project(models.Model):
    title = models.CharField(max_length=60,blank=True)
    image = CloudinaryField('image')
    description = models.TextField()
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    link = models.URLField(blank=True)
    profile = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)


     #project  class methods
    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()
    @classmethod
    def search_projects(cls, name):
        return cls.objects.filter(title__icontains=name).all()   
    @classmethod
    def project_by_id(cls,id):
        project = Project.objects.filter(id =id)
        return project

   # 3. Reviews/rating.
class Review(models.Model):
    ratings= (
        (1, 'very low'),(2, '2'),
        (3, '3'),(4, '4'),
        (5, 'Avarage'),(6, '6'),
        (7, '7'),(8, '8'),
        (9, '9'),(10, 'Exellent'),
    )
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    content = models.IntegerField(choices=ratings,blank=False,default=0)
    design = models.IntegerField(choices=ratings,default=0,blank=False)
    usability = models.IntegerField(choices=ratings,blank=False,default=0)
    project = models.ForeignKey(Project,null=True,on_delete=models.CASCADE)
    average =  models.DecimalField(default=1,blank=False,max_digits=30,decimal_places=2)
   
    def __str__(self):
        return self.user

    def save_review(self):
        self.save()

    def delete_review(self):
        self.delete()

class ProfileApi(models.Model):
    username = models.CharField(max_length=40)
    bio = models.TextField()
    projects=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    project= models.ForeignKey(Project,null=True,on_delete=models.CASCADE)
    profile_picture= CloudinaryField('image')
      
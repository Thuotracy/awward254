from rest_framework import serializers
from .models import Profile, Project  


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ( 'profile_picture','bio','contact','user')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ( 'user','title', 'image','link','description')

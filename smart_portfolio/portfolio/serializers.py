from rest_framework import serializers
from .models import AboutMe, Skill, TechStack, Project, Contact, Blog, ProjectImage  # noqa: F401


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name']

class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = ['name', 'headline', 'bio', 'profile_picture', 'skills']

class TechStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechStack
        fields = ['name']

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image', 'caption']

class ProjectSerializer(serializers.ModelSerializer):
    tech_stack = TechStackSerializer(many=True)
    tech_stack_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=TechStack.objects.all(), write_only=True, source='tech_stack'
    )
    images = ProjectImageSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['title', 'description', 'live_url', 'github_url', 'image', 'tech_stack']
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        

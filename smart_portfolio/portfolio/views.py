from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import (
    AboutMe,
    Skill,
    TechStack,
    Project,
    Contact,
    Blog,
    ProjectImage
)
from .serializers import (
    AboutMeSerializer,
    SkillSerializer,
    TechStackSerializer,
    ProjectSerializer,
    ContactSerializer,
    BlogSerializer,
    ProjectImageSerializer,
)

# ===== ABOUT ME =====
class AboutMeListCreateView(generics.ListCreateAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer


class AboutMeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer


# ===== CONTACT =====
class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# ===== PROJECT =====
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# ===== PROJECT IMAGE =====
class ProjectImageListCreateView(generics.ListCreateAPIView):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer


class ProjectImageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer


# ===== BLOG =====
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# ===== SKILL =====
class SkillListCreateView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


# ===== TECH STACK =====
class TechStackListCreateView(generics.ListCreateAPIView):
    queryset = TechStack.objects.all()
    serializer_class = TechStackSerializer


class TechStackRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TechStack.objects.all()
    serializer_class = TechStackSerializer

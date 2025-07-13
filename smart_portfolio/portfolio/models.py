from django.db import models
from django.utils.text import slugify
# Create your models here.

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    headline = models.CharField(max_length=150)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to="about/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class TechStack(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    live_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    tech_stack = models.ManyToManyField(TechStack, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    website = models.URLField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contact Info ({self.email})"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField(help_text="Supports markdown or rich text")
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey('Project', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.project.title}"
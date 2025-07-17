from django.db import models

class Greeting(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    resume_link = models.URLField(blank=True)
    display = models.BooleanField(default=True)

class SocialMediaLinks(models.Model):
    platform = models.CharField(max_length=50)
    url = models.URLField()
    display = models.BooleanField(default=True)

class Skill(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
    display = models.BooleanField(default=True)

class SkillDetail(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='details')
    description = models.CharField(max_length=300)

class SoftwareSkill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='software_skills')
    skill_name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100)  # e.g., "faHtml5"

class Education(models.Model):
    school_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='education/logos/')
    sub_header = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    display = models.BooleanField(default=True)

class EducationBullet(models.Model):
    education = models.ForeignKey(Education, on_delete=models.CASCADE, related_name='bullets')
    bullet = models.CharField(max_length=255)

class TechStack(models.Model):
    stack_name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=10)
    display = models.BooleanField(default=True)

class WorkExperience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to='work_experience/logos/')
    date = models.CharField(max_length=100)
    description = models.TextField()
    display = models.BooleanField(default=True)

class WorkDescBullet(models.Model):
    experience = models.ForeignKey(WorkExperience, on_delete=models.CASCADE, related_name='bullets')
    bullet = models.CharField(max_length=255)

class Project(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/images/')
    description = models.TextField()
    url = models.URLField()
    display = models.BooleanField(default=True)

class Achievement(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
    image = models.ImageField(upload_to='achievements/images/')
    image_alt = models.CharField(max_length=100)

class AchievementLink(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE, related_name='links')
    name = models.CharField(max_length=100)
    url = models.URLField()

class Blog(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField()
    display = models.BooleanField(default=True)

class Talk(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    slides_url = models.URLField()
    event_url = models.URLField()
    image_url = models.URLField(blank=True)

class Podcast(models.Model):
    url = models.URLField()
    display = models.BooleanField(default=True)

class Resume(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    display = models.BooleanField(default=True)

class ContactInfo(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
    phone = models.CharField(max_length=30)
    email = models.EmailField()

class TwitterDetails(models.Model):
    username = models.CharField(max_length=100)
    display = models.BooleanField(default=True)

class OpenSource(models.Model):
    show_github_profile = models.BooleanField(default=True)
    display = models.BooleanField(default=True)

class SplashScreen(models.Model):
    enabled = models.BooleanField(default=True)
    duration = models.PositiveIntegerField(default=2000)
    animation = models.FileField(upload_to='splash_animations/')


class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    headline = models.CharField(max_length=150)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to="about/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


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
        return f"Contact: {self.email}"
        
        

class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="project_images/")
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.project.title}"

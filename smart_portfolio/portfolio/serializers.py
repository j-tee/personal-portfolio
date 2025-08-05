from rest_framework import serializers
from .models import (
    Greeting,
    SocialMediaLinks,
    Skill,
    SkillDetail,
    SoftwareSkill,
    Education,
    EducationBullet,
    TechStack,
    WorkExperience,
    WorkDescBullet,
    Project,
    ProjectImage,
    Achievement,
    AchievementLink,
    Blog,
    Talk,
    Podcast,
    Resume,
    ContactInfo,
    TwitterDetails,
    OpenSource,
    SplashScreen,
    AboutMe,
    Contact,
)


class GreetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Greeting
        fields = "__all__"


class SocialMediaLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLinks
        fields = "__all__"


class SkillDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillDetail
        fields = "__all__"


class SoftwareSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftwareSkill
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    details = SkillDetailSerializer(many=True, read_only=True)
    software_skills = SoftwareSkillSerializer(many=True, read_only=True)

    class Meta:
        model = Skill
        fields = ["id", "title", "subtitle", "display", "details", "software_skills"]


class EducationBulletSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationBullet
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    bullets = EducationBulletSerializer(many=True, read_only=True)

    class Meta:
        model = Education
        fields = [
            "id",
            "school_name",
            "logo",
            "sub_header",
            "duration",
            "description",
            "display",
            "bullets",
        ]


class TechStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechStack
        fields = "__all__"


class WorkDescBulletSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkDescBullet
        fields = "__all__"


class WorkExperienceSerializer(serializers.ModelSerializer):
    bullets = WorkDescBulletSerializer(many=True, read_only=True)

    class Meta:
        model = WorkExperience
        fields = [
            "id",
            "role",
            "company",
            "company_logo",
            "date",
            "description",
            "display",
            "bullets",
        ]


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ["id", "image", "caption"]


class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "subtitle",
            "image",
            "description",
            "url",
            "display",
            "images",
        ]


class AchievementLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementLink
        fields = "__all__"


class AchievementSerializer(serializers.ModelSerializer):
    links = AchievementLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Achievement
        fields = ["id", "title", "subtitle", "image", "image_alt", "links"]


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        fields = "__all__"


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = "__all__"


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = "__all__"


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__"


class TwitterDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterDetails
        fields = "__all__"


class OpenSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenSource
        fields = "__all__"


class SplashScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SplashScreen
        fields = "__all__"


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

from django.urls import path
from .views import (
    AboutMeListCreateView,
    AboutMeRetrieveUpdateDestroyView,
    ContactListCreateView,
    ContactRetrieveUpdateDestroyView,
    ProjectListCreateView,
    ProjectRetrieveUpdateDestroyView,
    ProjectImageListCreateView,
    ProjectImageRetrieveUpdateDestroyView,
    BlogListCreateView,
    BlogRetrieveUpdateDestroyView,
    SkillListCreateView,
    SkillRetrieveUpdateDestroyView,
    TechStackListCreateView,
    TechStackRetrieveUpdateDestroyView,
    GreetingsListCreateView,
    GreetingsRetrieveUpdateDestroyView
)

urlpatterns = [
    # === AboutMe ===
    path("about/", AboutMeListCreateView.as_view(), name="aboutme-list-create"),
    path("about/<int:pk>/", AboutMeRetrieveUpdateDestroyView.as_view(), name="aboutme-detail"),

    # === Skill ===
    path("skills/", SkillListCreateView.as_view(), name="skill-list-create"),
    path("skills/<int:pk>/", SkillRetrieveUpdateDestroyView.as_view(), name="skill-detail"),

    # === TechStack ===
    path("techstacks/", TechStackListCreateView.as_view(), name="techstack-list-create"),
    path("techstacks/<int:pk>/", TechStackRetrieveUpdateDestroyView.as_view(), name="techstack-detail"),

    # === Projects ===
    path("projects/", ProjectListCreateView.as_view(), name="project-list-create"),
    path("projects/<int:pk>/", ProjectRetrieveUpdateDestroyView.as_view(), name="project-detail"),

    # === Project Images ===
    path("project-images/", ProjectImageListCreateView.as_view(), name="projectimage-list-create"),
    path("project-images/<int:pk>/", ProjectImageRetrieveUpdateDestroyView.as_view(), name="projectimage-detail"),

    # === Contact Info ===
    path("contact/", ContactListCreateView.as_view(), name="contact-list-create"),
    path("contact/<int:pk>/", ContactRetrieveUpdateDestroyView.as_view(), name="contact-detail"),

    # === Blog ===
    path("blogs/", BlogListCreateView.as_view(), name="blog-list-create"),
    path("blogs/<int:pk>/", BlogRetrieveUpdateDestroyView.as_view(), name="blog-detail"),

    # === Greetings ===
    path("greetings/", GreetingsListCreateView.as_view(), name="greetings-list-create"),
    path("greetings/<int:pk>/", GreetingsRetrieveUpdateDestroyView.as_view(), name="greetings-detail"),
]

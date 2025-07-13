from django.urls import path
from .views import (
    AboutMeListCreateView,
    AboutMeRetrieveUpdateDestroyView, ContactListCreateView,
		ContactRetrieveUpdateDestroyView, ProjectListCreateView,
		ProjectRetrieveUpdateDestroyView, BlogListCreateView,
		BlogRetrieveUpdateDestroyView, SkillListCreateView,
		SkillRetrieveUpdateDestroyView, TechStackListCreateView,
		TechStackRetrieveUpdateDestroyView
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

    # === Contact Info ===
    path("contact/", ContactListCreateView.as_view(), name="contact-list-create"),
    path("contact/<int:pk>/", ContactRetrieveUpdateDestroyView.as_view(), name="contact-detail"),

    # === Blog ===
    path("blogs/", BlogListCreateView.as_view(), name="blog-list-create"),
    path("blogs/<int:pk>/", BlogRetrieveUpdateDestroyView.as_view(), name="blog-detail"),
]

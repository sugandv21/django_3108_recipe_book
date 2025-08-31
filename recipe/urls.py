from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    home, RecipeListView, RecipeDetailView,
    recipe_create, recipe_edit, recipe_delete,
    register
)

urlpatterns = [
    path("", home, name="home"),

    path("recipes/", RecipeListView.as_view(), name="recipe_list"),
    path("recipe/<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("recipe/new/", recipe_create, name="recipe_create"),
    path("recipe/<int:pk>/edit/", recipe_edit, name="recipe_edit"),
    path("recipe/<int:pk>/delete/", recipe_delete, name="recipe_delete"),

    path(
        "accounts/login/",
        auth_views.LoginView.as_view(template_name="recipe/layout/login.html"),
        name="login"
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(template_name="recipe/layout/logged_out.html"),
        name="logout"
    ),
    path("register/", register, name="register"),
]

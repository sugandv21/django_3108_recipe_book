from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, DetailView
from .models import Recipe
from .forms import RecipeForm

def home(request):
    return render(request, "recipe/layout/home.html")

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe/layout/recipe_list.html"
    context_object_name = "recipes"
    paginate_by = 5

    def get_queryset(self):
        queryset = Recipe.objects.all().order_by("-created_at")
        query = self.request.GET.get("query")
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe/layout/recipe_detail.html"



@login_required
def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, "Recipe added successfully!")
            return redirect("recipe_list")
    else:
        form = RecipeForm()
    return render(request, "recipe/layout/recipe_form.html", {"form": form})


@login_required
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, author=request.user)
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, "Recipe updated successfully!")
            return redirect("recipe_detail", pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "recipe/layout/recipe_form.html", {"form": form})

@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, author=request.user)
    if request.method == "POST":
        recipe.delete()
        messages.success(request, "Recipe deleted successfully!")
        return redirect("recipe_list")
    return render(request, "recipe/layout/recipe_confirm_delete.html", {"recipe": recipe})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "recipe/layout/register.html", {"form": form})

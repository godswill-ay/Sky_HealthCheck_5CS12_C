from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from .models import Department, Team, CustomUser

User = get_user_model()


def home(request):
    return render(request, 'core/home.html')


@login_required
def department_list(request):
    query = request.GET.get('q')
    if query:
        departments = Department.objects.filter(name__icontains=query)
    else:
        departments = Department.objects.all()
    return render(request, 'core/department_list.html', {'departments': departments})


@login_required
def team_list(request):
    query = request.GET.get('q')
    if query:
        teams = Team.objects.filter(name__icontains=query)
    else:
        teams = Team.objects.all()
    return render(request, 'core/team_list.html', {'teams': teams})


@login_required
def user_list(request):
    query = request.GET.get('q')
    if query:
        users = CustomUser.objects.filter(username__icontains=query)
    else:
        users = CustomUser.objects.all()
    return render(request, 'core/user_list.html', {'users': users})


def about(request):
    return render(request, 'core/about.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        # optionally add a message here for invalid login
        return redirect('login')
    return render(request, 'core/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            # optional: set error message for mismatch
            return render(request, 'core/register.html', {'error': "Passwords do not match."})

        if User.objects.filter(username=username).exists():
            # optional: set error message for existing user
            return render(request, 'core/register.html', {'error': "Username already taken."})

        # Create and log in the new user
        user = User.objects.create_user(username=username, password=password1)
        login(request, user)
        return redirect('home')

    return render(request, 'core/register.html')


def logout_view(request):
    logout(request)
    return redirect('login')

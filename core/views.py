from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from .models import Department, Team, CustomUser, Session, Card, Vote
from .forms import VoteForm

User = get_user_model()


def home(request):
    return render(request, 'core/home.html')


@login_required
def department_list(request):
    query = request.GET.get('q')
    departments = Department.objects.filter(name__icontains=query) if query else Department.objects.all()
    return render(request, 'core/department_list.html', {'departments': departments})


@login_required
def team_list(request):
    query = request.GET.get('q')
    teams = Team.objects.filter(name__icontains=query) if query else Team.objects.all()
    return render(request, 'core/team_list.html', {'teams': teams})


@login_required
def user_list(request):
    query = request.GET.get('q')
    users = CustomUser.objects.filter(username__icontains=query) if query else CustomUser.objects.all()
    return render(request, 'core/user_list.html', {'users': users})


def about(request):
    return render(request, 'core/about.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, "Please enter both username and password.")
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials or account does not exist.")
            return redirect('login')

    return render(request, 'core/login.html')


def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name  = request.POST.get('last_name', '').strip()
        email      = request.POST.get('email', '').strip()
        username   = request.POST.get('username', '').strip()
        password1  = request.POST.get('password1', '')
        password2  = request.POST.get('password2', '')

        if not (first_name and last_name and email and username and password1 and password2):
            messages.error(request, "All fields are required.")
            return render(request, 'core/register.html')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'core/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "That username is already taken.")
            return render(request, 'core/register.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with that email already exists.")
            return render(request, 'core/register.html')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
        )

        user.first_name = first_name
        user.last_name  = last_name
        user.save()

        login(request, user)
        messages.success(request, "Your account has been created successfully!")
        return redirect('home')

    return render(request, 'core/register.html')


def logout_view(request):
    logout(request)
    messages.info(request, "You’ve been logged out.")
    return redirect('login')


@login_required
def cast_vote(request):
    user = request.user
    if request.method == 'POST':
        form = VoteForm(request.POST, user=user)
        if form.is_valid():
            session = form.cleaned_data['session']
            team = form.cleaned_data['team']
            for card in Card.objects.all():
                vote_value = request.POST.get(f'vote_{card.id}')
                progress_flag = request.POST.get(f'progress_{card.id}') == 'on'
                if vote_value:
                    Vote.objects.update_or_create(
                        user=user,
                        session=session,
                        card=card,
                        defaults={
                            'vote': vote_value,
                            'progress_better': progress_flag
                        }
                    )
            return redirect('complete')
        else:
            messages.error(request, "Please select both a session and a team before voting.")
    else:
        form = VoteForm(user=user)

    cards = Card.objects.all()
    return render(request, 'core/cast_vote.html', {'form': form, 'cards': cards})


@login_required
def vote_summary(request):
    user = request.user
    session_id = request.GET.get('session')
    sessions = Session.objects.all()
    votes = []
    if session_id:
        try:
            session = Session.objects.get(pk=int(session_id))
            votes = Vote.objects.filter(user=user, session=session)
        except (ValueError, Session.DoesNotExist):
            messages.error(request, "The selected session is invalid.")
    return render(request, 'core/vote_summary.html', {
        'sessions': sessions,
        'selected_session': session_id,
        'votes': votes
    })


@login_required
def complete(request):
    return render(request, 'core/complete.html')

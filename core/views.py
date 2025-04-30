from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from .models import Department, Team, CustomUser, Session, Card, Vote
from .forms import VoteForm

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
        #add a message here for invalid login - need to do zaamin
        return redirect('login')
    return render(request, 'core/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            #set error message for mismatch
            return render(request, 'core/register.html', {'error': "Passwords do not match."})

        if User.objects.filter(username=username).exists():
            # please set error message for existing user
            return render(request, 'core/register.html', {'error': "Username already taken."})

        user = User.objects.create_user(username=username, password=password1)
        login(request, user)
        return redirect('home')

    return render(request, 'core/register.html')


def logout_view(request):
    logout(request)
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
            return redirect('vote_summary')
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
        session = Session.objects.get(pk=session_id)
        votes = Vote.objects.filter(user=user, session=session)
    return render(request, 'core/vote_summary.html', {'sessions': sessions, 'selected_session': session_id, 'votes': votes})


from django import forms
from .models import Vote, Session, Card, Team
from django.contrib.auth import get_user_model
#zq
class VoteForm(forms.Form):
    session = forms.ModelChoiceField(
        queryset=Session.objects.all(),
        empty_label=None,
        label="Health Check Session"
    )
    team = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        empty_label=None,
        label="Your Team"
    )

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        # if you need to filter teams based on user, do it here

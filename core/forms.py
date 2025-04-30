

from django import forms
from .models import Vote, Session, Card, Team
from django.contrib.auth import get_user_model

User = get_user_model()

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
        # If you want to restrict the teams dropdown based on the user,
        # you can filter here, e.g.:
        # if user and user.role == 'engineer':
        #     self.fields['team'].queryset = Team.objects.filter(…)
        self.fields['card_votes'] = forms.MultipleChoiceField(
            choices=Vote.VOTE_CHOICES,
            widget=forms.RadioSelect,
            label='Cards Voting'
        )

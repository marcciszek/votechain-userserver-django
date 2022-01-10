from django import forms
from django.db import models


class ContVoteForm(forms.Form):
    class Cont(models.IntegerChoices):
        Afr = 0, "Afryka"
        Am_pd = 1, "Ameryka Południowa"
        Am_pn = 2, "Ameryka Północna"
        Ant = 3, "Antarktyda"
        Aus = 4, "Australia"
        Azj = 5, "Azja"
        Eur = 6, "Europa"
        

    vote = forms.ChoiceField(choices=Cont.choices,
                             label="")

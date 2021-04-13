from django import forms
from .models import Lead,Agent

# agent = Agent.objects.all()

# class LeadForm(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     age = forms.IntegerField()
#     agent = forms.ChoiceField(choices=agent)

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'


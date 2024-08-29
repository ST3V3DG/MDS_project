from django import forms
class AdminForm(forms.Form):
    nom=forms.CharField(max_length=60)
    mot_de_passe=forms.CharField(max_length=60)
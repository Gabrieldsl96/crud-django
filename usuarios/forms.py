from django import forms

from .models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nome", "email", "telefone"]
        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "class": "w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent",
                    "placeholder": "Nome completo",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent",
                    "placeholder": "email@exemplo.com",
                }
            ),
            "telefone": forms.TextInput(
                attrs={
                    "class": "w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent",
                    "placeholder": "(11) 99999-9999",
                }
            ),
        }

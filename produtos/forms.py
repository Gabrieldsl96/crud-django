from django import forms

from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "descricao", "preco", "estoque"]
        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "class": "w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent",
                    "placeholder": "Nome do produto",
                }
            ),
            "descricao": forms.Textarea(
                attrs={
                    "class": "w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent",
                    "rows": 3,
                    "placeholder": "Descrição do produto",
                }
            ),
            "preco": forms.NumberInput(
                attrs={
                    "class": "w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent",
                    "placeholder": "0.00",
                    "step": "0.01",
                }
            ),
            "estoque": forms.NumberInput(
                attrs={
                    "class": "w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent",
                    "placeholder": "0",
                }
            ),
        }

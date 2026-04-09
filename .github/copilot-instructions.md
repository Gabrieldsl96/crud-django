# Project Guidelines

## Stack

- **Backend**: Python 3.10+ / Django 6.x
- **Banco de dados**: SQLite em desenvolvimento; PostgreSQL em produção
- **Estilização**: Tailwind CSS via CDN (sem instalação local)
- **Variáveis de ambiente**: `python-decouple` (`.env` + `.env.example`)

---

## Estrutura de Diretórios

```
project-root/
├── project_config/          # Configurações Django (settings, urls, wsgi, asgi)
├── app_name/                # Cada feature é um app Django independente
│   ├── static/
│   │   └── app_name/        # Namespace obrigatório para evitar colisão no collectstatic
│   │       ├── css/
│   │       ├── js/
│   │       └── img/
│   ├── migrations/
│   ├── models.py
│   ├── views.py             # Function-based views (FBV)
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── tests.py
├── templates/               # Templates globais, organizados por app
│   ├── base.html
│   └── app_name/
│       ├── lista.html
│       ├── form.html
│       └── confirmar_delecao.html
├── static/                  # Saída do collectstatic — NÃO versionar, NÃO editar aqui
├── .env                     # Não versionado
├── .env.example             # Versionado, sem valores sensíveis
├── .gitignore
├── requirements.txt
└── manage.py
```

### Regras de estrutura

- **Statics por app**: cada app gerencia seus próprios CSS/JS em `app/static/app_name/`
- **Templates globais**: `templates/` na raiz, com subpasta por app para namespacing
- **`static/` raiz**: destino exclusivo do `collectstatic` (produção); não adicionar arquivos manualmente
- **Pastas vazias no Git**: usar `.gitkeep` apenas quando a pasta não tiver arquivo real (ex: `img/`)

---

## Settings

- `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` via `python-decouple`
- Em desenvolvimento: `DATABASES` com SQLite (`django.db.backends.sqlite3`)
- `STATIC_ROOT = BASE_DIR / "static"` — sem `STATICFILES_DIRS` global
- `TEMPLATES["DIRS"] = [BASE_DIR / "templates"]`
- `LANGUAGE_CODE = "pt-br"`, `TIME_ZONE = "America/Sao_Paulo"`

---

## URLs

- `project_config/urls.py` inclui as URLs de cada app com `namespace`
- Cada app tem seu próprio `urls.py`
- Padrão de rotas para CRUD:

| Método | URL                     | Name            |
|--------|-------------------------|-----------------|
| GET    | `/app/`                 | `app:lista`     |
| GET    | `/app/criar/`           | `app:criar`     |
| POST   | `/app/criar/`           | `app:criar`     |
| GET    | `/app/<id>/editar/`     | `app:editar`    |
| POST   | `/app/<id>/editar/`     | `app:editar`    |
| GET    | `/app/<id>/deletar/`    | `app:deletar`   |
| POST   | `/app/<id>/deletar/`    | `app:deletar`   |

---

## Views

- Usar **function-based views (FBV)**
- GET renderiza o template; POST processa e redireciona (`redirect` após sucesso)
- Usar `get_object_or_404` para buscar objetos por PK
- Usar `messages.success` / `messages.error` para feedback ao usuário

---

## Models

- Sempre incluir `criado_em = DateTimeField(auto_now_add=True)` e `atualizado_em = DateTimeField(auto_now=True)`
- `__str__` retornando o campo principal (ex: `nome`)
- Registrar no `admin.py`

---

## Forms

- Usar `ModelForm`
- Todos os widgets com classes Tailwind:
  ```python
  'class': 'w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent'
  ```
- Campos opcionais com `required=False` no widget quando necessário

---

## Templates

### base.html

- `{% load static %}` no topo
- Navbar dark (`bg-slate-900`) com logo e links por app
- Blocos: `{% block titulo %}`, `{% block conteudo %}`, `{% block extra_css %}`, `{% block extra_js %}`
- Mensagens com auto-dismiss (4s via JS inline) e botão de fechar
- Footer com `border-t border-slate-200`
- Layout `max-w-7xl mx-auto`

### Templates de listagem (`lista.html`)

- `{% load static %}` + `{% block extra_css %}` linkando o CSS do app
- Cabeçalho com título, subtítulo e botão "Novo" (indigo)
- Campo de busca ao vivo (`id="search-input"`) acima da tabela
- Tabela com `thead` em `bg-slate-50`, linhas com `hover:bg-slate-50 transition-colors`
- Botões de ação como chips coloridos com ícone SVG (Editar = indigo, Excluir = vermelho)
- Estado vazio com ícone SVG centralizado e CTA
- `{% block extra_js %}` linkando o JS do app

### Templates de formulário (`form.html`)

- Breadcrumb com link de volta
- Card `bg-white rounded-xl border border-slate-200 shadow-sm p-6`
- Campos em `space-y-4`, labels com `text-sm font-medium text-slate-700`
- Campos numéricos relacionados em `grid grid-cols-2 gap-4`
- Botão Salvar (indigo) com ícone de check; botão Cancelar (slate)
- Erros de validação em `text-red-500 text-xs mt-1`

### Templates de confirmação de exclusão (`confirmar_delecao.html`)

- Card com barra vermelha no topo (`h-1 bg-red-500`)
- Ícone de triângulo de aviso SVG em círculo vermelho
- Botão "Sim, excluir" (vermelho) + "Cancelar" (slate)

---

## CSS por App (`app/static/app_name/css/style.css`)

- Focus: `border-color: #6366f1; box-shadow: 0 0 0 3px rgba(99,102,241,0.15)`
- Animação sutil de entrada nas linhas da tabela (`rowFadeIn`)

## JS por App (`app/static/app_name/js/main.js`)

- Busca ao vivo na tabela via `input#search-input`, filtrando `tbody tr`
- Exibir `#no-results` quando não houver resultados
- Lógica de UI específica do app (ex: badges de estoque coloridos)

---

## Paleta de Cores (Tailwind)

| Uso                  | Classe                          |
|----------------------|---------------------------------|
| Fundo da página      | `bg-slate-50`                   |
| Navbar               | `bg-slate-900`                  |
| Cor primária (ações) | `bg-indigo-600 hover:bg-indigo-700` |
| Perigo (excluir)     | `bg-red-600 hover:bg-red-700`   |
| Texto principal      | `text-slate-800`                |
| Texto secundário     | `text-slate-500`                |
| Bordas               | `border-slate-200`              |
| Cards                | `bg-white rounded-xl border border-slate-200 shadow-sm` |

---

## Git e Versionamento

- `.env` nunca versionado; `.env.example` sempre atualizado
- `static/` (raiz) no `.gitignore` como `/static/`
- `db.sqlite3` no `.gitignore`
- `.gitkeep` apenas em pastas vazias que precisam ser rastreadas (ex: `img/`)

---

## Arquivos Estáticos em Produção

- `STATIC_ROOT = BASE_DIR / "static"` recebe os arquivos via `python manage.py collectstatic`
- Em desenvolvimento, o Django serve automaticamente os statics de cada app — não rodar `collectstatic` localmente
- Nunca editar arquivos dentro de `static/` (raiz) diretamente

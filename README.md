# CRUD Básico — Django + SQLite + Tailwind

CRUD de **Usuários** e **Produtos** construído com Django, SQLite e Tailwind CSS (via CDN).

## Tecnologias

- Python 3.x
- Django 6.x
- SQLite (banco embutido no Python)
- Tailwind CSS (CDN)
- python-decouple (variáveis de ambiente)

---

## Pré-requisitos

- Python 3.10+
- Git

---

## Como rodar o projeto

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd crud-basico
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
```

**Windows (PowerShell):**

```powershell
# Se der erro de permissão:
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

venv\Scripts\Activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Copie o arquivo `.env.example` para `.env` e preencha com seus dados:

```bash
cp .env.example .env
```

```env
SECRET_KEY=sua-secret-key-aqui
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 5. Execute as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. (Opcional) Crie um superusuário para o Admin

```bash
python manage.py createsuperuser
```

### 7. Rode o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Arquivos estáticos (CSS, JS, imagens)

Em **desenvolvimento**, o Django serve os estáticos automaticamente — nenhuma ação necessária.

Em **produção**, é preciso coletar todos os arquivos estáticos de cada app num único diretório (`static/`) para que o servidor web (Nginx, Apache, etc.) possa servi-los diretamente.

### Passos para produção

**1. Crie o diretório de saída na raiz do projeto (se ainda não existir):**

```bash
mkdir static
```

**2. Execute o collectstatic:**

```bash
python manage.py collectstatic
```

O Django irá copiar todos os arquivos de `usuarios/static/`, `produtos/static/` e de qualquer app instalado para a pasta `static/` na raiz. Essa pasta **não é versionada** (está no `.gitignore`).

> ⚠️ Nunca edite arquivos diretamente dentro de `static/` (raiz). Sempre edite nos respectivos `app/static/app/` e rode `collectstatic` novamente.

---

## Estrutura do projeto

```
crud-basico/
├── crud_basico/          # Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── usuarios/             # App de usuários
│   ├── static/
│   │   └── usuarios/     # Statics do app
│   │       ├── css/
│   │       ├── js/
│   │       └── img/
│   ├── models.py
│   ├── views.py          # Function-based views
│   ├── forms.py
│   └── urls.py
├── produtos/             # App de produtos
│   ├── static/
│   │   └── produtos/     # Statics do app
│   │       ├── css/
│   │       ├── js/
│   │       └── img/
│   ├── models.py
│   ├── views.py          # Function-based views
│   ├── forms.py
│   └── urls.py
├── templates/
│   ├── base.html         # Template base com Tailwind CDN
│   ├── usuarios/
│   │   ├── lista.html
│   │   ├── form.html
│   │   └── confirmar_delecao.html
│   └── produtos/
│       ├── lista.html
│       ├── form.html
│       └── confirmar_delecao.html
├── static/               # Saída do collectstatic (não versionado)
├── .env                  # Variáveis de ambiente (não versionado)
├── .env.example          # Exemplo de variáveis de ambiente
├── .gitignore
├── requirements.txt
└── manage.py
```

---

## Rotas disponíveis

| Método | URL                       | Descrição                  |
| ------ | ------------------------- | -------------------------- |
| GET    | `/usuarios/`              | Listagem de usuários       |
| GET    | `/usuarios/criar/`        | Formulário de novo usuário |
| POST   | `/usuarios/criar/`        | Criar usuário              |
| GET    | `/usuarios/<id>/editar/`  | Formulário de edição       |
| POST   | `/usuarios/<id>/editar/`  | Atualizar usuário          |
| GET    | `/usuarios/<id>/deletar/` | Confirmar exclusão         |
| POST   | `/usuarios/<id>/deletar/` | Excluir usuário            |
| GET    | `/produtos/`              | Listagem de produtos       |
| GET    | `/produtos/criar/`        | Formulário de novo produto |
| POST   | `/produtos/criar/`        | Criar produto              |
| GET    | `/produtos/<id>/editar/`  | Formulário de edição       |
| POST   | `/produtos/<id>/editar/`  | Atualizar produto          |
| GET    | `/produtos/<id>/deletar/` | Confirmar exclusão         |
| POST   | `/produtos/<id>/deletar/` | Excluir produto            |

---

## Modelos

### Usuario

| Campo         | Tipo                     |
| ------------- | ------------------------ |
| nome          | CharField (150)          |
| email         | EmailField (único)       |
| telefone      | CharField (20, opcional) |
| criado_em     | DateTimeField (auto)     |
| atualizado_em | DateTimeField (auto)     |

### Produto

| Campo         | Tipo                 |
| ------------- | -------------------- |
| nome          | CharField (200)      |
| descricao     | TextField (opcional) |
| preco         | DecimalField (10, 2) |
| estoque       | PositiveIntegerField |
| criado_em     | DateTimeField (auto) |
| atualizado_em | DateTimeField (auto) |

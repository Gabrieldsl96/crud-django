# CRUD Básico — Django + PostgreSQL + Tailwind

CRUD de **Usuários** e **Produtos** construído com Django, PostgreSQL e Tailwind CSS (via CDN).

## Tecnologias

- Python 3.x
- Django 6.x
- PostgreSQL (psycopg2-binary)
- Tailwind CSS (CDN)
- python-decouple (variáveis de ambiente)

---

## Pré-requisitos

- Python 3.10+
- PostgreSQL instalado e rodando
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

DB_NAME=crud_basico_db
DB_USER=postgres
DB_PASSWORD=sua-senha-aqui
DB_HOST=localhost
DB_PORT=5432
```

### 5. Crie o banco de dados no PostgreSQL

```sql
CREATE DATABASE crud_basico_db;
```

### 6. Execute as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. (Opcional) Crie um superusuário para o Admin

```bash
python manage.py createsuperuser
```

### 8. Rode o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Estrutura do projeto

```
crud-basico/
├── crud_basico/          # Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── usuarios/             # App de usuários
│   ├── models.py
│   ├── views.py          # Function-based views
│   ├── forms.py
│   └── urls.py
├── produtos/             # App de produtos
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

# E-commerce

Um projeto simples de e-commerce (ainda incompleto) feito com Django 5.0.3 e Python 3.12.

Este projeto foi criado no [Curso de Python 3 - Do Básico Ao Avançado (Completo)](https://www.udemy.com/course/python-3-do-zero-ao-avancado/).

Projeto possui funcionalidades padrões de um E-commerce, como:

- [x] Model produtos
- [x] Model variações
- [x] Listagem e detalhes de produtos e variações
- [x] Carrinho de compras baseado em session
- [x] Remover produtos do carrinho
- [x] Model perfil (criar e atualizar)
- [x] Login e Logout do cliente
- [x] Registrar pedido do cliente
- [x] Página de pagamento

## 🚀 Começando

Estas instruções permitirão que você obtenha uma cópia do projeto em execução em sua máquina local para fins de desenvolvimento e teste.

## Instalação

- Instalar git (Windows, Linux e Mac) e depois:

1. Clone este repositório em sua máquina local.

```
git clone https://github.com/guicamargo19/ecommerce.git
```

2. Navegue até o diretório clonado.

```
cd django-simple-ecommerce
```

3. Siga estas etapas a seguir para configurar o ambiente de desenvolvimento:

- Para **Windows**:

```
python -m venv venv
venv\Scripts\activate.bat
python -m pip install --upgrade pip setuptools wheel --user
python -m pip install django django-debug-toolbar django-crispy-forms pillow
python manage.py migrate
```

- Para **Linux**:

```
python3.7 -m venv venv
. venv/bin/activate
pip install django django-debug-toolbar django-crispy-forms pillow
python manage.py migrate
```

- Para **Mac**

```
python -m venv venv
. venv/bin/activate
pip install django django-debug-toolbar django-crispy-forms pillow
python manage.py migrate
```

## 🛠️ Ferramentas utilizadas para construção do projeto

* **Python** - Linguagem de alto nível, interpretada de script, orientada a objetos, funcional, de tipagem dinâmica e forte.
* **Django** - Framework para desenvolvimento rápido para web, escrito em Python, que utiliza o padrão model-template-view.
* **HTML** - Linguagem de marcação utilizada na construção de páginas na Web.
* **CSS** - Cascading Style Sheets é um mecanismo para adicionar estilos a uma página web.
* **JavaScript** - Linguagem de programação interpretada estruturada, de alto nível com tipagem dinâmica fraca e multiparadigma.
* **Bootstrap** - Framework web open-source para desenvolvimento de componentes de interface para sites e aplicações web.

## ✒️ Autor

Guilherme Ferreira Camargo

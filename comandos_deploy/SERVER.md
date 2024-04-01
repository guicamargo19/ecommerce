# Configuração para deploy

## Primeiros passos

- Prepare o local_settings.py
- Crie o seu servidor Ubuntu 20.04 LTS (onde preferir)

Comando para gerar SECRET_KEY

```
python -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"
```

## Criando sua chave SSH

```
ssh-keygen -C 'COMENTÁRIO'
```

## No servidor

### Conectando

```
ssh usuário@IP_SERVIDOR
```

### Comandos iniciais

```
sudo apt update -y
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt install build-essential -y

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.11 python3.11-venv -y

sudo apt install nginx -y
sudo apt install certbot python3-certbot-nginx -y
sudo apt install postgresql postgresql-contrib -y
sudo apt install libpq-dev -y
sudo apt install git -y
```

### Configurando o git

```
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
```

Criando as pastas do projeto e repositório

```
mkdir ~/blogrepo ~/blogapp
```

Configurando os repositórios

```
cd ~/blogrepo
git init --bare
cd ..
cd ~/blogapp
git init
git remote add blogrepo ~/blogrepo
git add .
git commit -m 'Initial'
git push blogrepo main -u # erro
```

No seu computador local

```
git remote add blogrepo usuario@IP_SERVIDOR:~/blogrepo
git push blogrepo main
```

No servidor

```
cd ~/blogapp
git pull blogrepo main
```

## Configurando o Postgresql

```
sudo -u postgres psql

postgres=# create role user with login superuser createdb createrole password 'senha_do_usuario';
CREATE ROLE
postgres=# create database base_de_dados with owner user;
CREATE DATABASE
postgres=# grant all privileges on database base_de_dados to user;
GRANT
postgres=# \q

sudo systemctl restart postgresql

```

## Criando o local_settings.py no servidor

```
nano ~/blogapp/project/local_settings.py
```

Cole os dados.

## Configurando o Django no servidor

```
cd ~/blogapp
python3.11 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install django
pip install pillow
pip install gunicorn
pip install psycopg
pip install faker

python manage.py runserver
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

## Permitir arquivos maiores no nginx

```
sudo nano /etc/nginx/nginx.conf
```

Adicione em http {}:

```
client_max_body_size 30M;
```

```
sudo systemctl restart nginx
```
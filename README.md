# Gymbro
## Descrição
Esse projeto se trata de um web site para registro de execuções da sua academia. Ele foi feito usando python.

## Dependências
Esse projeto roda com o Python 3.14.6.

Os pacotes instalados são:
- Flask 3.1.3
- SQLAlchemy 2.0.52
- Alembic 1.19.1
- Mysql Connector Python 26.7.0
Para instalar esses pacotes rode o comando abaixo:
```sh
pip install flask==3.1.3 sqlalchemy==2.0.52 alembic==1.19.1 mysql-connector-python==26.7.0
```

O banco de dados principal usado é o mysql 8.4.9, porém, devido ao sqlalchemy, qualquer banco de dados pode ser usado.

## Inicialização
### Definição de configuração de configuração
Os arquivos de configuração são o .env e o alembic.ini, porém aparece apenas suas versões de exemplo(terminam com a extensão ".example"). 
Para ter os arquivos de configuração originais, remova a extensão ".example" e defina as configurações como quiser.

### Inicialização do banco de dados
Garanta que o seu banco de dados esteja em execução e crie um banco com o nome que desejar.

### Rode as migrations
Para atualizar o banco de banco é necessário rodar as migrations do alembic.
Use o comando a seguir para isso:

```sh
alembic upgrade head
```

Também é preciso definir a variável "sqlalchemy.url" em alembic.ini com a url do seu banco de dados.

### Inicialize a aplicação
Para isso rode o comando a baixo:
```sh
python main.py
```
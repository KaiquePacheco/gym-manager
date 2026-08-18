from main import db
from models import Usuario
from main import bcrypt

def cadastrar(email, senha):
    usuario = Usuario(email=email, senha=bcrypt.generate_password_hash(senha).decode('utf-8'))

    try:
        db.session.add(usuario)
        db.session.commit()
        return True
    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")
        db.session.rollback()
        return False

def login(email, senha):
    usuario = Usuario.query.filter_by(email=email).first()

    if usuario and bcrypt.check_password_hash(usuario.senha, senha):
        return usuario

    return None
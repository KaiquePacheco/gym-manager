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
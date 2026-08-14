import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Uuid, CHAR, String
from sqlalchemy.orm import Mapped, mapped_column

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[uuid.Uuid] = mapped_column(Uuid, primary_key=True, nullable=False, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(CHAR(60), nullable=False)

metadata = Base.metadata
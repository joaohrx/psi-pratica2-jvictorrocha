from typing import List

from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


# TODO: crie o modelo Autor.
# Campos: id, nome, pais.
# Relacionamento: livros.
class Autor(Base):
    __tablename__ = "autores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    pais: Mapped[str] = mapped_column(String(100), nullable=False)

    livros: Mapped[List["Livro"]] = relationship('Livro', back_populates='autor')
    


# TODO: crie o modelo Livro.
# Campos: id, titulo, ano, autor_id.
# Relacionamento: autor.
class Livro(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    ano: Mapped[int] = mapped_column(Integer, nullable=False)
    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id"))

    autor: Mapped["Autor"] = relationship('Autor', back_populates='livros')



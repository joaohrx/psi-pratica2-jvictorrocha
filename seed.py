from models import Autor, Livro


def popular_banco(session):
    # TODO: crie pelo menos 3 autores e 6 livros.
    autor1 = Autor(nome="Jorge Luis Borges", pais="Argentina")
    autor2 = Autor(nome="Lygia Fagundes Telles", pais="Brasil")
    autor3 = Autor(nome="Italo Calvino", pais="Itália")

    livros = [
        Livro(titulo="Cidades Invisíveis", ano=1972, autor=autor3),
        Livro(titulo="Se um viajante numa noite de inverno", ano=1979, autor=autor3),
        Livro(titulo="Ficções", ano=1945, autor=autor1),
        Livro(titulo="O Aleph", ano=1949, autor=autor1),
        Livro(titulo="Antes do Baile Verde", ano=1970, autor=autor2),
        Livro(titulo="As Meninas", ano=1973, autor=autor2), 
    ]

    session.add_all(livros)
    session.commit()



    # TODO: relacione os livros aos autores.
    # TODO: use session.add ou session.add_all e session.commit.
    pass

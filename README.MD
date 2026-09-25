# Prática Orientada 02

## Onde estão os modelos ORM no seu projeto?
Estão nos arquivos de models.py e database.py

## Qual classe representa o lado "um" e qual representa o lado "muitos" no relacionamento?
O Livro representa o lado 1 e o Autor representa o lado muitos, já que um livro só pode ter um único autor e um autor pode ter diversos livros.

## Para que serve o ForeignKey em Livro.autor_id ?
Para criar um relacionamento entre a classes Livro e Autor

## O que acontece se você esquecer o session.commit() após inserir os dados?
Os dados não serão salvos no Banco.

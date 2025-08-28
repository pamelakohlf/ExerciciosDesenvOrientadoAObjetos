class Livro:
  def __init__(self,nome,autor,editora,paginas):
    self.nome = nome
    self.autor = autor
    self.editora = editora
    self.paginas = paginas

  def alterar_editora(self,nova_editora):
    if nova_editora == self.editora:
      print("Mesma editora")
    else:
      self.editora = nova_editora

  def listar_qtde_paginas(self):
    print(f'A quantidade de páginas é: {self.paginas}')

livro1 = Livro("Primeiro eu tive que morrer","Lorena Portela","Planeta",176)

livro1.alterar_editora("Planeta")
livro1.alterar_editora("Planeta ABC")
print(f'Editora alterada para: {livro1.editora}')
livro1.listar_qtde_paginas()
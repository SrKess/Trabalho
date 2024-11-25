#Gabriel Kesley da Silva Cesário
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def descricao(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) < 3 and livro.disponivel:
            self.livros_emprestados.append(livro)
            livro.disponivel = False
            print(f"Livro '{livro.titulo}' emprestado com sucesso!")
        else:
            print("Empréstimo não permitido. Limite atingido ou livro indisponível.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.disponivel = True
            print(f"Livro '{livro.titulo}' devolvido com sucesso!")
        else:
            print("O livro não está emprestado por este usuário.")

    def descricao(self):
        return f"Usuário: {self.nome}, Matrícula: {self.matricula}"

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def descricao(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"Livro: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Status: {status}"

if __name__ == "__main__":

    livro1 = Livro("Python para Iniciantes", "Guido van Rossum", 2023)
    
    usuario = UsuarioComum("Carlos", 20, "20230001")

    print(usuario.descricao())
    print(livro1.descricao())

    usuario.emprestar_livro(livro1)
    print(livro1.descricao())

    usuario.devolver_livro(livro1)
    print(livro1.descricao())

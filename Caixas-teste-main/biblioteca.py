class Biblioteca:
    def __init__(self):
        self.livros = {}  # Armazena os livros com o status de disponíveis ou emprestados

    def adicionar_livro(self, titulo):
        if not titulo.strip():
            raise ValueError("O título do livro não pode ser vazio.")
        if titulo in self.livros:
            raise ValueError("O livro já está cadastrado.")
        self.livros[titulo] = "disponível"
        return f"Livro '{titulo}' adicionado com sucesso."

    def emprestar_livro(self, titulo):
        if titulo not in self.livros:
            raise ValueError("Livro não encontrado na biblioteca.")
        if self.livros[titulo] == "emprestado":
            raise ValueError("Livro já emprestado.")
        self.livros[titulo] = "emprestado"
        return f"Livro '{titulo}' emprestado com sucesso."

    def retornar_livro(self, titulo):
        if titulo not in self.livros:
            raise ValueError("Livro não encontrado na biblioteca.")
        if self.livros[titulo] == "disponível":
            return "Livro já está disponível."
        self.livros[titulo] = "disponível"
        return f"Livro '{titulo}' retornado com sucesso."

    def listar_livros(self):
        return self.livros

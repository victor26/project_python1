class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f' {self._nome} - Ano: {self.ano} - Likes: {self._likes} '

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len (self._programas)

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f' {self._nome} - Ano: {self.ano} - {self.duracao} min - Likes: {self._likes} '

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f' {self._nome} - Ano: {self.ano} - {self.temporadas} temporadas -Likes: {self._likes} '

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
guardioes = Filme('Guardiões da galaxia', 2016, 175 )
atlanta = Serie('atlanta', 2018, 2)
twc=Serie('The witcher', 2017, 2)
vingadores.dar_likes()
guardioes.dar_likes()
guardioes.dar_likes()
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta, twc, guardioes]
play_fds = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(play_fds)}')

for programa in play_fds:
    print(programa)
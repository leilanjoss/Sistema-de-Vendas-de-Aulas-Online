from model.aula import Aula
from model.professor import Professor
from typing import List


class Curso:
    def __init__(self,
                 nome: str,
                 preco_atual: float,
                 descricao: str,
                 tempo: str,
                 codigo_curso: str,
                 professor: Professor,
                aulas: List[Aula],
                 ):
        self.__nome = nome
        self.__preco_atual = preco_atual
        self.__descricao = descricao
        self.__tempo = tempo
        self.__codigo_curso = codigo_curso
        self.__professor = professor
        self.__aulas = aulas

    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco_atual(self):
        return self.__preco_atual

    @property
    def descricao(self):
        return self.__descricao

    @property
    def tempo(self):
        return self.__tempo

    @property
    def codigo_curso(self):
        return self.__codigo_curso

    @property
    def professor(self):
        return self.__professor

    @property
    def aulas(self):
        return self.__aulas
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @preco_atual.setter
    def preco_atual(self, preco_atual):
        self.__preco_atual = preco_atual

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
    
    @tempo.setter
    def tempo(self, tempo):
        self.__tempo = tempo

    @codigo_curso.setter
    def codigo_curso(self, codigo_curso):
        self.__codigo_curso = codigo_curso
    
    @professor.setter
    def professor(self, professor):
        self.__professor = professor
    
    @aulas.setter
    def aulas(self, aulas):
        self.__aulas = aulas

    def nome_professor(self):
        return self.__professor.nome


        
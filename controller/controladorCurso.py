from view.telaCurso import TelaCurso
from model.curso import Curso
from model.aula import Aula
from DAOs.curso_dao import CursoDAO
from exceptions.curso_exceptions import CursoRepetidoException
from exceptions.curso_exceptions import CursoNExisteException


class ControladorCurso:
    def __init__(self):
        self.__curso_dao = CursoDAO()
        self.__tela_curso = TelaCurso()

    
    def pegar_curso_por_codigo(self, codigo_curso):
        for curso in self.__curso_dao.get_all():
            if curso.codigo_curso == codigo_curso:
                return curso
        return None
    
    def inserir_curso(self):
        self.listar_cursos()
        dados_curso = self.__tela_curso.pegar_dados_curso()
        curso = self.pegar_curso_por_codigo(dados_curso["codigo_curso"])
        try:
            if curso is None:
                novo_curso = Curso(dados_curso["nome"], 
                                dados_curso["preco_atual"], 
                                dados_curso["descricao"], 
                                dados_curso["tempo"], 
                                dados_curso["codigo_curso"],
                                dados_curso["professor"],
                                dados_curso["aulas"]
                                )
                
                print('novo_curso', novo_curso)
                self.__curso_dao.add(novo_curso)
                self.__tela_curso.mostrar_mensagem("Curso inserido.")
            else:
                raise CursoRepetidoException(curso)
        except CursoRepetidoException as e:
            self.__tela_curso.mostrar_mensagem(e)

    def excluir_curso(self):
        self.listar_cursos()
        codigo_curso = self.__tela_curso.selecionar_curso()
        curso = self.pegar_curso_por_codigo(codigo_curso)
        try:
            if curso is not None:
                self.__curso_dao.remove(curso.codigo_curso)
                self.__tela_curso.mostrar_mensagem("Curso excluído.")
                self.listar_cursos()
            else:
                raise CursoNExisteException()
        except CursoNExisteException as e:
            self.__tela_curso.mostrar_mensagem(e)

    def listar_cursos(self):
        if not self.__curso_dao:
            self.__tela_curso.mostrar_mensagem("Nenhum curso cadastrado.")
        else:
            self.__tela_curso.mostrar_cursos(self.__curso_dao.get_all())

    def alterar_curso(self):
        codigo_curso = self.__tela_curso.selecionar_curso()
        curso = self.pegar_curso_por_codigo(codigo_curso)
        if curso is not None:
            novos_dados_curso = self.__tela_curso.pegar_dados_curso()
            curso.nome = novos_dados_curso["nome"]
            curso.tempo = novos_dados_curso["tempo"]
            curso.descricao = novos_dados_curso["descricao"]
            curso.professor = novos_dados_curso["professor"]
            curso.preco_atual = novos_dados_curso["preco_atual"]
            curso.codigo_curso = novos_dados_curso["codigo_curso"]
            curso.aulas = novos_dados_curso["aulas"]
            self.__curso_dao.update(curso)
            print('novos_dados_curso', novos_dados_curso)
            self.__tela_curso.mostrar_mensagem('Curso alterado.')
        else:
            self.__tela_curso.mostrar_mensagem('Não foi possível alterar o curso.')
    
    def retornar(self):
        from controller.controladorSistema import ControladorSistema
        ControladorSistema().abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.inserir_curso, 
                        2: self.alterar_curso, 
                        3: self.listar_cursos, 
                        4: self.excluir_curso, 
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_curso.tela_opcoes()]()
    
        
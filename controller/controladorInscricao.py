from model.inscricao import Inscricao
from controller.controladorCurso import ControladorCurso
from view.telaInscricao import TelaInscricao
from controller.controladorAluno import ControladorAluno
from model.aluno import Aluno
from model.curso import Curso
from DAOs.inscricao_dao import InscricaoDAO

class ControladorInscricao:
    def __init__(self, controlador_sistema):
        # self.__inscricoes = [] # Substituido por DAO
        self.__controlador_sistema = controlador_sistema
        self.__controlador_curso = ControladorCurso()
        self.__tela_inscricao = TelaInscricao()
        self.__controlador_aluno = ControladorAluno()
        self.__inscricao_DAO = InscricaoDAO()

    @property
    def inscricoes(self):
        return self.__inscricoes

    def inserir_inscricao(self):
        self.__controlador_aluno.listar_alunos()
        self.__controlador_curso.listar_cursos()
        dados_inscricao = self.__tela_inscricao.pegar_dados_inscricao()
        
        print(dados_inscricao)
        print(dados_inscricao['cpf_aluno']) # Ambos deram certo
        
        aluno = self.__controlador_aluno.pegar_aluno_por_cpf(dados_inscricao['cpf_aluno'])
        curso = self.__controlador_curso.pegar_curso_por_codigo(dados_inscricao['cod_curso'])
        
        if isinstance(aluno, Aluno) and isinstance(curso, Curso):
            nova_inscricao = Inscricao(curso, aluno, dados_inscricao['data_hora'], dados_inscricao['id_inscricao'])
            self.__inscricao_DAO.add(nova_inscricao)
            self.__tela_inscricao.mostra_mensagem("Aluno inserido")
        else:
            self.__tela_inscricao.mostra_mensagem("Aluno ou curso não encontrado")




    def excluir_inscricao(self):
        codigo_curso = input("Digite o código do curso: ")
        inscricao_a_excluir = None
        for inscricao in self.__inscricoes:
            if inscricao.curso.codigo_curso == codigo_curso:
                inscricao_a_excluir = inscricao
                break
        if inscricao_a_excluir:
            self.__inscricoes.remove(inscricao_a_excluir)
            self.__tela_inscricao.mostra_mensagem("Inscrição excluída com sucesso!")
        else:
            self.__tela_inscricao.mostra_mensagem("Inscrição não encontrada!")

    def atualizar_inscricao(self):
        codigo_curso = input("Digite o código do curso: ")
        for inscricao in self.__inscricoes:
            if inscricao.curso.codigo_curso == codigo_curso:
                cpf_aluno = input("Digite o novo CPF do aluno: ")
                preco_pago = float(input("Digite o novo preço pago: "))
                data_hora = input("Digite a nova data e hora: ")
                inscricao.aluno = cpf_aluno
                inscricao.preco_pago = preco_pago
                inscricao.data_hora = data_hora
                self.__tela_inscricao.mostra_mensagem("Inscrição atualizada com sucesso!")
                return
        self.__tela_inscricao.mostra_mensagem("Inscrição não encontrada!")

    def retornar(self):
        self.__controlador_sistema.abrir_tela()

    def finalizar_sistema(self):
        exit()

    def abrir_tela(self):
        lista_opcoes = {
            1: self.inserir_inscricao,
            2: self.excluir_inscricao,
            3: self.atualizar_inscricao,
            4: self.retornar,
            0: self.finalizar_sistema
        }
        
        continua = True
        while continua:
            opcao_escolhida = self.__tela_inscricao.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            if funcao_escolhida:
                funcao_escolhida()
            else:
                print("Opção inválida. Escolha novamente.")




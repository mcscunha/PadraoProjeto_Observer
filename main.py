''' Padrao de Projeto Observer '''

# Objeto oservador
class Observador:
    def __init__(self, nome):
        self.nome = nome


# Objeto observado
class Passaro:
    # Forma de adicionar classe em outra classe
    def __init__(self):
        self.observadores = []  # <<== 
    
    def adic_observador(self, observador):
        # Aqui esta o "pulo do gato" - associar a classe acima na 
        # lista desta classe, assim, pode-se acessar as "coisas" dele!
        self.observadores.append(observador)

    def enviar_msg(self, mensagem):
        for observador in self.observadores:
            # Acessando o NOME do observador nesta classe!
            # Interessante abordagem!
            print( f'|{observador.nome} recebeu | {mensagem}' )


observ_1 = Observador('Murilo')
observ_2 = Observador('Mauricio')
observ_3 = Observador('Fabricio')

pardal = Passaro()
pardal.adic_observador(observ_1)
pardal.adic_observador(observ_2)
pardal.adic_observador(observ_3)

pardal.enviar_msg('Estão vendo o mesmo pássaro?')

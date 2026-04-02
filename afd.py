import random


class AutomatoFinito:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        self.estados = set(estados)
        self.alfabeto = set(alfabeto)
        self.transicoes = dict(transicoes)
        self.estado_inicial = estado_inicial
        self.estados_finais = set(estados_finais)

        self.validar_automato()

    def validar_automato(self):
        if self.estado_inicial not in self.estados:
            raise ValueError("Estado inicial inválido")

        if not self.estados_finais.issubset(self.estados):
            raise ValueError("Estados finais inválidos")

    def delta(self, estado, simbolo):
        return self.transicoes.get((estado, simbolo), None)

    def processar(self, palavra, mostrar_passos=False):
        estado_atual = self.estado_inicial

        if mostrar_passos:
            print(f"Estado inicial: {estado_atual}")

        for simbolo in palavra:
            proximo_estado = self.delta(estado_atual, simbolo)

            if proximo_estado is None:
                return False

            if mostrar_passos:
                print(f"δ({estado_atual}, {simbolo}) = {proximo_estado}")

            estado_atual = proximo_estado

        if mostrar_passos:
            print(f"Estado final: {estado_atual}")

        return estado_atual in self.estados_finais

    #gerar palavra aleatória
    def gerar_palavra_aleatoria(self, tamanho):
        return "".join(random.choice(list(self.alfabeto)) for _ in range(tamanho))

    #testar várias palavras aleatórias
    def testar_palavras_aleatorias(self, quantidade=10, tamanho_max=5):
        print("\n=== Testando palavras aleatórias ===")

        for _ in range(quantidade):
            tamanho = random.randint(0, tamanho_max)
            palavra = self.gerar_palavra_aleatoria(tamanho)

            resultado = self.processar(palavra)
            print(f"Palavra: '{palavra}' -> {'ACEITA' if resultado else 'REJEITADA'}")

#exemplo
estados = {"q0", "q1"}
alfabeto = {"0", "1"}

transicoes = {
    ("q0", "0"): "q0",
    ("q0", "1"): "q1",
    ("q1", "0"): "q0",
    ("q1", "1"): "q1",
}

estado_inicial = "q0"
estados_finais = {"q1"}

automato = AutomatoFinito(
    estados,
    alfabeto,
    transicoes,
    estado_inicial,
    estados_finais
)

#Teste automático
automato.testar_palavras_aleatorias(quantidade=10, tamanho_max=6)
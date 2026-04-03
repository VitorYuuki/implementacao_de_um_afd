import random


class AutomatoDeterministico:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        self.estados = set(estados)
        self.alfabeto = list(alfabeto)
        self.transicoes = dict(transicoes)
        self.estado_inicial = estado_inicial
        self.estados_finais = set(estados_finais)

        self.validar_afd()

    def validar_afd(self):
        if self.estado_inicial not in self.estados:
            raise ValueError("Estado inicial inválido.")

        if not self.estados_finais.issubset(self.estados):
            raise ValueError("Há estados finais inválidos.")

        for estado in self.estados:
            for simbolo in self.alfabeto:
                if (estado, simbolo) not in self.transicoes:
                    raise ValueError(
                        f"Transição ausente para ({estado}, {simbolo}). "
                        "Em um AFD, toda transição deve estar definida."
                    )

                destino = self.transicoes[(estado, simbolo)]

                if destino not in self.estados:
                    raise ValueError(
                        f"Destino inválido na transição ({estado}, {simbolo}) -> {destino}"
                    )

    def delta(self, estado, simbolo):
        return self.transicoes[(estado, simbolo)]

    def processar(self, palavra, mostrar_passos=True):
        estado_atual = self.estado_inicial

        if mostrar_passos:
            print(f"Estado inicial: {estado_atual}")

        for simbolo in palavra:
            if simbolo not in self.alfabeto:
                print(f"Símbolo inválido: {simbolo}")
                return False

            proximo_estado = self.delta(estado_atual, simbolo)

            if mostrar_passos:
                print(f"δ({estado_atual}, {simbolo}) = {proximo_estado}")

            estado_atual = proximo_estado

        if mostrar_passos:
            print(f"Estado final: {estado_atual}")

        return estado_atual in self.estados_finais

    def gerar_palavra_aleatoria(self, tamanho):
        return "".join(random.choice(self.alfabeto) for _ in range(tamanho))

# EXEMPLO DE AFD


estados = {"q0", "q1"}
alfabeto = ["a", "b"]

transicoes = {
    ("q0", "a"): "q1",
    ("q0", "b"): "q0",
    ("q1", "a"): "q1",
    ("q1", "b"): "q0"
}

estado_inicial = "q0"
estados_finais = {"q1"}

automato = AutomatoDeterministico(
    estados,
    alfabeto,
    transicoes,
    estado_inicial,
    estados_finais
)

# MENU

while True:
    print("\n=== AUTÔMATO FINITO DETERMINÍSTICO ===")
    print("1 - Testar palavra manualmente")
    print("2 - Gerar palavra aleatória")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        palavra = input("Digite a palavra: ").strip().lower()
        resultado = automato.processar(palavra, mostrar_passos=True)
        print("Resultado:", "ACEITA" if resultado else "REJEITADA")

    elif opcao == "2":
        tamanho = int(input("Tamanho da palavra: "))
        palavra = automato.gerar_palavra_aleatoria(tamanho)
        print("Palavra gerada:", palavra)
        resultado = automato.processar(palavra, mostrar_passos=True)
        print("Resultado:", "ACEITA" if resultado else "REJEITADA")

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")

Autômato Finito em Python

Este projeto implementa um Autômato Finito Determinístico (AFD) de forma simples e prática utilizando Python.
A ideia é permitir que você simule o comportamento de um autômato, teste palavras e até gere entradas aleatórias para validação.

O que esse código faz?

Com esse código você consegue:

Criar um autômato finito com estados, alfabeto e transições
Processar palavras e verificar se são aceitas ou rejeitadas
Visualizar o passo a passo da execução (opcional)
Gerar palavras aleatórias automaticamente
Testar várias palavras de forma automática
  Conceito rápido

Um Autômato Finito é um modelo matemático usado para representar sistemas com estados, muito comum em:

Compiladores
Validação de strings
Inteligência artificial
Sistemas embarcados
  Estrutura do código

A classe principal é:

AutomatoFinito

Ela recebe:

estados: conjunto de estados
alfabeto: símbolos permitidos
transicoes: regras de mudança de estado
estado_inicial: ponto de partida
estados_finais: estados de aceitação
  Funcionalidades
  Processar palavra

Use o método processar para validar uma palavra:

automato.processar("101", mostrar_passos=True)

Mostra o caminho percorrido (se ativado)
Retorna True (aceita) ou False (rejeita)
  Gerar palavra aleatória

automato.gerar_palavra_aleatoria(5)

Gera uma palavra com base no alfabeto definido.

  Testar várias palavras automaticamente

automato.testar_palavras_aleatorias(quantidade=10, tamanho_max=6)

Exemplo de saída:

Palavra: '101' -> ACEITA
Palavra: '00' -> REJEITADA

  Exemplo usado no código

O autômato definido possui:

Estados: q0, q1
Alfabeto: 0 e 1
Estado inicial: q0
Estado final: q1

Regra importante:
Esse autômato aceita palavras que terminam em 1.

  Como executar
Salve o arquivo como automato.py
Execute no terminal:

python automato.py

  Exemplo de saída

=== Testando palavras aleatórias ===
Palavra: '1' -> ACEITA
Palavra: '000' -> REJEITADA
Palavra: '1011' -> ACEITA

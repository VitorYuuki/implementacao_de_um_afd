# Como as coisas funcionam por dentro
O código usa alguns conceitos principais:
 * Estados: São os "lugares" onde a máquina pode estar (tipo q_0 e q_1).
 * Alfabeto: As únicas letras que a máquina entende (nesse caso, a e b).
 * Transições: São as regras de movimento. Exemplo: "se estiver no q_0 e ler a, pule para o q_1".
 * Estado Inicial: Onde tudo começa.
 * Estados Finais: Se a palavra acabar e você estiver em um desses estados, você "venceu" e a palavra é aceita.
# O que o programa faz
Quando você roda o arquivo, ele te dá opções em um menu:
 * Testar na mão: Você digita uma palavra e ele mostra o caminho que fez entre os estados até dar o resultado.
 * Gerar aleatório: O computador inventa uma palavra com as letras permitidas e testa sozinho para ver o que acontece.
 * Sair: Fecha o programa.
Exemplo prático do código
Nesse arquivo, a regra é simples: o estado final é o q_1. Para terminar nele, a última letra da palavra geralmente precisa ser um a, porque o b sempre te manda de volta (ou te segura) no estado q_0.

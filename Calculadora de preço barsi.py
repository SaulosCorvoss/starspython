papel = input("Qual é o ativo?: ").strip().upper()
price = float(input("Qual é o preço?: ").strip().replace(",", "."))
lpa = float(input("Qual é o LPA?: ").strip().replace(",", "."))
dividendo = float(input("Quantos porcentos de Dividend Yield por ano deseja?: ").strip().replace(",", ".")
                  .replace("%", " "))

# Pergunte ao usuário se deseja calcular a média
ajuda = input("Precisa calcular a média de Dividendos pagos nos últimos 4 anos? (sim/não): ").strip()
if ajuda.lower() == "sim":
    # O usuário deseja calcular a média
    dividendos_ultimos_anos = []
    for i in range(1, 5):
        dividendo_ano = float(input(f"Digite o dividendo do {i}º ano: ").strip().replace(",", "."))
        dividendos_ultimos_anos.append(dividendo_ano)

    # Calcule a média
    dividend = sum(dividendos_ultimos_anos) / len(dividendos_ultimos_anos)

    # Mostre o resultado
    print(f"A média dos últimos 4 anos é: {dividend} reais")
else:
    # O usuário não deseja calcular a média
    dividend = float(input("Qual é a média de dividendos nos últimos anos então?: ").strip().replace(",", "."))

div100 = dividendo / 100
result = (dividend / div100)
diferenca = result - price
earinig_yield = (lpa / price) * 100

def calcular_desconto(price, diferenca):
    variacao_percentual = (price - diferenca) / price * 100
    return variacao_percentual

desconto = calcular_desconto(price, diferenca)

if result > price:
    print("\nO valor de acordo com a porcentagem de {}%, que você nos informou,\n"
          "o preço justo para {} é de {:.2f} reais, e com valor de {}, \nisso significa que "
          "o seu preço está {:.3f} R$ abaixo de seu valor. O desconto do ativo esta de {:.2f}%."
          "E seu potencial de crecismento no ano é de {:.2f}%"
          .format(dividendo, papel, result, price, diferenca, desconto, earinig_yield))
else:
    print("O preço está muito caro para seus parâmetros,"
          " com um Dividend Yield esperado de {}% a/o {} \ntem um valor de {:.2f} e está custando {}, "
          "e esta {:.2f}% acima do preço justo \nporém com um {:.2f}% de potencial de crescimento "
          "de acordo com os dados fornecidos".format(dividendo, papel, result, price, desconto, earinig_yield))

comperer = str(input("deseja saber sobre outra ação?: "))
if comperer.lower() == 'sim':
    print("ok, vamos lá!")
papel2 = input("Qual é o outro ativo?: ").strip().upper()
price2 = float(input("Qual é o preço?: ").strip().replace(",", "."))
lpa2 = float(input("Qual é o LPA?: ").strip().replace(",", "."))
dividendo2 = float(input("Quantos porcentos de Dividend Yield por ano deseja?: ").strip().replace(",", ".")
                   .replace("%", " "))

# Pergunte ao usuário se deseja calcular a média
ajuda2 = input("Precisa calcular a média de Dividendos pagos nos últimos 4 anos? (sim/não): ").strip()
if ajuda2.lower() == "sim":
    # O usuário deseja calcular a média
    dividendos_ultimos_anos2 = []
    for i in range(1, 5):
        dividendo_ano2 = float(input(f"Digite o dividendo do {i}º ano: ").strip().replace(",", "."))
        dividendos_ultimos_anos2.append(dividendo_ano2)

    # Calcule a média
    dividend2 = sum(dividendos_ultimos_anos2) / len(dividendos_ultimos_anos2)

    # Mostre o resultado
    print(f"A média dos últimos 4 anos é: {dividend2} reais")
else:
    # O usuário não deseja calcular a média
    dividend2 = float(input("Qual é a média de dividendos nos últimos anos então?: ").strip().replace(",", "."))

    div1002 = dividendo2 / 100
    result2 = (dividend2 / div1002)
    diferenca2 = result2 - price2
    earinig_yield2 = (lpa2 / price2) * 100

    if result2 > price2:
        print("\nO valor de acordo com a porcentagem de {}%, que você nos informou,\n"
              "o preço justo para {} é de {:.2f} reais, e com valor de {}, \nisso significa que "
              "o seu preço está {:.3f} R$ abaixo de seu valor. E seu potencial de crecismento no ano é de {:.2f}%"
              .format(dividendo2, papel2, result2, price2, diferenca2, earinig_yield2))
    else:
        print("O preço está muito caro para seus parâmetros,"
              " com um Dividend Yield esperado de {}% a/o {} \ntem um valor de {:.2f} e está custando {}, "
              "\nporém com um {:2f}% de potencial de crescimento "
              "de acordo com os dados fornecidos".format(dividendo2, papel2, result2, price2, earinig_yield2))

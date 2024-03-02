# ⦁ 1	Criar um algoritmo para calcular o valor de y como função de x, segundo a função y(x)=3x+2, em um domínio real.
# ⦁	2   Dados o tamanho de um arquivo (em bits), bem como a velocidade da conexão (em bits por segundo), informe o tempo necessário para o download do arquivo.
# ⦁	3   Criar um algoritmo  que calcule o consumo médio de um automóvel (medido em km/l), dado que são conhecidos a distância total percorrida e o volume de combustível consumido para percorrê-la (medido em litros).
# - 4   Criar um algoritmo  que leia o saldo de uma aplicação e imprimir o novo saldo, considerando um reajuste de 15%.
# ⦁	5   Criar um algoritmo que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.
# ⦁	6   Criar um algoritmo  que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre: 
#           - A idade desta pessoa hoje;
#           - A idade desta pessoa em 2025.
# ⦁	7   Criar um algoritmo  que converta segundos em minutos e segundos. Por exemplo, 252 segundos equivalem a 4 minutos e 12 segundos.
# ⦁	8   Criar um algoritmo que dados dois lados de um triângulo retângulo calcule e exiba a respectiva hipotenusa
# - 9   Faça um algoritmo que receba o número de horas trabalhadas e o valor do salário mínimo. Calcule e mostre o salário a receber seguindo as regras abaixo: 
#           - o valor da hora trabalhada vale a metade do salário mínimo; 
#           - o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada; 
#           - o imposto equivale a 3% do salário bruto; 
#           - o salário a receber equivale ao salário bruto menos o imposto.
# - 10  Faça um algoritmo que receba um número positivo e maior que zero, calcule e mostre:  
#           - o número digitado ao quadrado; 
#           - a raiz quadrada do número digitado; 
# - 11  Pedro comprou um saco de ração com peso em quilos. Pedro possui dois gatos para os quais fornece a quantidade de ração em gramas. Faça um algoritmo que receba o peso do saco de ração e a quantidade de ração fornecida para cada gato por dia. Calcule e mostre quanto restará de ração no saco após cinco dias. 
# - 12  Faça um algoritmo que receba o custo de um espetáculo teatral e o preço do convite deste espetáculo. Esse algoritmo deve calcular e mostrar a quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado.  
# - 13  Faça um algoritmo que receba o peso de uma pessoa em quilos. Calcule e mostre:  
#           - O novo peso se a pessoa engordar 15% sobre o peso digitado; 
#           - O novo peso se a pessoa emagrecer 20% sobre o peso digitado; 
# - 14  Sabe-se que para iluminar de maneira correta os cômodos de uma casa, para cada metro quadrado, deve-se usar 18W de potência. Faça um algoritmo que receba as duas dimensões de um cômodo (em metros). Calcule e mostre a sua área (em m2) e a potência de iluminação que deverá ser utilizada.

from datetime import date
import math

def q1():
    x = float(input("Insira o valor de x:"))
    y = 3*x+2
    print("O valor de y em função de x é: {}".format(y))

def q2():
    tamanhoArquivo = float(input("Tamanho do arquivo: "))
    velocidadeConex = float(input("Velocidade da conexão: "))
    tempoNecessario = tamanhoArquivo/velocidadeConex
    print("Tempo necessário: {} segundos".format(tempoNecessario))
    
def q3():
    distancia = float(input("Distância: "))
    litrosConsumidos = float(input("Litros Consumidos:"))
    kmPorLitro = distancia/litrosConsumidos
    print("Seu carro andou {} Km por litro:".format(kmPorLitro))
    
def q4():
    saldo = float(input("saldo: "))
    percentual = 15
    novoSaldo = saldo+(saldo * (percentual/100))
    print("Saldo Reajustado: {}".format(novoSaldo))
    
def q5():
    salarioAtual = float(input("Salário atual: "))
    percentual = float(input("Percentual: "))
    aumento = salarioAtual*(percentual/100)
    salario_corrigido = salarioAtual+aumento
    print("O novo salário será de R${}, tendo um aumento de R${}".format(salario_corrigido,aumento))

def q6():
    agora = date.today()
    anoAtual = agora.year
    nascimento = int(input("Ano de nascimento: "))    
    print("Esse ano você completa {} anos!\nEm 2025 você terá {} anos!".format(anoAtual-nascimento,2025-nascimento))

def q7():
    inputSegundos = int(input("Insira os Segundos: "))
    minutos = int(inputSegundos/60)
    segundos = inputSegundos%60
    print("minutos: {}\nsegundos: {}".format(minutos,segundos))
    
def q8():
    lado1 = float(input("Lado 1 do triangulo: "))
    lado2 = float(input("Lado 2 do triangulo: "))
    hipotenusa = math.sqrt((lado1**2)+(lado2**2))
    print("Hipotenusa = {:.2f}".format(hipotenusa))

def q9():
    horasTrabalhadas = float(input("Horas trabalhadas: "))
    salarioMinimo = float(input("Salário Minimo: "))
    valorHoraTrabalhada = salarioMinimo/2
    salarioBruto = valorHoraTrabalhada*horasTrabalhadas
    imposto = salarioBruto*0.03
    salarioReceber = salarioBruto-imposto
    print("\n")
    print("Horas Trabalhadas:{}".format(horasTrabalhadas))
    print("Valor da hora trabalhada: R${}".format(valorHoraTrabalhada))
    print("Salario Bruto: R${}".format(salarioBruto))
    print("Imposto:: R${}".format(imposto))
    print("Salario a receber: R${}".format(salarioReceber))

def q10():
    x = 0
    while (x == 0): 
        entrada = int(input("Insira um número positivo: "))
        if entrada > 0:
            x = 1
            print("Número ao quadrado: {}".format(pow(entrada,2)))
            print("Raiz Quadrada: {:.2f}".format(pow(entrada,0.5)))
        else: 
            print("Valor inválido!!\n")
        
def q11():
    pesoSaco = float(input("Insira o peso do saco em Kg: "))
    comidaGato = float(input("Insira a quantidade que o gato come em gramas: "))
    KgToGrama = pesoSaco * 1000
    dias = float(input("Insira o número de dias: "))
    comidaRestante = KgToGrama - (comidaGato * dias)
    print("Ao final de {} dias, sobrarão {} gramas de ração.".format(dias,comidaRestante))

def q12():
    custo = float(input("Custo: "))
    valorIngresso = float(input("Valor do Ingresso: "))
    ingressosVendidos = 0
    rendaIngresso = 0
    while (rendaIngresso < custo):
        ingressosVendidos = ingressosVendidos + 1
        rendaIngresso = valorIngresso*ingressosVendidos
    print("Será preciso vender",ingressosVendidos,"ingressos que darão R$",rendaIngresso,"de renda")
    
def q13():
    peso = float(input("Peso:"))
    percentEngordar = 15
    percentEmagrecer = 20
    valorEngordar = peso*(percentEngordar/100)
    valorEmagrecer = peso*(percentEmagrecer/100)
    
    print("Se você engordar {}%, irá ficar com: {}kg".format(percentEngordar,peso+valorEngordar))
    print("Se você emagrecer {}%, irá ficar com: {}kg".format(percentEmagrecer,peso-valorEmagrecer))
    
def q14():
    dimensao1 = float(input("Lado 1:"))
    dimensao2 = float(input("Lado 2:"))
    metroQuadrado = dimensao2*dimensao1
    potenciaIdealPorMetroQuadrado = 18
    print("Dimensão do comodo: {}".format(metroQuadrado))
    print("Potência ideal: {}".format(metroQuadrado*potenciaIdealPorMetroQuadrado))
resp = ''
while resp != "2":
    validador = 0
    print("\n" * 130)
    questao = input("\nQual questão você quer testar? De 1 a 14: ")
    while validador == 0:
        if int(questao) < 1 or int(questao) > 14:
            print("-"*100)
            questao = input("Essa questão não existe!!\nDigite um número entre 1 e 14: ")
        else:
            validador = 1

    if questao == "1":
        print("\n" * 130)
        print("\nQuestão 1","\n")
        print("Criar um algoritmo para calcular o valor de y como função de x, segundo a função y(x)=3x+2, em um domínio real.\n")
        print("-"*100,"\n")
        q1()
    elif questao == "2":
        print("\n" * 130)
        print("\nQuestão 2","\n")
        print("Dados o tamanho de um arquivo (em bits), bem como a velocidade da conexão (em bits por segundo), informe o tempo necessário para o download do arquivo.\n")
        print("-"*100,"\n")
        q2()
    elif questao == "3":
        print("\n" * 130)
        print("\nQuestão 3","\n")
        print("Criar um algoritmo  que calcule o consumo médio de um automóvel (medido em km/l), dado que são conhecidos a distância total percorrida e o volume de combustível consumido para percorrê-la (medido em litros).\n")
        print("-"*100,"\n")
        q3()
    elif questao == "4":
        print("\n" * 130)
        print("\nQuestão 4","\n")
        print("Criar um algoritmo  que leia o saldo de uma aplicação e imprimir o novo saldo, considerando um reajuste de 15%.\n")
        print("-"*100,"\n")
        q4()
    elif questao == "5":
        print("\n" * 130)
        print("\nQuestão 5","\n")
        print(" Criar um algoritmo que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.\n")
        print("-"*100,"\n")
        q5()
    elif questao == "6":
        print("\n" * 130)
        print("\nQuestão 6","\n")
        print("Criar um algoritmo  que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:")
        print("- A idade desta pessoa hoje")
        print("- A idade desta pessoa em 2025.\n")
        print("-"*100,"\n")
        q6()
    elif questao == "7":
        print("\n" * 130)
        print("\nQuestão 7","\n")
        print(" Criar um algoritmo  que converta segundos em minutos e segundos. Por exemplo, 252 segundos equivalem a 4 minutos e 12 segundos.\n")
        print("-"*100,"\n")
        q7()
    elif questao == "8":
        print("\n" * 130)
        print("\nQuestão 8","\n")
        print(" Criar um algoritmo que dados dois lados de um triângulo retângulo calcule e exiba a respectiva hipotenusa\n")
        print("-"*100,"\n")
        q8()
    elif questao == "9":
        print("\n" * 130)
        print("\nQuestão 9","\n")
        print("Faça um algoritmo que receba o número de horas trabalhadas e o valor do salário mínimo.\n")
        print("-"*100,"\n")
        q9()
    elif questao == "10":
        print("\n" * 130)
        print("\nQuestão 10","\n")
        print("Faça um algoritmo que receba um número positivo e maior que zero, calcule e mostre:")
        print("- o número digitado ao quadrado")
        print("- a raiz quadrada do número digitado\n")
        print("-"*100,"\n")
        q10()
    
    elif questao == "11":
        print("\n" * 130)
        print("\nQuestão 11","\n")
        print("Pedro comprou um saco de ração com peso em quilos. Pedro possui dois gatos para os quais fornece a quantidade de ração em gramas. Faça um algoritmo que receba o peso do saco de ração e a quantidade de ração fornecida para cada gato por dia. Calcule e mostre quanto restará de ração no saco após cinco dias.\n")
        print("-"*100,"\n")
        q11()
    
    elif questao == "12":
        print("\n" * 130)
        print("\nQuestão 12","\n")
        print("Faça um algoritmo que receba o custo de um espetáculo teatral e o preço do convite deste espetáculo. Esse algoritmo deve calcular e mostrar a quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado.\n")
        print("-"*100,"\n")
        q12()   
      
    elif questao == "13":
        print("\n" * 130)
        print("\nQuestão 13","\n")
        
        print("Faça um algoritmo que receba o peso de uma pessoa em quilos. Calcule e mostre:")
        print("- O novo peso se a pessoa engordar 15% sobre o peso digitado")
        print("- O novo peso se a pessoa emagrecer 20% sobre o peso digitado\n")
        print("-"*100,"\n")
        q13()  
        
    elif questao == "14":
        print("\n" * 130)
        print("\nQuestão 14","\n")
        print("Sabe-se que para iluminar de maneira correta os cômodos de uma casa, para cada metro quadrado, deve-se usar 18W de potência. Faça um algoritmo que receba as duas dimensões de um cômodo (em metros). Calcule e mostre a sua área (em m2) e a potência de iluminação que deverá ser utilizada.\n")
        print("-"*100,"\n")
        q14()
        
    print("\n================= MENU ==================")
    resp = input("Continuar = 1\nSair = 2\nR: ")
    if resp == "2":
        print("Encerrado!!")
        

import os

#criar as funções
#função da área do circulo 
def calcular_circulo(raio):
    area = 3.14*raio**2
    return area

#função da área do tringulo
def calcular_triangulo(base, altura):
    area = (base*altura)/2
    return area

#função da área do trapezio
def calcular_trapezio(base1, base2, altura):
    area = ((base1+base2)*altura)/2
    return area

def exibir_menu():
    print('Lista de Calculos Disponíveis:')
    print('1 - para Círculo')
    print('2 - para o Triângulo')
    print('3 - para o Trapézio')
    print('4 ou vazio para Sair')

# programa principal

while True:
    exibir_menu()
    calculo = int(input('Informe o Calculo Desejado: '))
    os.system('cls')

    match calculo:
        case 1:
            raio = float(input('Informe o valor do Raio: '))
            print(f' A Área do Círculo é: {calcular_circulo(raio)}')
            continue
        
        case 2:
            base = float(input('Informe o valor da Base: '))
            altura = float(input('Informe o valor da Altura: '))
            print(f' A Área do Triângulo é: {calcular_triangulo(base,altura)}')
            continue
        
        case 3:
            base1 = float(input('Informe o valor da Primeira Base: '))
            base2 = float(input('Informe o valor da Segunda Base: '))
            altura = float(input('Informe o valor da Altura: '))
            print(f' A Área do Trapézio é: {calcular_trapezio(base1,base2,altura)}')
            continue
        case 4:
            break

        case _:
            print('Opção Invalida')
            continue






              


    

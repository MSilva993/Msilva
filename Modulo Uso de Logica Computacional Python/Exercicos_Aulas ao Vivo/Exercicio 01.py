#Uma empresa quer calcular o salario de seus
#funcionarios com base em sua carga horaria
#semanal e o valor da hora de trabalho
#Alem disso, a empresa oferece um bônus
#de 10% para aqueles funcionarios que
#trabalharem mais de 40 horas por semana 
#e 20% para quem trabalha mais de 100 horas
#e 30% para quem trabalha mais de 200 horas

carga_horaria = int(input("Digite sua carga horária: "))
Valor_hora = float(input("Digite seu valor hora: "))

Salario = carga_horaria * Valor_hora

if carga_horaria > 200:
    Salario = Salario * 1.30
elif carga_horaria > 100:
    Salario = Salario * 1.20 
elif carga_horaria > 40:
    Salario = Salario * 1.10


print(f'Seu Salario é: {Salario}')
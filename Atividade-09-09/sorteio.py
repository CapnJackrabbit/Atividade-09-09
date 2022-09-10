import random


aluno1 = input('Informe o nome do primeiro aluno: ' )
aluno2 = input('Informe o nome do segundo aluno: ' )
aluno3 = input('Informe o nome do terceiro aluno: ' )
aluno4 = input('Informe o nome do quarto aluno: ' )

lista_al = {1: aluno1, 2: aluno2, 3: aluno3, 4: aluno4}

sorteado = random.randrange(1,5)

print ("Quem vai apagar o quadro e o aluno: ", lista_al[sorteado])
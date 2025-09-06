"""9. Crie um dicionário com os nomes de 5 alunos e suas notas. Percorra o dicionário e
imprima apenas os alunos que tiraram nota maior que 7."""

notas_alunos = {'Clara': 6.5, 'Carlos': 7.9, 'Andre': 8.0, 'Ana': 10.00, 'Luiz': 5.00}

for aluno, nota in notas_alunos.items():
  if nota > 7:
    print(f"Aluno: {aluno} - nota: {nota}")
              
            

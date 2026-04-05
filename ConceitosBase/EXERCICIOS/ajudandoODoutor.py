# O programa deve pedir a nota e aprovar os alunos que possum nota maior do que 8,5.
# Peça e-mail e nota do aluno
# Utilize um IF simples

email = str(input("Esta ferramenta realiza a validação de notas na disciplina de Arqueologia do Dr. Henry J. Jr.\nAqueles com nota MAIOR que 8,5 receberão o convite para a visita de campo na América do Sul\n\nDigite seu e-mail: "))
nota = float(input("Digite a sua última nota: "))

if nota > 8.5:
    # print("Nota válida. O convite foi enviado para o e-mail: {}".format(email))
    print(f"Nota válida. O convite foi enviado para o e-mail: {email}")

# else:
#     print("Você não é elegível para receber o convite.")
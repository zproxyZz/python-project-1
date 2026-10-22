turma = ""
nome = ""
idade = 0
aprovado = True
situacao = ""
numero_aluno = 1

print("diga a turma:")
turma = input()

continuar = True

while continuar:
    print("\nagora, diga o nome do aluno", numero_aluno)
    nome = input()

    print("qual a idade de", nome, "?")
    idade = input()

    while True:
        print("este aluno(a) foi aprovado?(sim ou não)")
        resposta = input().lower()

        if resposta == "sim":
            aprovado = True
            break
        elif resposta == "não":
            aprovado = False
            break
        else:
            aprovado = False
            print("resposta não reconhecida")

    if aprovado:
        situacao = "aprovado"
    elif not aprovado:
        situacao = "não aprovado"

    print("\nresumo do aluno", numero_aluno, "da turma", turma, ":", "\n", nome, "\n", idade, "\n", situacao)

    print("\nDeseja cadastrar outro aluno nesta turma? (sim ou não)")
    resposta_continuar = input().lower()


    numero_aluno += 1

    if resposta_continuar == "sim":
        continuar = True
        print("\nsiga com as informações do próximo aluno")
    elif resposta_continuar == "não":
        continuar = False
        print("Cadastro da turma", turma, "finalizado!")
    else:
        continuar = False
        print("Palavra não reconhecida. Cadastro encerrado!")


from time import sleep

print("--------------------------------------------------------------")

team_name = input("Nome da equipe: ")

subareas = ["Aerodinâmica", "Eletrônica", "Estruturas", "Propulsão", "Recuperação"]
subarea_member_select = 0
subarea_select = 0
problem_select = 0

print("--------------------------------------------------------------")

def selectSubarea(message):
    global subareas
    print(message)
    for i, subarea in enumerate(subareas, 1):
        print(f"[ {i} ] {subarea}")
    print("--------------------------------------------------------------")

    while True:
        try:
            selection = int(input("Selecione a opção: "))
            if 1 <= selection <= len(subareas):
                print("--------------------------------------------------------------")
                return selection
            else:
                print("Seleção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def subareaMember():
    global subarea_member_select
    subarea_member_select = selectSubarea("Sua subárea de atuação")
    print(f"Subárea do usuário: {subareas[subarea_member_select - 1]}")
    print("--------------------------------------------------------------")

def subareaProblem():
    global subarea_select
    subarea_select = selectSubarea("Qual das subáreas falhou no voo?")
    print(f"Subárea selecionada: {subareas[subarea_select - 1]}")
    print("--------------------------------------------------------------")

def problemAnalysi():
    global problem_select

    problem_options = {
        1: [
            "Alto ângulo de ataque.",
            "Falta de estabilidade durante o voo.",
            "Super estabilidade durante o voo."
        ],
        2: [
            "Não houve leitura por parte do sensor barométrico.",
            "Os dados não foram armazenados no micro SD.",
            "A recuperação do foguete não foi ativada."
        ],
        3: [
            "Estrutura sofreu danos durante o voo.",
            "Falha na conexão entre componentes estruturais.",
            "Deformação durante a decolagem."
        ],
        4: [
            "Falha no motor.",
            "Propulsor não atingiu o desempenho esperado.",
            "Problema na ignição."
        ],
        5: [
            "Paraquedas não abriu corretamente.",
            "Sistema de recuperação falhou.",
            "Impacto mais forte do que o esperado."
        ]
    }

    while True:
        print("O que ocorreu durante o voo?")
        for i, option in enumerate(problem_options[subarea_select], 1):
            print(f"[ {i} ] {option}")

        print("--------------------------------------------------------------")

        try:
            problem_select = int(input("Selecione a opção: "))
            if 1 <= problem_select <= len(problem_options[subarea_select]):
                print(f"Falha selecionada: n° {problem_select}")
                print("--------------------------------------------------------------")
                print("Possível solução:")
                if subarea_select == 1:
                    print("- Verifique os dados aerodinâmicos do foguete na simulação e veja se a parte física está coincidindo.")
                elif subarea_select == 2:
                    print("- Verifique as conexões do sensor e o código de armazenamento.")
                elif subarea_select == 3:
                    print("- Reforce a estrutura e revise o design para evitar deformações.")
                elif subarea_select == 4:
                    print("- Verifique o motor e a mistura de combustível.")
                elif subarea_select == 5:
                    print("- Inspecione o paraquedas e o sistema de recuperação para garantir funcionamento correto.")
                break
            else:
                print("Seleção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    print("--------------------------------------------------------------")

def usageReport():
    pass  # Implement usage reporting functionality here

subareaMember()
sleep(1)

subareaProblem()
sleep(1)

problemAnalysi()

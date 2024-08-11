# Open Cause
# Software para análise de problemas na área de foguete modelismo

# Implementações - 0.1
# Mudar a lógica de exibição da análise e possível solução.
# Implementar a função de relatório de uso

from time import sleep

print("--------------------------------------------------------------")

team_name = str(input("Nome da equipe: "))

subarea_name = ["Aerodinâmica", "Eletrônica", "Estruturas", "Propulsão", "Recuperação"]
subarea_member_select = 0
subarea_select = 0
problem_select = 0

problemsList = {
    1: [
        "[ 1 ] Alto ângulo de ataque.",
        "[ 2 ] Falta de estabilidade durante o voo.", 
        "[ 3 ] Super estabilidade durante o voo."
        ],

    2: [
        "[ 1 ] Não houve leitura por parte do sensor barométrico.", 
        "[ 2 ] Os dados não foram armazenados no micro SD.", 
        "[ 3 ] O quibe não foi ativado."
        ],

    3: [
        "", 
        "", 
        ""
        ],

    4: [
        "", 
        "", 
        ""
        ],

    5: [
        "", 
        "", 
        ""
        ]
}

resolutionList = {
    1: [
        "", 
        "", 
        ""
        ],

    2: [
        "", 
        "", 
        ""
        ],

    3: [
        "", 
        "", 
        ""
        ],

    4: [
        "", 
        "", 
        ""
        ],

    5: [
        "", 
        "", 
        ""
        ]
}

print("--------------------------------------------------------------")

def subareaMember():
    global subarea_name, subarea_member_select

    while(subarea_member_select < 1 or subarea_member_select > 5):
        print("Sua subárea de atuação")
        print("[ 1 ] Aerodinâmica")
        print("[ 2 ] Eletrônica")
        print("[ 3 ] Estruturas")
        print("[ 4 ] Propulsão")
        print("[ 5 ] Recuperação")

        print("--------------------------------------------------------------")

        subarea_member_select = int(input("Selecione: "))

        print("--------------------------------------------------------------")

        if(subarea_member_select >= 1 and subarea_member_select <= 5):
            print(f"Subárea do usuário: {subarea_name[subarea_member_select - 1]}")
            
            break

    print("--------------------------------------------------------------")

def subareaProblem():
    global subarea_name, subarea_select

    while(subarea_select < 1 or subarea_select > 5):
        print("Qual das subáreas falhou no voo?")
        print("[ 1 ] Aerodinâmica")
        print("[ 2 ] Eletrônica")
        print("[ 3 ] Estruturas")
        print("[ 4 ] Propulsão")
        print("[ 5 ] Recuperação")

        print("--------------------------------------------------------------")

        subarea_select = int(input("Selecione a subárea: "))

        print("--------------------------------------------------------------")

        if(subarea_select >= 1 and subarea_select <= 5):
            print(f"Subárea selecionada: {subarea_name[subarea_select - 1]}")
            
            break

    print("--------------------------------------------------------------")

def problemAnalysi():
    
    def aeroProblem():
        global problem_select

        while (problem_select < 1 or problem_select > 3):
            print("O que ocorreu durante o voo?")
            print("[ 1 ] Alto ângulo de ataque.")
            print("[ 2 ] Falta de estabilidade durante o voo.")
            print("[ 3 ] Super estabilidade durante o voo.")

            print("--------------------------------------------------------------")

            problem_select = int(input("Selecione a opção: "))

            print("--------------------------------------------------------------")

            if(problem_select >= 1 and problem_select <= 3):

                print(f"Falha selecionada: n° {problem_select}")

                print("--------------------------------------------------------------")

                print("Possível solução:")
                print("- Verifique os dados aerodinâmicos do foguete na")
                print("simulação e veja se a parte física está coincidindo.")
            
                break

        print("--------------------------------------------------------------")


    def eletronicProblem():
        global problem_select

        while (problem_select < 1 or problem_select > 3):
            print("O que ocorreu durante o voo?")
            print("[ 1 ] Não houve leitura por parte do sensor barométrico.")
            print("[ 2 ] Os dados não foram armazenados no micro SD.")
            print("[ 3 ] O quibe não foi ativado")

            print("--------------------------------------------------------------")

            problem_select = int(input("Selecione a opção: "))

            print("--------------------------------------------------------------")

            if(problem_select >= 1 and problem_select <= 3):
                
                print(f"Falha selecionada: n° {problem_select}")
            
                print("--------------------------------------------------------------")

                print("Possível solução:")
                print("- Verifique as conexões entre o microcontrolador e ")
                print("e o arduino, além disso, analise de forma mais minuciosa.")
                print("a parte do código responsável pelo micro sd.")

                break

        print("--------------------------------------------------------------")

    def structureProblem():
        global problem_select

        while (problem_select < 1 or problem_select > 3):
            print("O que ocorreu durante o voo?")
            print("[ 1 ] Fuselagem rachou durante o voo")
            print("[ 2 ] Suporte da eletrônica sofreu dano")
            print("[ 3 ] Fuselagem não ficou firme.")

            print("--------------------------------------------------------------")

            problem_select = int(input("Selecione a opção: "))

            print("--------------------------------------------------------------")

            if(problem_select >= 1 and problem_select <= 3):
                print(f"Falha selecionada: n° {problem_select}")

                print("--------------------------------------------------------------")

                print("Possível solução:")
                print("- Verifique o processo de produção da fuselagem")
                print("pois é provavel que exista falhas e camadas finas,")
                print("e verifique a fixação dos suportes, pois podem estar")
                print("influênciando de maneira direta na compisição estrutural.")
            
                break

        print("--------------------------------------------------------------")
    
    def propProblem():
        global problem_select

        while (problem_select < 1 or problem_select > 3):
            print("O que ocorreu durante o voo?")
            print("[ 1 ] O apogeu não foi alcançado.")
            print("[ 2 ] A tubeira rachou.")
            print("[ 3 ] O motor explodiu.")

            print("--------------------------------------------------------------")

            problem_select = int(input("Selecione a opção: "))

            print("--------------------------------------------------------------")

            if(problem_select >= 1 and problem_select <= 3):
                print(f"Falha selecionada: n° {problem_select}")

                print("--------------------------------------------------------------")

                print("Possível solução:")
                print("- É BOLSONARO OU NÃO É?!")
                print("ÉÉÉÉÉÉÉÉÉÉÉÉÉÉÉÉÉÉÉÉÉÉÉÉÉÉÉÉÉÉÉ")
            
                break

        print("--------------------------------------------------------------")

    def recProblem():
        global problem_select
        
        while (problem_select < 1 or problem_select > 3):
            print("O que ocorreu durante o voo?")
            print("[ 1 ] Pouca desaceleração")
            print("[ 2 ] Cordas enrroscando")
            print("[ 3 ] Paraquedas não foi totalmente ejetado")

            print("--------------------------------------------------------------")

            problem_select = int(input("Selecione a opção: "))

            print("--------------------------------------------------------------")

            if(problem_select >= 1 and problem_select <= 3):
                print(f"Falha selecionada: n° {problem_select}")

                print("--------------------------------------------------------------")

                print("Possível solução:")
                print("- Essa parada aí mesmo que tu pensou, Boia, gênio!")
            
                break

        print("--------------------------------------------------------------")
    
    if(subarea_select == 1):
        aeroProblem()

    if(subarea_select == 2):
        eletronicProblem()

    if(subarea_select == 3):
        structureProblem()

    if(subarea_select == 4):
        propProblem()

    if(subarea_select == 5):
        recProblem()


def usageReport():
    print("")

subareaMember()

sleep(5)

subareaProblem()

sleep(5)

problemAnalysi()

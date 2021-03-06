# encoding: utf-8

#GERANDO OS VERTICES DIAS DA SEMANA
semana = []
'''
MODELO DOS DADOS DO VERTICE DIAS DA SEMANA
{
    "Nome" : "Dia",
    "Dados": {
        "Aulas": [None* Numero de aulas no dia],
        "ProfessoresDisponiveis" : [Professor1, Professor2]
    }
}
'''
def define_semana():
    semana.append({"Nome": "Segunda",   "Dados": {"Aulas": [], "ProfessoresDisponiveis": ["Faulin", "Cesar","Eloiza"]}})
    semana.append({"Nome": "Terca",     "Dados": {"Aulas": [], "ProfessoresDisponiveis": ["Ettore", "Victor"]}})
    semana.append({"Nome": "Quarta",    "Dados": {"Aulas": [], "ProfessoresDisponiveis": ["Cesar", "Victor", "Ettore"]}})
    semana.append({"Nome": "Quinta",    "Dados": {"Aulas": [], "ProfessoresDisponiveis": ["Victor", "Faulin"]}})
    semana.append({"Nome": "Sexta",     "Dados": {"Aulas": [], "ProfessoresDisponiveis": ["Cleber", "Ettore"]}})

define_semana()

#GERANDO OS VERTICES PROFESSORES
professores = []
'''
MODELO DOS DADOS DO VERTICE DOS PROFESSORES
{
    "Nome": "NomeDoProfessor",
    "Dados": {
        "DaAulaDe": [Aula1, Aula2],
        "DiasDisponiveis": {
            "Dia1": [Intervalo de tempo disponível],
            "Dia2": [Intervalo de tempo disponível]
        }
    }
}
'''
def define_professores():
    professores.append({"Nome": "Eloiza",   "Dados": {"DaAulaDe": {"Ingles": 2}, "DiasDisponiveis": {"Segunda": [1,2,3,4]}}})
    professores.append({"Nome": "Faulin",   "Dados": {"DaAulaDe": {"Manejo": 2}, "DiasDisponiveis": {"Segunda": [3,4], "Quinta": [1,2]}}})
    professores.append({"Nome": "Ettore",   "Dados": {"DaAulaDe": {"Redes": 4}, "DiasDisponiveis": {"Terca": [1,2,3,4], "Quarta": [1,2], "Sexta": [3,4]}}})
    professores.append({"Nome": "Cesar",    "Dados": {"DaAulaDe": {"Empreendedorismo": 2}, "DiasDisponiveis": {"Segunda": [1,2,3,4], "Quarta": [1,2]}}})
    professores.append({"Nome": "Victor",   "Dados": {"DaAulaDe": {"Algoritmos": 6}, "DiasDisponiveis": {"Terca": [1,2,3,4], "Quarta": [1,2,3,4], "Quinta": [1,2,3,4]}}})
    professores.append({"Nome": "Cleber",   "Dados": {"DaAulaDe": {"WebSemantica": 4}, "DiasDisponiveis": {"Sexta": [1,2,3,4]}}})

define_professores()

#GERANDO OS VERTICES MATERIAS
materias = []
'''
{
    "Nome": "NomeDaMateria",
    "Dados": {
        "ProfessoresDisponiveis": ["Professor1", "Professor2"]
        "NumeroDeAulas": x
    }
}
'''
def define_materias():
    materias.append({"Nome": "Ingles",              "Dados": {"ProfessoresDisponiveis": ["Eloiza"], "NumeroDeAulas": 2}})
    materias.append({"Nome": "Manejo",              "Dados": {"ProfessoresDisponiveis": ["Faulin"], "NumeroDeAulas": 2}})
    materias.append({"Nome": "Redes",               "Dados": {"ProfessoresDisponiveis": ["Ettore"], "NumeroDeAulas": 4}})
    materias.append({"Nome": "Algoritmos",          "Dados": {"ProfessoresDisponiveis": ["Victor"], "NumeroDeAulas": 6}})
    materias.append({"Nome": "Empreendedorismo",    "Dados": {"ProfessoresDisponiveis": ["Cesar"], "NumeroDeAulas": 2}})
    materias.append({"Nome": "WebSemantica",        "Dados": {"ProfessoresDisponiveis": ["Cleber"], "NumeroDeAulas": 4}})

define_materias()

def busca_professor(professor):
    res = [prof for prof in professores if prof['Nome'] is professor]
    return res.pop()

def busca_dia(dia):
    res = [day for day in semana if day['Nome'] is dia]
    return res.pop()
    

def busca_materia(materia):
    res = [mat for mat in materias if mat['Nome'] is materia]
    return res.pop()

def agendar_aula(dia, profs):
    objDiaDaSemana = busca_dia(dia)
    for i in profs:
        objMateria = melhor_materia_do_professor(i['Nome'])
        for j in range(objMateria['Dados']['NumeroDeAulas']):
            if len(objDiaDaSemana['Dados']['Aulas']) >= 4:
                break
            objDiaDaSemana['Dados']['Aulas'].append(objMateria['Nome'])
            objMateria['Dados']['NumeroDeAulas'] -= 1
        # del i['Dados']['DaAulaDe'][matAux['Nome']]
        # diaAux['Dados']['ProfessoresDisponiveis'].remove(i['Nome'])

# def professores_disponiveis_no_dia(dia):
#     res = []
#     for day in semana:
#         if day['Nome'] == dia:
#             for row in day['Dados']['ProfessoresDisponiveis']:
#                 res.append(busca_professor(row))
#     return res

# def dias_disponiveis_do_professor(professor):
#     res = []
#     for prof in professores:
#         if prof['Nome'] == professor:
#             for row in prof['Dados']['DiasDisponiveis']:
#                 res.append(busca_dia(row))
#     return res

def melhor_materia_do_professor(professor):
    profAux = busca_professor(professor)
    res = []
    if len(profAux['Dados']['DaAulaDe']) == 1:
        for materia in profAux['Dados']['DaAulaDe']:
            return busca_materia(materia)
    for row in profAux['Dados']['DaAulaDe']:
        materiaAux = busca_materia(row)
        try:
            if len(res[0]['Dados']['ProfessoresDisponiveis']) > len(materiaAux['Dados']['ProfessoresDisponiveis']):
                res.insert(0, materiaAux)
        except:
            res.insert(0, materiaAux)
    return res.pop()

def buscar_professores_do_dia(_nome_dia):
    dia = busca_dia(_nome_dia)
    professores_disponiveis = []

    # Separa array de professores
    for nome_professor in dia['Dados']['ProfessoresDisponiveis']:
        professores_disponiveis.append(busca_professor(nome_professor))
    
    # Ordena professores do dia por quem tem menor disponibilidade e seleciona até que preencha as 4 aulas
    qtde_aulas = 0
    professores_escolhidos = []

    for professor in sorted(professores_disponiveis, key=lambda k: len(k['Dados']['DiasDisponiveis'])):
        materia = melhor_materia_do_professor(professor['Nome'])
        
        if qtde_aulas < 4:
            professores_escolhidos.append(professor)

        qtde_aulas += materia['Dados']['NumeroDeAulas']
        
    return professores_escolhidos

# def buscar_dias_adjacentes_ao_prof(prof):
#     return []

dias_visitados = []

def pega_um_dia_nao_visitado_de_grafo_desconexo():
    
    for dia in semana:
        if dia['Nome'] not in dias_visitados:
            return dia
    
    return False

def busca_em_largura_do_dia(dia_inicial):
    dias_nao_visitados = [dia_inicial['Nome']]
    
    while len(dias_nao_visitados):

        dias_visitados.append(dias_nao_visitados[0]) # Adiciona dia aos visitados
        professores_escolhidos = buscar_professores_do_dia(u''+dias_nao_visitados[0])
        agendar_aula(dias_nao_visitados[0], professores_escolhidos)

        dia = busca_dia(dias_nao_visitados[0])

        dias_nao_visitados.pop(0)

        # Pega um array de objetos de professor, só pra ordenar
        professores_disponiveis = []
        for nome_professor in dia['Dados']['ProfessoresDisponiveis']:
            professores_disponiveis.append(busca_professor(nome_professor))

        # Considera buscar os adjacentes do professor com a mesma ordem de critério
        for prof in sorted(professores_disponiveis, key=lambda k: len(k['Dados']['DiasDisponiveis'])):
            dias_adjacentes = prof['Dados']['DiasDisponiveis'] # vai dar erro aqui
            # dias_adjacentes = buscar_dias_adjacentes_ao_prof(prof) # Retorna vértices adjacentes, remove da lista de busca
        
            for prox_dia in dias_adjacentes:
                if prox_dia not in dias_visitados and prox_dia not in dias_nao_visitados: # Para cada adjacente não visitado, acrescenta na lista
                    dias_nao_visitados.append(prox_dia)

    dia_desconexo = pega_um_dia_nao_visitado_de_grafo_desconexo()
    if dia_desconexo:
        busca_em_largura_do_dia(dia_desconexo)

def limpa_grafo_inicial():
    
    del dias_visitados[:]
    del semana[:]
    define_semana()
    del professores[:]
    define_professores()
    del materias[:]
    define_materias()

gaps = []

def valida_resultado():

    del gaps[:]
    resultado = True

    for dia in semana:
        if (len(dia['Dados']['Aulas']) < 4):
            gaps.append(dia)
            resultado = False

    for materia in materias:
        if (materia['Dados']['NumeroDeAulas'] > 0):
            gaps.append(materia)
            resultado = False

    return resultado

def montar_grade():

    for dia in semana:
        busca_em_largura_do_dia(dia)

        if valida_resultado():
            print(semana)
            break

        if len(gaps):
            print('GAPS (' + str(dia["Nome"]) + ')\n')
            print(gaps)

        limpa_grafo_inicial()




#print(professores_disponiveis("Segunda"))

#print(professores_disponiveis_no_dia('Segunda'))
#print(melhor_materia_do_professor('Victor'))
#print(melhor_professor_no_dia('Terca'))

montar_grade()
#print(melhor_materia_do_professor(professores[0]['Nome']))
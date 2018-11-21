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
semana.append({"Nome": "Segunda",   "Dados": {"Aulas": [], "ProfessoresDisponiveis": ["Eloiza", "Faulin", "Cesar"]}})
semana.append({"Nome": "Terça",     "Dados": {"Aulas": [], "ProfessoresDisponiveis": ["Ettore", "Victor"]}})
semana.append({"Nome": "Quarta",    "Dados": {"Aulas": [], "ProfessoresDisponiveis": ["Cesar", "Victor", "Ettore"]}})
semana.append({"Nome": "Quinta",    "Dados": {"Aulas": [], "ProfessoresDisponiveis": ["Victor", "Faulin"]}})
semana.append({"Nome": "Sexta",     "Dados": {"Aulas": [], "ProfessoresDisponiveis": ["Cleber", "Ettore"]}})

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
professores.append({"Nome": "Eloiza",   "Dados": {"DaAulaDe": {"Ingles": 2}, "DiasDisponiveis": {"Segunda": [1,2,3,4]}}})
professores.append({"Nome": "Faulin",   "Dados": {"DaAulaDe": {"Manejo": 2}, "DiasDisponiveis": {"Segunda": [3,4], "Quinta": [1,2]}}})
professores.append({"Nome": "Ettore",   "Dados": {"DaAulaDe": {"Redes": 4}, "DiasDisponiveis": {"Terça": [1,2,3,4], "Quarta": [1,2], "Sexta": [3,4]}}})
professores.append({"Nome": "Cesar",    "Dados": {"DaAulaDe": {"Empreendedorismo": 2}, "DiasDisponiveis": {"Segunda": [1,2,3,4], "Quarta": [1,2]}}})
professores.append({"Nome": "Victor",   "Dados": {"DaAulaDe": {"Algoritmos": 6}, "DiasDisponiveis": {"Terça": [1,2,3,4], "Quarta": [1,2,3,4], "Quinta": [1,2,3,4]}}})
professores.append({"Nome": "Cleber",   "Dados": {"DaAulaDe": {"WebSemantica": 4}, "DiasDisponiveis": {"Sexta": [1,2,3,4]}}})

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
materias.append({"Nome": "Ingles",              "Dados": {"ProfessoresDisponiveis": ["Eloiza"], "NumeroDeAulas": 2}})
materias.append({"Nome": "Manejo",              "Dados": {"ProfessoresDisponiveis": ["Faulin"], "NumeroDeAulas": 2}})
materias.append({"Nome": "Redes",               "Dados": {"ProfessoresDisponiveis": ["Ettore"], "NumeroDeAulas": 4}})
materias.append({"Nome": "Algoritmos",          "Dados": {"ProfessoresDisponiveis": ["Victor"], "NumeroDeAulas": 6}})
materias.append({"Nome": "Empreendedorismo",    "Dados": {"ProfessoresDisponiveis": ["Cesar"], "NumeroDeAulas": 2}})
materias.append({"Nome": "WebSemantica",        "Dados": {"ProfessoresDisponiveis": ["Cleber"], "NumeroDeAulas": 4}})

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
    diaAux = busca_dia(dia)
    for i in profs:
        matAux = melhor_materia_do_professor(i['Nome'])
        for j in range(matAux['Dados']['NumeroDeAulas']):
            if len(diaAux['Dados']['Aulas']) >= 4:
                break
            diaAux['Dados']['Aulas'].append(matAux['Nome'])
            matAux['Dados']['NumeroDeAulas'] -= 1
        # del i['Dados']['DaAulaDe'][matAux['Nome']]
        # diaAux['Dados']['ProfessoresDisponiveis'].remove(i['Nome'])

def professores_disponiveis_no_dia(dia):
    res = []
    for day in semana:
        if day['Nome'] == dia:
            for row in day['Dados']['ProfessoresDisponiveis']:
                res.append(busca_professor(row))
    return res

def dias_disponiveis_do_professor(professor):
    res = []
    for prof in professores:
        if prof['Nome'] == professor:
            for row in prof['Dados']['DiasDisponiveis']:
                res.append(busca_dia(row))
    return res

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

def melhor_professor_no_dia(dia):
    day = busca_dia(dia)
    possivel_professor = []
    for row in day['Dados']['ProfessoresDisponiveis']:
        profAux = busca_professor(row)
        try:
            print(len(possivel_professor[0]['Dados']['DiasDisponiveis']), len(profAux['Dados']['DiasDisponiveis']))
            if len(possivel_professor[0]['Dados']['DiasDisponiveis']) <= len(profAux['Dados']['DiasDisponiveis']):
                print(profAux['Nome'])
                possivel_professor.append(profAux)
        except:
            possivel_professor.append(profAux)
    return possivel_professor




def montar_grade():
    for dias in semana:
        profsDisponiveis = melhor_professor_no_dia(dias['Nome'])
        contador = 0
        profsEscolhidos = []
        for i in profsDisponiveis:
            matAjudante = melhor_materia_do_professor(i['Nome'])
            if contador >= 4:
                break
            contador += matAjudante['Dados']['NumeroDeAulas']
            profsEscolhidos.append(i)
        agendar_aula(dias['Nome'], profsEscolhidos)
    print(semana)


#print(professores_disponiveis("Segunda"))

#print(professores_disponiveis_no_dia('Segunda'))
#print(melhor_materia_do_professor('Victor'))
#print(melhor_professor_no_dia('Terça'))

montar_grade()
#print(melhor_materia_do_professor(professores[0]['Nome']))
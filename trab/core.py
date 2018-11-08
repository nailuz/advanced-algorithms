from operator import attrgetter

week = []

week.append({"Dia": "Segunda","Aulas":  [None, None, None, None]})
week.append({"Dia": "Terça","Aulas":    [None, None, None, None]})
week.append({"Dia": "Quarta","Aulas":   [None, None, None, None]})
week.append({"Dia": "Quinta","Aulas":   [None, None, None, None]})
week.append({"Dia": "Segunda","Aulas":  [None, None, None, None]})

teachers = []
teachers.append({"Nome": "Eloiza", "Disponibilidade": ["Segunda", "Terça", "Sexta"], "Aulas": 2})
teachers.append({"Nome": "Faulin", "Disponibilidade": ["Segunda", "Terça"], "Aulas": 2})
teachers.append({"Nome": "Ettore", "Disponibilidade": ["Terça", "Sexta"], "Aulas": 4})
teachers.append({"Nome": "Cesar", "Disponibilidade": ["Quarta", "Quinta", "Sexta"], "Aulas": 2})
teachers.append({"Nome": "Victor", "Disponibilidade": ["Quarta", "Quinta"], "Aulas": 6})
teachers.append({"Nome": "Cleber", "Disponibilidade": ["Sexta"], "Aulas": 4})

def pick_day(day):
    for row in week:
        if day == row["Dia"]:
            return row

def pick_teacher(name):
    for row in teachers:
        if name == row["Nome"]:
            return row

def day_by_teacher(day):
    response = []
    for row in teachers:
        if day in row["Disponibilidade"]:
            response.append(row["Nome"])
    return response

def core(day):
    helper = []
    the_teachers = day_by_teacher(day)
    sorted(the_teachers, key=lambda classes: len(pick_teacher(the_teachers)["Disponibilidade"]))

for row in week:
    print(row)

print(day_by_teacher("Segunda"))
the_teachers = day_by_teacher("Segunda")
sorted(the_teachers, key=lambda aux: len(pick_teacher(aux)["Disponibilidade"]))
print(len(pick_teacher("Eloiza")["Disponibilidade"]))
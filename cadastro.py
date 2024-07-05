import sqlite3
from models import CreatePeople, UpdatePeople, CreateAddres
from datetime import datetime



def insert_people(pessoa : CreatePeople):
    conn = sqlite3.connect("package.db")
    agora = datetime.now().strftime('%Y-%m-%d %H:%M')
    cursor = conn.cursor()
    query = "INSERT INTO people (name,fk_addres,fk_graduation,birth_date,email,phone,cpf,is_student,is_teacher,created_at) VALUES (?,?,?,?,?,?,?,?,?,?);"
    cursor.execute(query,(pessoa.name,pessoa.fk_addres,pessoa.fk_graduation,pessoa.birth_date,pessoa.email,pessoa.phone,pessoa.cpf,pessoa.is_student,pessoa.is_teacher,agora))
    conn.commit()
    conn.close()


def read_last_registration():
    conn = sqlite3.connect("package.db")
    cursor = conn.cursor()
    query = "SELECT * FROM people ORDER BY ROWID DESC LIMIT 1;" 
    cursor.execute(query)
    last_registro = cursor.fetchone()
    conn.close()

    if last_registro:
        return CreatePeople(name=last_registro[1], fk_addres=str(last_registro[2]), fk_graduation=str(last_registro[3]), birth_date=last_registro[4], email=last_registro[5], phone=str(last_registro[6]), cpf=str(last_registro[7]), is_student=last_registro[8], is_teacher=last_registro[9])  
    else:
        return "Erro ao cadastrar"   


def query_by_name(name: str) -> CreatePeople:
    conn = sqlite3.connect("package.db")
    cursor = conn.cursor()
    query = "SELECT * FROM people WHERE name = ?;"
    cursor.execute(query, (name,))
    results = cursor.fetchone()
    conn.close()

    if results:    
        return CreatePeople(name=results[1], fk_addres=str(results[2]), fk_graduation=str(results[3]), birth_date=results[4], email=results[5], phone=str(results[6]), cpf=str(results[7]), is_student=results[8], is_teacher=results[9])
    else:
        return "Nenhum cadastro"
    

def change_registration(id: int, pessoa : CreatePeople):
    conn = sqlite3.connect("package.db")
    agora = datetime.now().strftime('%Y-%m-%d %H:%M')
    cursor = conn.cursor()
    query = "UPDATE people SET name = ?, fk_addres = ?, fk_graduation = ?, birth_date = ?, email = ?, phone = ?, cpf = ?, is_student = ?, is_teacher = ?,updated_at = ? WHERE id = ?; "    
    cursor.execute(query, (pessoa.name,pessoa.fk_addres,pessoa.fk_graduation,pessoa.birth_date,pessoa.email,pessoa.phone,pessoa.cpf,pessoa.is_student,pessoa.is_teacher,agora, id ))

    conn.commit()
    conn.close()


def partially_registration(id: int, pessoa : UpdatePeople):
    conn = sqlite3.connect("package.db")
    cursor = conn.cursor()
    filters = []
    variables = []

    if pessoa.name is not None:
        filters.append(f"name= ?")
        variables.append(pessoa.name)

    if pessoa.fk_addres is not None:
        filters.append(f"fk_addres= ?")
        variables.append(pessoa.fk_addres)

    if pessoa.fk_graduation is not None:
        filters.append(f"fk_graduation= ?")
        variables.append(pessoa.fk_graduation)
    
    if pessoa.birth_date is not None:
        filters.append(f"birth_date= ?")
        variables.append(pessoa.birth_date)

    if pessoa.email is not None:
        filters.append(f"email= ?")
        variables.append(pessoa.email)

    if pessoa.phone is not None:
        filters.append(f"phone= ?")
        variables.append(pessoa.phone)            

    if pessoa.cpf is not None:
        filters.append(f"cpf= ?")
        variables.append(pessoa.cpf) 

    if pessoa.is_student is not None:
        filters.append(f"is_student= ?")
        variables.append(pessoa.is_student)

    if pessoa.is_teacher is not None:
        filters.append(f"is_teacher= ?")
        variables.append(pessoa.is_teacher)

    
    agora = datetime.now().strftime('%Y-%m-%d %H:%M')
    filters.append("updated_at = ?")
    variables.append(agora) 

    variables.append(id)

    filters_set = ",".join(filters)

    query = f"UPDATE people SET {filters_set} WHERE id = ?;"
    cursor.execute(query, variables)

    conn.commit()
    conn.close()             


def delete_registration(id):
    conn = sqlite3.connect("package.db")
    cursor = conn.cursor()
    query = "DELETE FROM people WHERE id = ?;"
    cursor.execute(query, (id,))
    
    conn.commit()
    conn.close()


def insert_addres(endereco : CreateAddres):
    conn = sqlite3.connect("package.db")
    agora = datetime.now().strftime('%Y-%m-%d %H:%M')
    cursor = conn.cursor()
    query = "INSERT INTO addresses (state,city,street,created_at,updated_at) VALUES (?,?,?,?,?);"
    cursor.execute(query,(endereco.state,endereco.city,endereco.street,agora,agora))
    conn.commit()
    conn.close()


def read_last_addres():
    conn = sqlite3.connect("package.db")
    cursor = conn.cursor()
    query = "SELECT * FROM addresses ORDER BY ROWID DESC LIMIT 1;"
    cursor.execute(query)
    last_addres = cursor.fetchone()
    conn.close()

    if last_addres:
        return CreateAddres(state=last_addres[1],city=last_addres[2],street=last_addres[3])
    else:
        return "Nenhum endereço cadastrado"
    



# id,state,city,street,created_at,updated_at
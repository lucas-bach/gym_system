from fastapi import FastAPI
import uvicorn
from typing import List
from cadastro import insert_people, read_last_registration,insert_addres,query_by_name,change_registration,partially_registration,delete_registration,read_last_addres,query_addres_id,update_addres,part_addres,delete_addres,insert_graduation,read_last_graduation,query_by_color,change_graduation,part_graduation,delete_graduation
from models import CreatePeople, UpdatePeople,CreateAddres,UpdateAddres,CreateGraduation,UpdateGraduation

app = FastAPI()



@app.post("/create_cad", tags=["Cadastro"])
def create(pessoa : CreatePeople):
    insert_people(pessoa)
    return read_last_registration()


# @app.get("/last_registration", tags=["Cadastro"])
# def last_reg(pessoa : CreatePeople):
#     read_last_registration()
#     return(pessoa)

@app.get("/query_by_name/{name}", tags=["Cadastro"])
def query_name(name: str) -> CreatePeople:         
    return query_by_name(name) 


@app.put("/update/{id}", tags=["Cadastro"])
def to_update(id: int, pessoa : CreatePeople):
    change_registration(id,pessoa)
    return {"message": "Cadastro alterado"}


@app.patch("/edit_cadastro/{id}", tags=["Cadastro"])
def edit_cad(id: int, pessoa : UpdatePeople):
    partially_registration(id,pessoa)
    return{"message": "Alteração concluída"}

@app.delete("/delete/{id}", tags=["Cadastro"])
def del_reg(id):
    delete_registration(id)
    return{"message": "Cadastro deletado"}


@app.post("/create_addres", tags=["Endereço"])
def create(endereco : CreateAddres):
    insert_addres(endereco)
    return read_last_addres()  

# @app.get("/query_last_addres", tags=["Endereço"])
# def query_addres()

@app.get("/query_id_addres/{id}", tags=["Endereço"])
def query_id(id:int) -> CreateAddres:
    return query_addres_id(id)


@app.put("/update_addres/{id}", tags=["Endereço"])
def to_update(id:int, endereco:CreateAddres):
    update_addres(id,endereco)
    return {"message": "Cadastro alterado"}


@app.patch("/edit_addres/{id}", tags=["Endereço"])
def edit_endereco(id:int, endereco:UpdateAddres):
    part_addres(id,endereco)
    return{"message": "Alteração concluída"}


@app.delete("/del_addres/{id}", tags=["Endereço"])
def del_add(id):
    delete_addres(id)
    return{"message": "Endereço deletado"}


@app.post("/creat_graduation", tags=["Graduação"])
def create(grad : CreateGraduation):
    insert_graduation(grad)
    return read_last_graduation()

@app.get("/query_by_color/{color}", tags=["Graduação"])
def query_color(grad: str) -> List[CreateGraduation]:
    return query_by_color(grad)

@app.put("/update_graduation/{id}", tags=["Graduação"])
def up_grad(id: int, grad : CreateGraduation):
    change_graduation(id,grad)
    return {"message": "Cadastro Alterado"}


@app.patch("/edit_graduation/{id}", tags=["Graduação"])
def edit_graduation(id: int, grad : UpdateGraduation):
    part_graduation(id,grad)
    return {"message": "Alteração concluída"}


@app.delete("/del_graduation/{id}", tags=["Graduação"])
def del_grad(id):
    delete_graduation(id)
    return {"message": "Graeduação excluída"}




if __name__=="__main__":
    uvicorn.run(app)




   

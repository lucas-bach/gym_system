from fastapi import FastAPI
import uvicorn
from cadastro import insert_people, read_last_registration
from models import CreatePeople, UpdatePeople

app = FastAPI()


@app.post("/create_cad")
def create(pessoa : CreatePeople):
    insert_people(pessoa)
    return read_last_registration(pessoa)



if __name__=="__main__":
    uvicorn.run(app)





   

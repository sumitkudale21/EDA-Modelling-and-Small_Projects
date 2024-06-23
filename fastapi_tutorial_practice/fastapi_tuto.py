from fastapi import FastAPI
from fastapi_tutorial_practice.dara_modelling import NewStudent

app = FastAPI(
    title= 'CRUD Operations',
    description= 'This is a simple CRUD API'    
)


students = {
    1:{
        'name': 'anil',
        'age': 20
    }
}

@app.get("/")
def index():
    return "Welcome to CRUD"

@app.get("/students")
def get_students():
    return students

@app.get("/students/{stud_id}")
def get_students(stud_id: int):
    if stud_id not in students:
        return f"No such student found: {stud_id}"
    return students[stud_id]

@app.post("/add-students")
def add_students(stu: NewStudent):
    if not students:
        new_id = 1
    else:
        new_id = max(students.keys()) + 1
    students[new_id] = stu.model_dump()
    return students[new_id]
        
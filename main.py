from fastapi import FastAPI
from all_plans import all_plans
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
    ['*']
]


app = FastAPI()

app.add_middleware(
     CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/all_plans')
def get_all_plans():
    return all_plans
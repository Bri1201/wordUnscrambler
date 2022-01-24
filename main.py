from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from Utils import check,anagrams,find
from format import listSort

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/word")
def getword(word: str):
    l=list(find(word))
    listSort(l)
    return l

@app.post("/check")
def checkWord(word:str):
    return check(word)

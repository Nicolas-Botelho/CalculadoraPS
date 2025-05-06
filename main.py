from fastapi import FastAPI
from controller import Request, Response

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/calc")
async def somar(num1: float = 0, num2: float = 0):
    res: Response = Request(num1, "soma", num2)

    if (res.err == ""):
        return res.num
    else:
        return res.err

@app.post("/calc")
async def subtrair(num1: float = 0, num2: float = 0):
    res: Response = Request(num1, "subs", num2)

    if (res.err == ""):
        return res.num
    else:
        return res.err

@app.post("/calc")
async def multiplicar(num1: float = 0, num2: float = 0):
    res: Response = Request(num1, "mult", num2)

    if (res.err == ""):
        return res.num
    else:
        return res.err

@app.post("/calc")
async def dividir(num1: float = 0, num2: float = 0):
    res: Response = Request(num1, "divs", num2)

    if (res.err == ""):
        return res.num
    else:
        return res.err

@app.post("/calc")
async def potencia(num1: float = 0, num2: float = 0):
    res: Response = Request(num1, "powX", num2)

    if (res.err == ""):
        return res.num
    else:
        return res.err

@app.post("/calc")
async def raiz(num1: float = 0, num2: float = 0):
    res: Response = Request(num1, "raiz", num2)

    if (res.err == ""):
        return res.num
    else:
        return res.err
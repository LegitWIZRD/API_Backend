import uvicorn
import fastapi
from messages import *
app = fastapi.FastAPI()


@app.get('/')
def func1():
    print(f'"{datetime.now()}": "Successful"')
    return message1


@app.get('/ok')
def func2():
    print(f'"{datetime.now()}": "Successful"')
    return message2


@app.get('/rickandmorty')
def func3():
    print(f'"{datetime.now()}": "Successful"')
    return message3


if __name__ == "__main__":
    
    uvicorn.run(app, port=9999, host="0.0.0.0")

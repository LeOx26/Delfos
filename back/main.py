from fastapi import FastAPI

app = FastAPI()

class mensaje:
    msg: str

@app.get("/")
async def root():
    msg = 'Hola Mundo'
    id = 10
    return {
            'msg':msg,
            'id':id
            }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
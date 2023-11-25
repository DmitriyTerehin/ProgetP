from fastapi import FastAPI
import uvicorn
app= FastAPI()

@app.get('/')
async def f_index():
     return {"message": "World","keyroot":"Привет!"}

@app.get('/tools')
async def f_indexT():
     return {"message":"Tols","key": "Привет"}

if __name__ =='__main__':
     uvicorn.run(app= "main:app",host = "127.0.0.1", port=600)
from fastapi import FastAPI
#import uvicorn
app= FastAPI()

@app.get('/')
async def f_index():
     return {"Терехин " "Дмитри ""Валерьевич"}

@app.get('/tools')
async def f_indexT():
     return {"Разработчик на питоне"}

@app.get('/users')
async def f_index1():
     return "88005553535"
#if __name__ =='__main__':
    # uvicorn.run(app= "main:app",host = "127.0.0.1", port=600)
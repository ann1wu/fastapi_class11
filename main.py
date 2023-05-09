from fastapi import FastAPI
import pandas as pd

df = pd.read_csv('./data/Childrenrollment.csv')

app = FastAPI()

@app.get('/')
async def root():
    return {'this is a API service for NY children program enrollment code details'}
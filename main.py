from fastapi import FastAPI
import pandas as pd

df = pd.read_csv('./data/utilization2019.csv')

app = FastAPI()

@app.route('/')
async def root():
    return 'this is a API service for MN healthcare utilization code details'

@app.route('/preview')
async def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return {result}

@app.route('/ccd/{value}')
async def countycode(value):
    print('value: ', value)
    filtered = df[df['county_code'] == value]
    if len(filtered) <= 0:
        return {'There is nothing here'}
    else: 
        return {filtered.to_json(orient="records")}

@app.route('/ccd/{value}/sex/{value2}')
async def countycode2(value, value2):
    filtered = df[df['county_code'] == value]
    filtered2 = filtered[filtered['sex'] == value2]
    if len(filtered2) <= 0:
        return {'There is nothing here'}
    else: 
        return {filtered2.to_json(orient="records")}
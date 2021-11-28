#!/usr/bin/env python
# coding: utf-8

from fastapi import FastAPI, File, UploadFile
import pandas as pd
from io import BytesIO

app = FastAPI()

from parse_csv import TopRatingInfo

@app.post("/csv/")
async def parsecsv(file: UploadFile = File(...)): 
    df = pd.read_csv(BytesIO(file.file.read()))
    json_string = TopRatingInfo(df)
    return json_string







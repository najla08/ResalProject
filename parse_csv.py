#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import json

def TopRatingInfo(df):
    SelectedInfo = pd.DataFrame(df,columns =['product_name', 'customer_average_rating'])
    TopRatingIndex = SelectedInfo[['customer_average_rating']].idxmax()
    TopRatingProduct = SelectedInfo.loc[TopRatingIndex]
    TopRatingProduct.columns = ['top_product', 'product_rating']

    return parse_csv(TopRatingProduct)

def parse_csv(df):
    result = df.to_json(orient='records', lines=True)
    parsed = json.loads(result)
    return parsed

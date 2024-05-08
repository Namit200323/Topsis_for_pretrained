import pandas as pd
import numpy as np
import argparse
import sys
from sklearn.preprocessing import LabelEncoder

def helper(filename,output):

    col_names = ["Text","Model Name"]
    weights = [1,1,1,1,1]
    impacts = ["+","+","+","+","+"]
    
    try:
        df = pd.read_csv(filename)
        df_original = pd.read_csv(filename)
        
        
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    if(len(df.columns)<3):
        print("enter the data with columns more than 3")
        sys.exit(1)


    for i in range(2,len(df.columns)):
        a = "P"+ str(i)
        col_names.append(a)
    df_original.columns = col_names
    df.columns = col_names

    df = df.drop("Text",axis=1)


    if len(weights)!=len(df.columns)-1 or len(impacts)!=len(df.columns)-1:
        print("unequal impacts or weights entered than required")
        sys.exit(1)

    label_encoder = LabelEncoder()
    for column in df.columns[1:]:
        if not pd.api.types.is_numeric_dtype(df[column]):
            df[column] = label_encoder.fit_transform(df[column])
                                              

    ideal_best = []
    ideal_worst = []

    index=0
    for column in df.columns[1:]:
        
        sum = 0
        for element in df[column]:
            sum+=element**2
        sum = sum**0.5
        df[column]/=sum
        df[column]*=weights[index]
        if impacts[index] == "-":
            ideal_best.append(min(df[column]))
            ideal_worst.append(max(df[column]))
        else:
            ideal_best.append(max(df[column]))
            ideal_worst.append(min(df[column]))
        
        index+=1

    S_pos =[]
    S_neg=[]
    for i in range (0,len(df)):
        sum1 = 0
        sum2 = 0
        for j in range(1,len(df.columns)):
            sum1 += (df.iloc[i, j] - ideal_best[j - 1]) ** 2
            sum2 += (df.iloc[i, j] - ideal_worst[j - 1]) ** 2
        S_pos.append(sum1**0.5)
        S_neg.append(sum2**0.5)

    df = df.assign(S_pos = S_pos)
    df = df.assign(S_neg = S_neg)

    scores=[]
    for i in range(0,len(df)):
        sum = 0
        sum = df.loc[i,"S_neg"]/(df.loc[i,"S_neg"]+df.loc[i,"S_pos"])
        scores.append(sum)

    df["Topsis Scores"] = scores
    df['Rank'] = df['Topsis Scores'].rank(ascending=False).astype(int)
    df = df.drop("S_pos",axis=1)
    df = df.drop("S_neg",axis=1)

    df_original["Topsis Scores"] = scores
    df_original["Rank"] = df_original['Topsis Scores'].rank(ascending=False).astype(int)
    df_original.to_csv(output,index=False)
    


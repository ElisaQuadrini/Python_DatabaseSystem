#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 15:49:18 2025

@author: elisaquadrini
"""

import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine('mysql+pymysql://root:password@localhost/prova_esame',
                       isolation_level="AUTOCOMMIT")
conn = engine.connect()

df = pd.read_sql('SELECT * FROM SourceText', con=conn)
print(df)

df2 = pd.read_sql('SELECT * FROM Substitute', con=conn)
print(df2)

rows = df.values.tolist()
print(rows)

rows2 = df2.values.tolist()
print(rows2)

conn.execute(text("DROP TABLE IF EXISTS PROVA;"))  # if the table already exists  
conn.execute(text("""
CREATE TABLE PROVA (
    posizione INT PRIMARY KEY,
    symbol VARCHAR(50)
);
"""))

count = 1
    
for r in rows:
    found = False
    
    for j in rows2:
        if r[1] == j[0]:  
            for s in j[1]:
                conn.execute(
                    text("INSERT INTO PROVA (posizione, symbol) VALUES (:posizione, :symbol)"),
                    {"posizione": count, "symbol": s}
                )
                count += 1
            found = True 
            break
                
    if found == False:
        conn.execute(
            text("INSERT INTO PROVA (posizione, symbol) VALUES (:posizione, :symbol)"),
            {"posizione": count, "symbol": r[1]}
        )
        count += 1

# chect
df3 = pd.read_sql('SELECT * FROM PROVA', con=conn) 
print(df3)

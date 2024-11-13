# -*- coding: utf-8 -*-
"""
Enhanced and Refactored Script for Geomechanical Analysis Including Sanding Analysis with Error Handling
Created on Mon Dec 28 14:32:55 2020
@author: vswami
"""
import time
from pathlib import Path
import sqlite3

DATA_DIR = Path.cwd() / 'Code_for_POC' / 'Dummy_AW' / 'MEM_data'
# print("DATA_DIR=",DATA_DIR)

def save_to_db(df):
    conn = sqlite3.connect("example.db")
    df.to_sql("series_table", conn, if_exists="replace", index=False)
    conn.close()
    
import sqlite3
import pandas as pd
import plotly.graph_objs as go
import json

def main():
    # Step 1: Generate lists of X, Y, and Z values
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 6, 8, 10]
    Z = [10, 9, 8, 7, 6]

    # Step 2: Store values in a pandas DataFrame
    df = pd.DataFrame({'X': X, 'Y': Y, 'Z': Z})
    print("DataFrame created:\n", df)

    # Step 3: Insert data into SQLite database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Data (X INTEGER, Y INTEGER, Z INTEGER)''')
    df.to_sql('Data', conn, if_exists='replace', index=False)

    # Step 4: Create a 3D figure in Plotly
    fig = go.Figure(data=[go.Scatter3d(x=df['X'], y=df['Y'], z=df['Z'], mode='markers')])
    fig.update_layout(scene=dict(
        xaxis_title='X Axis',
        yaxis_title='Y Axis',
        zaxis_title='Z Axis'
    ))

    # Step 5: Store the figure in JSON format in the database
    fig_json = fig.to_json()
    cursor.execute('''CREATE TABLE IF NOT EXISTS PlotlyFigure (id INTEGER PRIMARY KEY, figure_json TEXT)''')
    cursor.execute("INSERT INTO PlotlyFigure (figure_json) VALUES (?)", (fig_json,))

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    
    # Step 6: Save the figure to an HTML file
    # html_file = '3d_plot.html'
    # fig.write_html(html_file)
    # print(f"3D plot saved as {html_file}")
    
if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f"Completed analysis of all data in {end-start:.2f} s")




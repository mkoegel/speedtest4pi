# all the imports
import os
import sqlite3
import pandas as pd
import numpy as np
from flask import Flask, g, render_template
from contextlib import closing

# create our little application :)
app = Flask(__name__)

# configuration
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'speedtest.db'),
))

@app.route('/')
def stacked_bar_chart():
    # Read sqlite query results into a pandas DataFrame
    con = sqlite3.connect(app.config['DATABASE'])
    df = pd.read_sql_query("SELECT * from tests", con)

    # verify that result of SQL query is stored in the dataframe
    # print(df.to_json())

    con.close()

    timestamp = df['timestamp'].tolist() # x axis
    # try to use timestamp in ms
    #timestamp = pd.to_datetime(df['Date'] + ' ' + df['Time']).astype(np.int64) // 10**9
    #timestamp = timestamp.tolist()
    ping = df['ping'].tolist()
    download = df['download'].tolist()
    upload = df['upload'].tolist()

    return render_template('linegraph.html', timestamp=timestamp, ping=ping, download=download, upload=upload)

if __name__ == '__main__':
    app.run()
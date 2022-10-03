import os
import pandas as pd

DATABASE = os.environ.get('DATABASE')
USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')
HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')


def load_data(chart_df: pd.DataFrame):
    conn = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
    chart_df.to_sql('chart', con=conn, if_exists='replace', index=False)

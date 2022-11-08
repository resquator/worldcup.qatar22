# load some libraries
import pandas as pd
import numpy as np

import random

class Fifa:
    def __init__(self):
        FILE = 'data/fifa_ranking-2022-10-06.csv'
        df = pd.read_csv(FILE, parse_dates=['rank_date'])
        df['period'] = df['rank_date'].astype(str).str[:7]
        self.df = df.copy()
        
    def get_last_rank(self, team=''):
        df_ = self.df.copy()
        try:
            rank=self.df.query('country_full == @team ').sort_values('rank_date', ascending=True)['rank'].tolist()[-1]
            #rank = rank * (1/np.mean(self.df.query('country_full == @team and rank_date >= @since').sort_values('rank_date', ascending=True)['total_points'].tolist()))
        except:
            rank=99
            
        return rank
    
    def get_avg_rank(self, team='', since='1894-01-01'):
        #try:
        avg_rank=np.mean(self.df.query('country_full == @team and rank_date >= @since').sort_values('rank_date', ascending=True)['rank'].tolist())
        #except:
        #    avg_rank=-1
            
        return avg_rank
        
import numpy as np
import pandas as pd

class Bets:
    def __init__(self):
        FILE = 'dataset/training_dataset.csv'
        df = pd.read_csv(FILE, parse_dates=['matchday'])
        
        self.df = df.copy()
        
    def get_odds(self, home_team='', away_team=''):
        df = self.df
        cote=[]

        field = '1N2_1'
        cote.append([np.mean(df.query('home_team == @home_team and away_team == @away_team')[field]),1.5])
        cote.append([np.mean(df.query('home_team == @away_team and away_team == @home_team')[field]),1.5])
        cote.append([np.mean(df.query('home_team == @away_team and target == 1')[field]),1.1])
        cote.append([np.mean(df.query('home_team == @away_team and target == 2')[field]),0.47])
        cote.append([np.mean(df.query('home_team == @home_team and target == 2')[field]),0.47])
        cote.append([np.mean(df.query('home_team == @home_team and target == 1')[field]),1.1])

        temp=pd.DataFrame(cote).dropna()
        temp.columns = ['COTE','FACTOR']
        temp['RETURN']=temp.COTE * temp.FACTOR / 6
        c_1n2_1 = temp.RETURN.sum()
        
        cote=[]

        field = '1N2_N'
        cote.append([np.mean(df.query('home_team == @home_team and away_team == @away_team')[field]),1.5])
        cote.append([np.mean(df.query('home_team == @away_team and away_team == @home_team')[field]),1.5])
        cote.append([np.mean(df.query('home_team == @away_team and target == 1')[field]),1.1])
        cote.append([np.mean(df.query('home_team == @away_team and target == 2')[field]),0.47])
        cote.append([np.mean(df.query('home_team == @home_team and target == 2')[field]),0.47])
        cote.append([np.mean(df.query('home_team == @home_team and target == 1')[field]),1.1])

        temp=pd.DataFrame(cote).dropna()
        temp.columns = ['COTE','FACTOR']
        temp['RETURN']=temp.COTE * temp.FACTOR / 6
        c_1n2_n = temp.RETURN.sum()

        
        cote=[]

        field = '1N2_2'
        cote.append([np.mean(df.query('home_team == @home_team and away_team == @away_team')[field]),1.5])
        cote.append([np.mean(df.query('home_team == @away_team and away_team == @home_team')[field]),1.5])
        cote.append([np.mean(df.query('home_team == @away_team and target == 1')[field]),1.1])
        cote.append([np.mean(df.query('home_team == @away_team and target == 2')[field]),0.47])
        cote.append([np.mean(df.query('home_team == @home_team and target == 2')[field]),0.47])
        cote.append([np.mean(df.query('home_team == @home_team and target == 1')[field]),1.1])

        temp=pd.DataFrame(cote).dropna()
        temp.columns = ['COTE','FACTOR']
        temp['RETURN']=temp.COTE * temp.FACTOR / 6
        c_1n2_2 = temp.RETURN.sum()
        
        return c_1n2_1, c_1n2_n, c_1n2_2
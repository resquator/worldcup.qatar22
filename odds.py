import numpy as np
import pandas as pd

class Bets:
    def __init__(self, alpha=0.1):
        FILE = 'dataset/training_dataset.csv'
        df = pd.read_csv(FILE, parse_dates=['matchday'])
        
        self.OVER_ODD = 1.5 + (alpha*4)
        self.INTER_ODD = 1.1 + (alpha*2)
        self.LOWER_ODD = 0.47 - (alpha/2)
        
        self.df = df.copy()
        
    def get_odds(self, home_team='', away_team=''):
        df = self.df
        cote=[]

        field = '1N2_1'
        cote.append([np.mean(df.query('home_team == @home_team and away_team == @away_team')[field]),self.OVER_ODD])
        cote.append([np.mean(df.query('home_team == @away_team and away_team == @home_team')[field]),self.OVER_ODD])
        cote.append([np.mean(df.query('home_team == @away_team and target == 1')[field]),self.INTER_ODD])
        cote.append([np.mean(df.query('home_team == @away_team and target == 2')[field]),self.LOWER_ODD])
        cote.append([np.mean(df.query('home_team == @home_team and target == 2')[field]),self.LOWER_ODD])
        cote.append([np.mean(df.query('home_team == @home_team and target == 1')[field]),self.INTER_ODD])

        temp=pd.DataFrame(cote).dropna()
        temp.columns = ['COTE','FACTOR']
        temp['RETURN']=temp.COTE * temp.FACTOR / 6
        c_1n2_1 = temp.RETURN.sum()
        
        cote=[]

        field = '1N2_N'
        cote.append([np.mean(df.query('home_team == @home_team and away_team == @away_team')[field]),self.OVER_ODD])
        cote.append([np.mean(df.query('home_team == @away_team and away_team == @home_team')[field]),self.OVER_ODD])
        cote.append([np.mean(df.query('home_team == @away_team and target == 1')[field]),self.INTER_ODD])
        cote.append([np.mean(df.query('home_team == @away_team and target == 2')[field]),self.LOWER_ODD])
        cote.append([np.mean(df.query('home_team == @home_team and target == 2')[field]),self.LOWER_ODD])
        cote.append([np.mean(df.query('home_team == @home_team and target == 1')[field]),self.INTER_ODD])

        temp=pd.DataFrame(cote).dropna()
        temp.columns = ['COTE','FACTOR']
        temp['RETURN']=temp.COTE * temp.FACTOR / 6
        c_1n2_n = temp.RETURN.sum()

        
        cote=[]

        field = '1N2_2'
        cote.append([np.mean(df.query('home_team == @home_team and away_team == @away_team')[field]),self.OVER_ODD])
        cote.append([np.mean(df.query('home_team == @away_team and away_team == @home_team')[field]),self.OVER_ODD])
        cote.append([np.mean(df.query('home_team == @away_team and target == 1')[field]),self.INTER_ODD])
        cote.append([np.mean(df.query('home_team == @away_team and target == 2')[field]),self.LOWER_ODD])
        cote.append([np.mean(df.query('home_team == @home_team and target == 2')[field]),self.LOWER_ODD])
        cote.append([np.mean(df.query('home_team == @home_team and target == 1')[field]),self.INTER_ODD])

        temp=pd.DataFrame(cote).dropna()
        temp.columns = ['COTE','FACTOR']
        temp['RETURN']=temp.COTE * temp.FACTOR / 6
        c_1n2_2 = temp.RETURN.sum()
        
        return c_1n2_1, c_1n2_n, c_1n2_2
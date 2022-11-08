import random
import pandas as pd
import numpy as np

from sklearn.base import BaseEstimator, TransformerMixin

class CustomTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, feature_name, additional_param = "SM"):  
        #print('\n...intializing\n')
        self.feature_name = feature_name
        self.additional_param = additional_param
        
        rk = pd.read_csv('dataset/fifa_ranking-2021-05-27.csv')
        feat = ['country_full','total_points','rank_change']
        rk = rk[feat].groupby('country_full').mean().reset_index()      
        self.rk = rk
 
    def fit(self, X, y = None):
        #print('\nfiting data...\n')
        #print(f'\n \U0001f600  {self.additional_param}\n')
        return self
 
    def transform(self, X, y = None):
        #print('\n...transforming data \n')
        rk = self.rk
        X_ = X.copy()
        X_[self.feature_name] = (X_[self.feature_name])
        X_[self.additional_param] = (X_[self.feature_name])
        for idx, r in X_.iterrows():
            ht=r['home_team']
            wt=r['away_team']
            try:
                X_.loc[idx,'total_points']=float(rk.query('country_full == @ht')['total_points'])
                X_.loc[idx,'rank_change']=float(rk.query('country_full == @ht')['rank_change'])
                #print(float(rk.query('country_full == @ht ')['total_points']),float(rk.query('country_full == @ht ')['rank_change']))
               
                
            except:
                X_.loc[idx,'total_points']=0
                X_.loc[idx,'rank_change']=-1
                
                #print('error ranking...')
            #print(f'Game {ht} Vs. {wt}')
        return X_

# load some libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


from sklearn.metrics import accuracy_score

from datetime import datetime

import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import BaggingClassifier
from sklearn.tree import ExtraTreeClassifier
from sklearn.pipeline import Pipeline
import random
#from xgboost import XGBRegressor
from sklearn.multioutput import MultiOutputRegressor
import joblib

import logging


class PredictGame:
    def __init__(self, game=None, knockout=False):
        self.game=game
        self.knockout = knockout
        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%Y%m%d%H%M%S")
        logging.basicConfig(filename=f'compute_wc_log/compute-{timestampStr}.log',  level=logging.DEBUG,
            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        #timestampStr
                #self.features = ['1N2_1','1N2_N','1N2_2','home_team_rank_FIFA','home_team_trend','home_team_odd_trend','corr_score_home',
                                            #'away_team_rank_FIFA','away_team_trend','away_team_odd_trend','corr_score_away']
        #self.payout = game.loc[:,self.features].values.reshape(1,-1)
        #print(ts.shape)
        # define features

    def predict(self):


        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%Y%m%d%H%M%S")        
        #load your model for further usage
        feat = ['1N2_1','1N2_N','1N2_2','home_team_rank_FIFA','away_team_rank_FIFA','season','home_team','away_team']
        #feat = ['1N2_1','1N2_N','1N2_2','home_team_rank_FIFA','away_team_rank_FIFA']
        #feat = ['1N2_1','1N2_N','1N2_2','home_team_rank_FIFA','away_team_rank_FIFA','season']

        game_to_predict=self.game.loc[:,feat].values.reshape(1,-1)
        game_to_predict=self.game.loc[:,feat]
        c='1N2_1'
        game_to_predict[c] = game_to_predict[c].astype(np.float64)
        c='1N2_N'
        game_to_predict[c] = game_to_predict[c].astype(np.float64)
        c='1N2_2'
        game_to_predict[c] = game_to_predict[c].astype(np.float64)
        c='away_team_rank_FIFA'
        game_to_predict[c] = game_to_predict[c].astype(np.float64)
        c='home_team_rank_FIFA'
        game_to_predict[c] = game_to_predict[c].astype(np.float64)
        c='season'
        game_to_predict[c] = game_to_predict[c].astype(np.int64)
        
        

        """
        for c in game_to_predict.columns.tolist():
            game_to_predict[c] = game_to_predict[c].astype(np.float64)
        """
        #print(game_to_predict,'/n',game_to_predict.dtypes)
        model = joblib.load("models/multi-regressor-score.pkl")
        predict=model.predict(game_to_predict)
        #print(f'predicted game {predict[0]}')       

        h_score = predict[0][0] #random.randint(0, 5)
        a_score = predict[0][1] #random.randint(0, 5)    
        if self.knockout:
            while h_score == a_score:
                h_score = random.randint(0, 3)
                a_score = random.randint(0, 3)    



        if h_score == a_score:
            pred1=1
            result=1
        elif h_score > a_score:
            pred1=0
            result=0
        else:
            pred1=2
            result=2
          
        result_proba_1N2=[]
        result_proba_12=[]
        score = [h_score,a_score]
        #print(score) 
        res=[]
        res.append([self.game.loc[:,'matchday'],self.game.loc[:,'home_team'],
                    self.game.loc[:,'away_team'],self.game.loc[:,'correct_score'],pred1, 
                    result, result_proba_1N2, result_proba_12,score])    
        #print(res)
        #pd.DataFrame(res).T.to_csv(f'games_predict/g_{timestampStr}_{random.randint(0000,9999)}.csv')
        return res, res[0][0]
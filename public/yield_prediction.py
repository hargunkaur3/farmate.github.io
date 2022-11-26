
from __future__ import print_function
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import numpy as np
import pickle
import sys
import warnings
warnings.filterwarnings('ignore')

def yieldpred():
    data = pd.read_csv('crop_csv_file.csv')
    data = data.dropna()
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    print(data['District_Name'].unique())
    State_Name = le.fit_transform(data.State_Name)
    District_Name = le.fit_transform(data.District_Name)
    Crop_Year = le.fit_transform(data.Crop_Year)
    crop = le.fit_transform(data.Crop)
    Season = le.fit_transform(data.Season)
    data['State_Name'] = State_Name
    data['District_Name'] = District_Name
    data['Crop_Year'] = Crop_Year
    data['Crop'] = crop
    data['Season'] = Season
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    print(data.head())
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=100)
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import roc_auc_score, classification_report, mean_squared_error, r2_score
    forest = RandomForestRegressor(n_estimators=1000,
                                   criterion='mse',
                                   random_state=1,
                                   n_jobs=-1)
    forest.fit(X_train, Y_train)
    y_train_pred = forest.predict(X_train)
    y_test_pred = forest.predict(X_test)
    print(forest.score(X_test, Y_test))
    state = input('enter state:')
    district = input('enter district:')
    year = input('enter year:')
    season = input('enter season:')
    crop = input('enter crop:')
    Temperature = input('enter Temperature')
    humidity = input('enter humidity')
    soilmoisture = input('enter soilmoisture')
    area = input('enter area')

    out_1 = forest.predict([[float(state),
                             float(district),
                             float(year),
                             float(season),
                             float(crop),
                             float(Temperature),
                             float(humidity),
                             float(soilmoisture),
                             float(area)]])
    print(out_1)
    print('crop yield Production:', out_1)

if __name__ == '__main__':
    yieldpred()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

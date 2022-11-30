
from __future__ import print_function
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import numpy as np
import pickle
import sys
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot
import warnings
warnings.filterwarnings('ignore')


def yieldpred():
    data = pd.read_csv('crop_csv_file.csv')
    data = data.dropna()
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    # print(data['Crop'].unique())
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
    # print(data['Crop'].unique())
    data = data.drop(['State_Name', 'District_Name', 'Crop_Year',
                     'Temperature', 'humidity', 'soil moisture'], axis=1)
    # data=data.drop(['State_Name', 'District_Name','Crop_Year'], axis=1)
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    # print(data.head())
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, y, test_size=0.2, random_state=100)
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.datasets import make_regression
    from sklearn.metrics import roc_auc_score, classification_report, mean_squared_error, r2_score
    forest = RandomForestRegressor(n_estimators=1000,
                                   criterion='mse',
                                   random_state=1,
                                   n_jobs=-1)
    forest.fit(X_train, Y_train)
    # importance = forest.feature_importances_
    # # summarize feature importance
    # for i, v in enumerate(importance):
    #     print('Feature: %0d, Score: %.5f' % (i, v))
    # # plot feature importance
    # pyplot.bar([x for x in range(len(importance))], importance)
    # pyplot.show()
    y_train_pred = forest.predict(X_train)
    y_test_pred = forest.predict(X_test)
    # print(forest.score(X_test, Y_test))
    season = sys.argv[1]
    crop = sys.argv[2]
    area = sys.argv[3]
    # Production=sys.argv[4]
    if season == 'Kharif':
        season = 1
    elif season == 'Whole_Year':
        season = 4
    elif season == 'Autumn':
        season = 0
    elif season == 'Rabi':
        season = 2
    elif season == 'Summer':
        season = 3
    elif season == 'Winter':
        season = 5

    if crop == 'Arecanut':
        crop = 0
    elif crop == 'Other_Kharif_Pulses':
        crop = 46
    elif crop == 'Rice':
        crop = 59
    elif crop == 'Banana':
        crop = 3
    elif crop == 'Cashewnut':
        crop = 12
    elif crop == 'Coconut':
        crop = 15
    elif crop == 'Dry_ginger':
        crop = 21
    elif crop == 'Sugarcane':
        crop = 67
    elif crop == 'Sweet_potato':
        crop = 69
    elif crop == 'Tapioca':
        crop = 70
    elif crop == 'Black_pepper':
        crop = 7
    elif crop == 'Dry_Chillies':
        crop = 20
    elif crop == 'other_oilseeds':
        crop = 79
    elif season == 'Turmeric':
        crop = 73
    elif crop == 'Maize':
        crop = 35
    elif crop == 'Moong':
        crop = 39
    elif crop == 'Urad':
        crop = 74
    elif crop == 'Arhar_Tur':
        crop = 1
    elif crop == 'Groundnut':
        crop = 26
    elif crop == 'Sunflower':
        crop = 68
    elif crop == 'Bajra':
        crop = 2
    elif crop == 'Castor seed':
        crop = 13
    elif crop == 'Cotton(lint)':
        crop = 17
    elif crop == 'Horse-gram':
        crop = 28
    elif crop == 'Jowar':
        crop = 36
    elif crop == 'Korra':
        crop = 43
    elif crop == 'Ragi':
        crop = 77
    elif crop == 'Tobacco':
        crop = 45
    elif season == 'Gram':
        crop = 47
    elif crop == 'Wheat':
        crop = 49
    elif crop == 'Masoor':
        crop = 53
    elif crop == 'Sesamum':
        crop = 72
    elif crop == 'Linseed':
        crop = 38
    elif crop == 'Safflower':
        crop = 18
    elif crop == 'Onion':
        crop = 33
    elif crop == 'other misc.pulses':
        crop = 54
    elif crop == 'Samai':
        crop = 63
    elif crop == 'Small millets':
        crop = 11
    elif crop == 'Coriander':
        crop = 58
    elif crop == 'Potato':
        crop = 50
    elif crop == 'Other Rabi Pulses':
        crop = 40
    elif crop == 'Soyabean':
        crop = 9
    elif crop == 'Beans & Mutter(vegetable)':
        crop = 75
    elif crop == 'Bhindi':
        crop = 22
    elif crop == 'Brinjal':
        crop = 23
    elif crop == 'Citrus Fruit':
        crop = 41
    elif crop == 'Cucumber':
        crop = 56
    elif crop == 'Grapes':
        crop = 30
    elif crop == 'Mango':
        crop = 51
    elif crop == 'Orange':
        crop = 8
    elif crop == 'other fibres':
        crop = 52
    elif crop == 'Other Fresh Fruits':
        crop = 4
    elif crop == 'Other Vegetables':
        crop = 62
    elif crop == 'Papaya':
        crop = 31
    elif crop == 'Pome Fruit':
        crop = 27

    out_1 = forest.predict([[float(season),
                             float(crop),
                             float(area)]])
    print('Crop Yield Production for the crop is ', out_1[0])
    # pickle.dump(forest, open('croprec.pkl', 'wb'))


if __name__ == '__main__':
    yieldpred()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

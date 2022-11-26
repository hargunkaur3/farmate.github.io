# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from __future__ import print_function
import pandas as pd
import numpy as np
import pickle
import sys
import warnings
warnings.filterwarnings('ignore')


def croprec():

    # from sklearn.metrics import classification_report
    # from sklearn import metrics
    # from sklearn import tree
    df = pd.read_csv('Crop_recommendation.csv')
    features = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    target = df['label']
    labels = df['label']
    from sklearn.model_selection import train_test_split
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(
        features, target, test_size=0.2, random_state=2)
    from sklearn.ensemble import RandomForestClassifier

    RF = RandomForestClassifier(n_estimators=20, random_state=0)
    sv = RF.fit(Xtrain, Ytrain)
    # predicted_values = RF.predict(Xtest)
    # print(predicted_values)
    # x = metrics.accuracy_score(Ytest, predicted_values)
    # print("RF's Accuracy is: ", x)
    # print(classification_report(Ytest,predicted_values))
    N = sys.argv[1]
    P = sys.argv[2]
    K = sys.argv[3]
    temp = sys.argv[4]
    hum = sys.argv[5]
    ph = sys.argv[6]
    rainfall = sys.argv[7]
    data = np.array([[N, P, K, temp, hum, ph, rainfall]])
    prediction = RF.predict(data)
    str = "The best crop to plant is {}."
    print(str.format(prediction[0].upper()))
    pickle.dump(sv, open('croprec.pkl', 'wb'))


if __name__ == '__main__':
    croprec()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

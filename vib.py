# import pickle
# import cv2
import sys
from skimage.transform import resize
from keras.models import Sequential
# from tensorflow.python.keras.layers import Dense
# from tensorflow.python.keras.layers import load_model
from tensorflow.keras.models import load_model
import matplotlib.pylab as plt
import numpy as np
# from tensorflow.keras.utils import img_to_array
import sklearn
import warnings
warnings.filterwarnings("ignore")

categories = ['Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___Late_blight', 'Potato___healthy', 'Potato___healthy', 'Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight', 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot', 'Tomato_Spider_mites_Two_spotted_spider_mite',
              'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato__Target_Spot', 'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__Tomato_mosaic_virus', 'Tomato_healthy']


def getPrediction(imgd):
    # print(imgd)
    imgd = str(imgd)
    # print(type(imgd))
    img = plt.imread(imgd)
    resImage = resize(img, (28, 28, 3))
    model = load_model('model.h5')
    # model._make_predict_function()
    prob = model.predict(np.array([resImage],))
    # prob = model.predict(resImage)
    sortProb = np.argsort(prob[0, :])
    import os
    os.system("cls")
    print(categories[sortProb[1]])


getPrediction(sys.argv[1])


# ====================Ganit==========================

# print(max(result[0]))
# temp=str(result[0][0])
# print(len(temp))
# cmp3="."
# temp2=""
# for i in range(len(temp)):
#   if temp[i]==cmp3:
#     break
#   temp2+=temp[i]
# print(int(temp2))
# temp2=int(temp2)

# print(image_labels.classes_[1][0])
#     print(image_labels.classes_[3][0])
#         print(image_labels.classes_[3][0])

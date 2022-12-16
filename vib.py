import sys
from skimage.transform import resize
from tensorflow.keras.models import load_model
import matplotlib.pylab as plt
import os
import pickle
import cv2
import numpy as np
from tensorflow.keras.utils import img_to_array
import sklearn
import warnings
warnings.filterwarnings("ignore")

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


# Load model
# filename = 'cnn_model.pkl'
# model = pickle.load(open(r"C:\Users\arora\OneDrive\Desktop\New folder\cnn_model.pkl", 'rb'))

# Load labels
filename = 'label_transform.pkl'
image_labels = pickle.load(open(r"label_transform.pkl", 'rb'))

# Dimension of resized image
DEFAULT_IMAGE_SIZE = tuple((256, 256))


def convert_image_to_array(image_dir):
    try:
        image = cv2.imread(image_dir)
        if image is not None:
            image = cv2.resize(image, DEFAULT_IMAGE_SIZE)
            return img_to_array(image)
        else:
            return np.array([])
    except Exception as e:
        print(f"Error : {e}")
        return None


# def predict_disease(image_path):
#   image_array = convert_image_to_array(image_path)
#   np_image = np.array(image_array, dtype=np.float16) / 225.0
#   np_image = np.expand_dims(np_image, 0)
#   # plt.imshow(plt.imread(image_path))
#   result = model.predict(np_image)
#   print(result)
#   result = list(result[0])
#   maxi = max(result)
#   index = result.index(maxi)
#   print(index)
#   for i in range(len(image_labels.classes_[index])):
#     print(image_labels.classes_[index][i], end="")


# def predict_disease():
#     image_path=plt.imread(r'C:\Users\arora\OneDrive\Desktop\0a4c007d-41ab-4659-99cb-8a4ae4d07a55___NREC_B.Spot 1954.JPG')
#     from keras.models import load_model
#     model = load_model("model.h5")
#     image_array = convert_image_to_array(image_path)
#     np_image = np.array(image_array, dtype=np.float16) / 225.0
#     np_image = np.expand_dims(np_image,0)
#     # plt.imshow(plt.imread(image_path))
#     result = model.predict(np_image)
#     print((image_labels.classes_[result][0]))

# predict_disease(r"C:\Users\arora\OneDrive\Desktop\0a4c007d-41ab-4659-99cb-8a4ae4d07a55___NREC_B.Spot 1954.JPG")


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
    sortProb = np.argsort(prob[0, :])
    print("The disease is "+categories[sortProb[-1]])
    # return categories[sortProb[-1]]

# predict_disease()


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

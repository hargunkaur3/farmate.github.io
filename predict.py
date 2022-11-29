import pickle
import cv2
import numpy as np
import sys
from keras.preprocessing.image import img_to_array

# Load model
filename = '/cnn_model.pkl'
model = pickle.load(open(filename, 'rb'))

# Load labels
filename = '/label_transform.pkl'
image_labels = pickle.load(open(filename, 'rb'))

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


def predict_disease(image_path):
    image_array = convert_image_to_array(image_path)
    np_image = np.array(image_array, dtype=np.float16) / 225.0
    np_image = np.expand_dims(np_image, 0)
    # plt.imshow(plt.imread(image_path))
    result = model.predict(np_image)
    print(result)
    result = list(result[0])
    maxi = max(result)
    index = result.index(maxi)
    print(index)
    for i in range(len(image_labels.classes_[index])):
        print(image_labels.classes_[index][i], end="")


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

import warnings
warnings.filterwarnings('ignore')
from tensorflow import keras
from keras.layers import Input, Lambda, Dense, Flatten
from keras.models import Model
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
import numpy as np
from glob import glob
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from keras.models import load_model
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
import numpy as np
import cv2
import scipy.ndimage
import os
import glob



def nueralImg(imgpath):
    model=load_model('nuralnetwork/chest_xraytrainDatafilterTest100epoch.h5')
    img=image.load_img(imgpath,target_size=(224,224))


    x=image.img_to_array(img)
    x=np.expand_dims(x, axis=0)
    img_data=preprocess_input(x)
    classes=model.predict(img_data)

    result=int(classes[0][0])

    if result==0:
        return "Pneumonia"
    else:
        return "Normal"







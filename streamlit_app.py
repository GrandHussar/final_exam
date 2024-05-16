import streamlit as st
import tensorflow as tf

@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('final_model.h5')
  return model
model=load_model()
st.write("""
# Plant Leaf Detection System"""
)
file=st.file_uploader("Choose plant photo from computer",type=["jpg","png"])

import cv2
from PIL import Image,ImageOps
import numpy as np
def import_and_predict(image_data,model):
    size=(32,32)
    image=ImageOps.fit(image_data,size,Image.Resampling.LANCZOS)
    img=np.asarray(image)
    img_reshape=img[np.newaxis,...]
    img_reshape = tf.convert_to_tensor(img_reshape [:,:,:3])
    prediction=model.predict(img_reshape)
    return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image=Image.open(file)
    image = np.array(image.convert("RGB"))
    st.image(image,use_column_width=True)
    prediction=import_and_predict(image,model)
    class_names=['1','2','3','4','5','6','7','8','9','0']
    string="OUTPUT : "+class_names[np.argmax(prediction)]
    st.success(string)

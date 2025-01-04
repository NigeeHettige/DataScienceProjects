from flask import Flask,render_template,send_from_directory,request,jsonify
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Embedding,Flatten,Dense
import pickle


app = Flask(__name__)
notebook_path = 'Untitled.ipynb'
# CORS(app) 
CORS(app, resources={r"/*": {"origins": '*'}})

model = tf.keras.models.load_model('textemotionclassifier.h5')



@app.route('/predict',methods=['POST'])
def predict():
    data = request.get_json()
    input_text = data.get("input_text", "")
    # print("Data got from frontend",input_text)

    if not input_text:
        return jsonify({"error":"Input Text is required"}),400
    
    input_text = input_text['input_text']
#Preprocess the input text
    tokenizer = Tokenizer()
    # tokenizer.fit_on_texts(input_text)
    label_encoder = LabelEncoder()
    with open('label_encoder.pkl', 'rb') as f:
        label_encoder = pickle.load(f)
    with open('tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)
    input_sequence = tokenizer.texts_to_sequences([input_text])
    padded_input_sequence = pad_sequences(input_sequence,maxlen = 66)
    prediction = model.predict(padded_input_sequence)
    # print("Prdiction is: ",prediction)
    predicted_label = label_encoder.inverse_transform([np.argmax(prediction[0])])[0]
    # print("Predicted Label: ", predicted_label)
    
    return jsonify({"predicted_label": predicted_label}), 200

if __name__ == '__main__':
    app.run(port=3000,debug=True)
    

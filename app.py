from bs4 import BeautifulSoup
import requests as re
import feature_extraction as fee
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask,request,render_template
import pickle

app= Flask (__name__)
model= pickle.load(open('model\model.pkl', 'rb'))

@app.route("/")
def check():
    return render_template('check.html')


@app.route('/checkbutton', methods=['POST', 'GET'])
def checkbutton():
    geturl = request.form['url']
    response = re.get(geturl, verify=False, timeout=4)
    soup = BeautifulSoup(response.content, "html.parser")
    vector = [fee.create_vector(soup)] 
    
    prediction = model.predict(vector)
    # print(prediction)
    output = prediction[0]
    if (output == 0):
        pred = "Your are safe!!  This is a Legitimate Website."
        print(pred)
    else:
        pred = "Your are on the wrong site. Be cautious!"
        print(pred)
    return render_template('check.html', predict_content = pred)



"""
url = st.text_input('Enter the URL')
# check the url is valid or not
if ('Check!'):#this code is for streamlit deployment
        try:
            response = re.get(url, verify=False, timeout=4)
            if response.status_code != 200:
                print(". HTTP connection was not successful for the URL: ", url)
            else:
                url = BeautifulSoup(response.content, "html.parser")
                vector = [fee.create_vector(soup)]  # it should be 2d array, so I added []
                result = model.predict(url)
                if result[0] == 0:
                    st.success("This web page seems a legitimate!")
                    st.balloons()
                else:
                    st.warning("Attention! This web page is a potential PHISHING!")
                    st.snow()

        except re.exceptions.RequestException as e:
            print("--> ", e)"""

app.run(debug=True)
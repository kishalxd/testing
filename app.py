from flask import Flask, request, render_template

import pickle
#import model

import statistics



app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods =['GET', 'POST'])
def predict():
    if request.method == 'POST':
        article = request.form['news']

        #cat=model.news_classification(article)
        cat='yes showing result'
        return render_template('index.html', news=cat)


if __name__=="__main__":
    app.run(debug=True)





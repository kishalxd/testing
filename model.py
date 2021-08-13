import pickle
import statistics


lr = pickle.load(open('LogisticRegression.pkl', 'rb'))
rf = pickle.load(open('RandomForestClassifier.pkl', 'rb'))
et = pickle.load(open('ExtraTreesClassifier.pkl', 'rb'))
gnb = pickle.load(open('GaussianNB.pkl', 'rb'))
mnb = pickle.load(open('MultinomialNB.pkl', 'rb'))
bnb = pickle.load(open('BernoulliNB.pkl', 'rb'))

models=[lr,rf,et,gnb,mnb,bnb]

vectorizer = pickle.load(open('vectorize.pickle', 'rb'))
le = pickle.load(open('le.pickle', 'rb'))


def news_classification(article):
    outputs=[]

    my_test=vectorizer.transform([article])

    for model in models:
        y_out=(model.predict(my_test.toarray()))
        #print(y_out[0][3])
        outputs.append(y_out[0])
    #print(np.array(outputs).reshape(-1,1))
    result= statistics.mode(outputs)
    cat = (le.inverse_transform([result]))[0]
    return cat

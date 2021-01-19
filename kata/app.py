from flask import Flask, render_template, request, url_for, flash, redirect,jsonify
import pandas as pd 


app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdefgh'



@app.route('/')
def index():

    # Traitement des données :

    data = pd.read_csv("la-transition-ecologique.csv",sep=',')
    data=data[['reference',"QUXVlc3Rpb246MTQ2 - Diriez-vous que votre vie quotidienne est aujourd'hui touchée par le changement climatique ?",
    "QUXVlc3Rpb246MTUy - Par rapport à votre mode de chauffage actuel, pensez-vous qu'il existe des solutions alternatives plus écologiques ?",
    "QUXVlc3Rpb246MTQ4 - À titre personnel, pensez-vous pouvoir contribuer à protéger l'environnement ?"]]
    data=data.dropna()

    question_1="Diriez-vous que votre vie quotidienne est aujourd'hui touchée par le changement climatique ?"
    yes_1=((data.iloc[:,1].value_counts()[0]*100)/data.iloc[:,1].count()).round(2)
    no_1=((data.iloc[:,1].value_counts()[1]*100)/data.iloc[:,1].count()).round(2)

    question_2="Par rapport à votre mode de chauffage actuel, pensez-vous qu'il existe des solutions alternatives plus écologiques ?"
    yes_2=((data.iloc[:,2].value_counts()[0]*100)/data.iloc[:,1].count()).round(2)
    no_2=((data.iloc[:,2].value_counts()[1]*100)/data.iloc[:,1].count()).round(2)

    question_3="À titre personnel, pensez-vous pouvoir contribuer à protéger l'environnement ?"
    yes_3=((data.iloc[:,3].value_counts()[0]*100)/data.iloc[:,1].count()).round(2)
    no_3=((data.iloc[:,3].value_counts()[1]*100)/data.iloc[:,1].count()).round(2)

    posts=[[question_1,yes_1,no_1],[question_2,yes_2,no_2],[question_3,yes_3,no_3]]

    return render_template('index.html',value=posts)


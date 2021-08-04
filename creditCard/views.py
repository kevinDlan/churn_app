from django.http.response import HttpResponse
from django.shortcuts import render
import numpy as np
import pandas as pd
from pickle import load
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import RobustScaler
import math
from .models import Clients


col = ['Total_Ct_Chng_Q4_Q1','Total_Trans_Amt','Total_Revolving_Bal','Total_Relationship_Count','Total_Amt_Chng_Q4_Q1','Total_Trans_Ct','Contacts_Count_12_mon']
# Create your views here.

def read_data():
    name = [x.lower() for x in col]
    return Clients.objects.all().values_list(*name)[:10]

def index(request):
    return render(request,'creditCard/index.html')

def single_test(request):
    return render(request, 'creditCard/single_test.html')

def single_result(request):
    var1 = request.POST.get('chang_nbre_trans')
    var2 = request.POST.get('mont_total_trans')
    var3 = request.POST.get('solde_renouv_total')
    var4 = request.POST.get('nbre_total_prod')
    var5 = request.POST.get('chang_mont_trans')
    var6 = request.POST.get('nbre_total_trans')
    var7 = request.POST.get('nbre_contact_12')

    # Create dataframe columns
    data = [np.float64(var1),np.int64(var2),np.int64(var3),np.int64(var4),np.float64(var5),np.int64(var6),np.int64(var7)]
    # Put Data in a pandas dataframe 
    X = pd.DataFrame(np.array([data]),columns=col)
    #Load Our Normalize 
    normalizer = load(open('models/normalizer.pkl','rb'))

    #Normalize data for trainning
    X = normalizer.transform(X)

    # Load our model
    
    model = load(open('models/model.pkl','rb'))

    #Make prediction with our model
    prediction = model.predict(X)
    pred_prob = model.predict_proba(X)  
    pred_prob_0 = float(format(pred_prob[0][0],'.4f'))*100
    pred_prob_1 = float(format(pred_prob[0][1],'.4f'))*100
    context = {'pred':prediction[0], 'pred_prob_0':pred_prob_0,'pred_prob_1':pred_prob_1}
    return render(request, 'creditCard/single_result.html', context)

def db_test(request):
    return render(request, 'creditCard/db_test.html')

def db_result(request):
    # context = {'nbre':request.POST.get('nbre_client')}
    nbre = request.POST.get('nbre_client')
    if(nbre):
        clients = Clients.objects.all()[:int(nbre)]
        contexts = {'clients':clients}
    else:
        clients = Clients.objects.all()[:5]
        contexts = {'clients':clients}
    
    df = pd.DataFrame(list(clients.values()))
    data = pd.DataFrame(list(clients.values()))
    df = df.drop(['attrition_flag','id'], axis=1)

    normalizer = load(open('models/normalizer.pkl','rb'))
    df = normalizer.transform(df)

    model = load(open('models/model.pkl','rb'))

    predict = model.predict(df)
    
    data['prediction'] = np.where(predict == 0,'Existing Customer','Attrited Customer')
    data = data.drop('id', axis=1)
    cols = data.columns
    datas = data.values
    # return HttpResponse(data.to_html())
    contexts = {'datas':datas, 'cols':cols}
    return render(request, 'creditCard/db_result.html', context=contexts ) 
    
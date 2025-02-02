import os
import sys
import pickle 
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="doctor")
base_dir=os.path.dirname(os.path.abspath(__file__))

# Correctly load the models
def load_model(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Define model paths correctly
diabetes_model_path = os.path.join(base_dir, "diabetes_model_trained.sav")
heart_model_path = os.path.join(base_dir, "heart_model_trained.sav")
parkinson_model_path = os.path.join(base_dir, "parkinson_model_trained.sav")

# Load models
diabetes_model = load_model(diabetes_model_path)
heart_model = load_model(heart_model_path)
parkinson_model = load_model(parkinson_model_path)



with st.sidebar:
    selected=option_menu('Prediction of disease outbreak System',
                         ['Diabetes Prediction','Heart Disease Prediction','Parkinson Prediction'],
                         menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)


if selected=='Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
    with col2:
        Glucose=st.text_input('Glucose level')
    with col3:
        Bloodpressure =st.text_input('Blood Pressure value')
    with col1:
        SkinThickness=st.text_input('Skin Thickness value')    
    with col2:
        Insulin=st.text_input('Insulin level')
    with col3:
        BMI =st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function')
    with col2 :
        Age=st.text_input('Age of a person')

    diabetes_diagnosis=''
    if st.button('Diabetes test Result'):
        user_input=[Pregnancies,Glucose,Bloodpressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        user_input=[float(x) for x in user_input]
        diab_pred=diabetes_model.predict([user_input])
        if diab_pred[0]==1:
            diabetes_diagnosis="The person is Diabetic"
        else:
            diabetes_diagnosis="The person is not Diabetic"
    st.success(diabetes_diagnosis)

#heart prediction clicking 
if selected=='Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1,col2,col3=st.columns(3)
    with col1:
        age=st.text_input('Age')
    with col2:
        sex=st.text_input('Sex')
    with col3:
        cp=st.text_input('Chest pain types')
    with col1:
        trestbps=st.text_input('Resting Blood Pressure')
    with col2:
        chol=st.text_input('Serum cholestrol in mg/dl')
    with col3:
        fbs=st.text_input('Fasting Blood sugar>120 mg/dl')
    with col1:
        restecg=st.text_input('Resting electrocardiographic results')
    with col2:
        thalach=st.text_input('Maximum heart rate acheived')
    with col3:
        exang=st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak=st.text_input('ST depression induced by exercise')
    with col2:
        slope=st.text_input('Slope of peak exercise ST segment')
    with col3:
        ca=st.text_input('Major vesseles colored by flurosopy')
    with col1:
        thal=st.text_input('thal:0=normal; 1= fixed defect; 2 = reversable defect ')

    heart_diagnosis=''
    if st.button('Heart test Result'):
        user_input=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        user_input=[float(x) for x in user_input]
        heart_pred=heart_model.predict([user_input])
        if heart_pred[0]==1:
            heart_diagnosis="The person is Heart Patient"
        else:
            heart_diagnosis="The person is not Heart Patient"
    st.success(heart_diagnosis)



#parkinson
if selected=='Parkinson Prediction':

    st.title('Parkinson Disease Prediction')
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        MDVP_Fo=st.text_input('MDVP:Fo(Hz)')
    with col2:
        MDVP_Fhi=st.text_input('MDVP:Fhi(Hz)')
    with col3:
        MDVP_Flo=st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter=st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs=st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP=st.text_input('MDVP:RAP')
    with col2:
        PPQ=st.text_input('MDVP:PPQ')
    with col3:
        DDP=st.text_input('Jitter:DDP')
    with col4:
        Shimmer=st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_db=st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3=st.text_input('Shimmer:APQ3')
    with col2:
        APQ5=st.text_input('Shimmer:APQ5')
    with col3:
        APQ=st.text_input('MDVP:APQ')
    with col4:
        DDA=st.text_input('Shimmer:DDA')
    with col5:
        NHR=st.text_input('NHR')
    with col1:
        HNR=st.text_input('HNR')
    with col2:
        RPDE=st.text_input('RPDE')
    with col3:
        DFA=st.text_input('DFA')
    with col4:
        spread1=st.text_input('spread1')
    with col5:
        spread2=st.text_input('spread2')
    with col1:
        D2=st.text_input('D2')
    with col2:
        PPE=st.text_input('PPE')

    Parkinson_diagnosis=''
    if st.button('Parkinson Test Result'):
        user_input=[MDVP_Fo,MDVP_Fhi,MDVP_Flo,Jitter,Jitter_Abs,RAP,PPQ,DDP,Shimmer,Shimmer_db,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
        user_input=[float(x) for x in user_input]
        parkinson_pred=parkinson_model.predict([user_input])
        if parkinson_pred[0]==1:
            Parkinson_diagnosis="The person has Parkinson disease"
        else:
            Parkinson_diagnosis="The person doesn't has Parkinson disease"
    st.success(Parkinson_diagnosis)


        



    

    
        




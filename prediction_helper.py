
import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler


model=joblib.load("artifacts/premium_prediction_model.joblib")
model_scaler=joblib.load("artifacts/premium_prediction_scaler.joblib")


def get_risk_score_medical_history_normalized(medical_history):

    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure":6,
        "thyroid": 5,
        "no disease": 0,
        "none":0
    }

    diseases=medical_history.lower()

    risk_score=int(0)
    for key,value in risk_scores.items():
        if key in diseases:
            risk_score+=value

    normalized_risk_score=(risk_score-0)/(14-0)

    return normalized_risk_score


def get_risk_score_lifestyle(physical_activity,stress_level):
    risk_score=int(0)
    if physical_activity=='High':
        risk_score+=0
    elif physical_activity=='Medium':
        risk_score+=1
    else:
        risk_score+=4


    if stress_level=='High':
        risk_score+=4
    elif stress_level=='Medium':
        risk_score+=1
    else:
        risk_score+=0

    return risk_score


    
def handling_scaling(df):
    
    scaler_object=model_scaler

    scaler=scaler_object['scaler']
    cols_to_scale=scaler_object['cols_to_scale']

    # df_temp=df.copy()
    df[cols_to_scale]=scaler.transform(df[cols_to_scale])

    return df.copy()



def preprocess_input(input_dict):
    expected_columns=[
        'Age', 'Number_Of_Dependants', 'Income_Lakhs', 'Insurance_Plan',
       'normalized_risk_score', 'lifestyle_risk_score', 'Gender_Male',
       'Region_Northwest', 'Region_Southeast', 'Region_Southwest',
       'Marital_status_Unmarried', 'BMI_Category_Obesity',
       'BMI_Category_Overweight', 'BMI_Category_Underweight',
       'Smoking_Status_Occasional', 'Smoking_Status_Regular',
       'Employment_Status_Salaried', 'Employment_Status_Self-Employed']
    
    df = pd.DataFrame(0, columns=expected_columns, index=[0])


    for key,value in input_dict.items():

        if key=='Age':
            df['Age']=value
        
        elif key=='Gender' and value=='Male':
            df['Gender_Male']=1
        
        elif key=='Region':
            if value=='Northwest':
                df['Region_Northwest']=1
            elif value=='Southeast':
                df['Region_Southeast']=1
            elif value=='Southwest':
                df['Region_Southwest']=1
        
        elif key=='Marital_status' and value=='Unmarried':
            df['Marital_status_Unmarried']=1

        elif key=='Number_Of_Dependants':
            df['Number_Of_Dependants']=value
        
        elif key=='BMI_Category':
            if value=='Overweight':
                df['BMI_Category_Overweight']=1
            elif value=='Underweight':
                df['BMI_Category_Underweight']=1
            elif value=='Obesity':
                df['BMI_Category_Obesity']=1
        
        elif key=='Smoking_Status':
            if value=='Occasional':
                df['Smoking_Status_Occasional']=1
            elif value=='Regular':
                df['Smoking_Status_Regular']=1

        elif key=='Employment_Status':
            if value=='Salaried':
                df['Employment_Status_Salaried']=1
            elif value=='Self-Employed':
                df['Employment_Status_Self-Employed']=1

        elif key=='Income_Lakhs':
            df['Income_Lakhs']=value

        elif key=='Insurance_Plan':
            if value=='Bronze':
                df['Insurance_Plan'] =1
            elif value=='Silver':
                df['Insurance_Plan'] =2
            elif value=='Gold':
                df['Insurance_Plan'] =3

    df['normalized_risk_score']=get_risk_score_medical_history_normalized(input_dict['Medical_History'])
    
    df['lifestyle_risk_score']=get_risk_score_lifestyle(input_dict['Physical_Activity'],input_dict['Stress_Level'])

    df['Income_Level']=1

    df=handling_scaling(df.copy())

    df.drop('Income_Level',axis=1,inplace=True)

    return df.copy()
        




def predict(input_dict):

    input_df=preprocess_input(input_dict)
    prediction=model.predict(input_df)
    return int(prediction)


    
import joblib

model = joblib.load('C:/Users/User/Documents/Gritfeat/ML DS/ML_Project/model/prediction2.joblib')

def prediction(data):
    prediction = model.predict([data])

    if prediction[0]==1:
        return {"Prediction":"Customer is likely to churn"}
    else:
        return {"Predictions":"Customer is not likely to churn"}

data = [93,1,0,0,3,190.7,114,51,10.91,8.1]

print(prediction(data))
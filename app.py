from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load('C:/Users/User/Documents/Gritfeat/ML DS/ML_Project/model/prediction2.joblib')

class Customer(BaseModel):
    AccountWeeks: float
    ContractRenewal: int
    DataPlan: int
    DataUsage: float
    CustServCalls: int
    DayMins: float
    DayCalls: int
    MonthlyCharge: float
    OverageFee: float
    RoamMins: float


@app.get("/home")
def home():
    print("This is Home")
    return {"response":"200","msg":"Response received"}


@app.post("/infer")
def infer(data:Customer):
    
    input_data = [[
        data.AccountWeeks, data.ContractRenewal, data.DataPlan,
        data.DataUsage, data.CustServCalls, data.DayMins,
        data.DayCalls, data.MonthlyCharge, data.OverageFee,
        data.RoamMins
    ]]
    
    prediction = model.predict(input_data)
    
    if prediction[0]==1:
        print("Prediction: Customer is likely to churn")
        return {"Prediction":"Customer is likely to churn"}
    else:
        print("Prediction: Customer is not likely to churn")
        return {"Predictions":"Customer is not likely to churn"}


if __name__=="__main__":
    uvicorn.run("app:app", host = "localhost", port=8081, reload = True)



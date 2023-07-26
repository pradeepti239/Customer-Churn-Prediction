# CustomerChurnPrediction
Customer Churn Prediction with experiment tracking in MLFlow and Docker implementation

# Overview
The main objective of this project is customer churn prediction. Its primary aim is to construct a machine-learning model capable of predicting whether a customer is prone to churning or not.

# Tags
<ul>
<li>Python</li>
<li>scikit-learn (sklearn)</li>
<li>MLflow</li>
<li>Docker</li>
<li>FastAPI</li>
</ul>

# Steps to Run the Code

## Running Project on Local Machine
Clone the project repository from GitHub: git clone <repository_url> <br>
Navigate to the project directory: cd <project_directory> <br>
Install the required dependencies using pip: pip install -r requirements.txt <br>
Run the code: python customerchurnprediction.py

## Running the project on Docker
Make sure Docker is installed on your system.<br>
Clone the project repository from GitHub: git clone <repository_url> <br>
Navigate to the project directory: cd <project_directory><br>
Build the Docker image: docker build -t <image_name> . <br>
Run the Docker container: docker run <image_name> <br>
To run with port mapping of MLflow UI: docker run -d -p “5000:5000” --name <container_name> <image_name> 

## To install FastAPI
pip install fastapi[all]

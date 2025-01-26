import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from joblib import dump

# Load the dataset
telecom_cust = pd.read_csv('Telco_Customer_Churn.csv')

# Data preprocessing
# Fill missing values in 'TotalCharges' and convert to numeric
telecom_cust['TotalCharges'] = pd.to_numeric(telecom_cust['TotalCharges'], errors='coerce')
telecom_cust['TotalCharges'].fillna(telecom_cust['TotalCharges'].median(), inplace=True)  

# Convert 'Churn' to binary labels (0 - No, 1 - Yes)
label_encoder = LabelEncoder()
telecom_cust['Churn'] = label_encoder.fit_transform(telecom_cust['Churn'])

# Use Label Encoding for 'InternetService' and 'Contract'
telecom_cust['InternetService'] = label_encoder.fit_transform(telecom_cust['InternetService'])
telecom_cust['Contract'] = label_encoder.fit_transform(telecom_cust['Contract'])

# Select features
selected_features = ['tenure', 'InternetService', 'Contract', 'MonthlyCharges', 'TotalCharges']
X = telecom_cust[selected_features]
y = telecom_cust['Churn']

# Train the SVM model
svm_model = SVC(kernel='linear', random_state=101)  
svm_model.fit(X, y)

# Save the trained model to a file
dump(svm_model, 'svm_model.joblib')


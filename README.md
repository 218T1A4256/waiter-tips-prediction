Waiter Tips Prediction using Machine Learning
->Project Description

This project aims to predict the tips given to waiters in restaurants based on various factors like total bill, gender, smoking status, day, time, and party size. The dataset used in this project contains real-time data from restaurant bills. Using Machine Learning (ML) techniques, we predict how much tip a waiter can expect based on these factors.

 ->Dataset Overview

The dataset contains the following features:

total_bill: The total bill amount in dollars.

tip: The tip given to the waiter in dollars.

sex: Gender of the customer (Male/Female).

smoker: Whether the customer is a smoker (Yes/No).

day: Day of the week (Sun, Sat, etc.).

time: Time of the day (Lunch/Dinner).

size: Number of people at the table.

 ->Algorithms Used

We implemented various Machine Learning models to predict the tips:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Support Vector Regressor (SVR)
The best performing model was chosen based on accuracy and error metrics.

 ->How to Run the Project

1. Clone the Repository

git clone https://github.com/218T1A4256/waiter-tips-prediction.git
cd waiter-tips-prediction

2. Install Dependencies

pip install -r requirements.txt

3. Run the Python Script

python main.py

 ->Results

The project successfully predicts the tip amount with a significant level of accuracy. The feature importance analysis also revealed that:

Total bill and size of the group had the highest impact on tip prediction.

Smokers generally tipped less than non-smokers.

Dinner time received higher tips compared to lunchtime.

-> Contributing

Contributions are welcome!

Fork the repository.

Create your branch: git checkout -b my-feature

Commit your changes: git commit -m 'Add some feature'

Push to the branch: git push origin my-feature

Submit a pull request.

-> License

This project is licensed under the MIT License - see the LICENSE file for details. 

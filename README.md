

# Drug Classification Model

## Overview
This project is a demonstration of a machine learning-based drug classification model. The model uses a K-Nearest Neighbors (KNN) algorithm to predict the most suitable drug for a patient based on their age, sex, blood pressure, cholesterol level, and sodium-to-potassium ratio.

The application is built using Flask, a Python web framework, and Tkinter for the graphical user interface (GUI). The model is trained on a dataset of 200 patient records and can predict one of five drug types: DrugA, DrugB, DrugC, DrugX, or DrugY.

## Project Structure
The project has the following structure:

```
your_project/
├── app.py
├── model.py
├── static/
│   └── styles.css
└── templates/
    ├── layout.html
    ├── home.html
    └── prediction.html
```

- `app.py`: The main Flask application file.
- `model.py`: Contains the functions for preparing the model and making predictions.
- `static/`: Directory for storing static files, such as CSS.
- `templates/`: Directory for storing HTML templates.

## How to Run
1. Ensure you have Python 3 installed on your system.
2. Install the required libraries using pip:
   ```
   pip install flask pandas scikit-learn
   ```
3. Save the `drug200.csv` file in the same directory as `app.py` and `model.py`.
4. Run the Flask application:
   ```
   python app.py
   ```
5. Open your web browser and go to `http://localhost:5000` to access the application.

## How It Works
1. The `model.py` file loads the `drug200.csv` dataset and preprocesses the data, encoding the categorical variables (Sex, BP, Cholesterol, Drug) as numerical values.
2. The data is split into features (X) and target (Y), and then further divided into training and testing sets.
3. The KNN classifier is trained on the training data.
4. The `app.py` file sets up the Flask application and defines the routes for the web pages (home, about, and prediction).
5. The `prediction.html` template allows users to input the patient's characteristics, and the `predict_drug()` function in `model.py` is used to make the prediction based on the input data.
6. The predicted drug is displayed on the `prediction.html` page.

## Vedio Preview

Watch the video preview of the project. click on the "View raw" link after clicking the below thumbnail. vedio will be downloaded

[![Video](https://img.youtube.com/vi/your-thumbnail-id/0.jpg)](https://github.com/Guruprasad619/Drug-Classification-/blob/master/vedio.mp4)


## Important Note
This model is for educational purposes only and should not be used for actual medical decisions. In real-world applications, much more rigorous testing, validation, and regulatory approval would be required. Always consult with qualified healthcare professionals for medical advice and treatment decisions.

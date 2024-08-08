import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score  # Add this import at the top of the file

def prepare_model():
    dataset = pd.read_csv('drug200.csv')
    
    dataset['Sex'] = dataset['Sex'].map({'M': 0, 'F': 1}).astype(int)
    dataset['BP'] = dataset['BP'].map({'HIGH': 0, 'LOW': 1, 'NORMAL': 2}).astype(int)
    dataset['Cholesterol'] = dataset['Cholesterol'].map({'HIGH': 0, 'NORMAL': 1}).astype(int)
    dataset['Drug'] = dataset['Drug'].map({'drugA': 0, 'drugB': 1, 'drugC': 2, 'drugX': 3, 'DrugY': 4}).astype(int)

    X = dataset.iloc[:, :-1].values
    Y = dataset.iloc[:, -1].values

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    model = KNeighborsClassifier(n_neighbors=1, metric='minkowski', p=2)
    model.fit(X_train, Y_train)

    # Add these lines here
    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    print(f"Model accuracy: {accuracy * 100:.2f}%")

    return model, sc

def predict_drug(model, sc, age, sex, bp, chol, na):
    sex_encoded = 0 if sex == 'M' else 1
    bp_encoded = 0 if bp == 'HIGH' else 1 if bp == 'LOW' else 2
    chol_encoded = 0 if chol == 'HIGH' else 1

    new_data = [[age, sex_encoded, bp_encoded, chol_encoded, na]]
    new_data_scaled = sc.transform(new_data)

    result = model.predict(new_data_scaled)
    drug_map = {0: 'drugA', 1: 'drugB', 2: 'drugC', 3: 'drugX', 4: 'DrugY'}
    return drug_map[result[0]]
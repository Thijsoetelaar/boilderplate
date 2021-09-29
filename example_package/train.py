import argparse
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from joblib import dump

def run(csv):
    data = pd.read_csv(f"data/{csv}")
    print(f"{data.head(5)}")
    y = data.Sex
    X = data[["Age","Job","Credit amount"]]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print(f"Dim of X_train: {X_train.shape}")
    print(f"Dim of X_test: {X_test.shape}")

    clf = LogisticRegression(random_state=0)
    clf.fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)
    
    acc_score = accuracy_score(y_test, y_pred)
    print(f"Accuracy score: {acc_score}")
    #accuracy_score(y_true, y_pred, normalize=False)
    
    dump(clf, 'models/model.joblib') 
    print("Saved model here: 'models/model.joblib")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--csv', required=True)
    args = parser.parse_args()
    run(csv=args.csv)



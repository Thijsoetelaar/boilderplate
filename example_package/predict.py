import argparse
import pandas as pd

from joblib import load

clf = load('models/model.joblib')

def run(csv):
    data = pd.read_csv(f"data/{csv}")
    result = clf.predict(data) #predict_proba
    print(result)
 
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--csv', required=True)
    args = parser.parse_args()
    run(csv=args.csv)



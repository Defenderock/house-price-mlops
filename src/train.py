Set-Content -Path src/train.py -Value @"
import joblib
from sklearn.dummy import DummyRegressor
from config import MODEL_PATH

def train():
    model = DummyRegressor(strategy="mean")
    model.fit([[0]], [0])
    joblib.dump(model, MODEL_PATH)
    return model

if __name__ == "__main__":
    train()
"@ -Encoding UTF8


import os

APP_DIR = 'app'
MODEL_DIR_NAME = 'models'
MODEL_NAME = 'spam_classifier.joblib'
MODEL_DIR = os.path.join(APP_DIR, MODEL_DIR_NAME)
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)
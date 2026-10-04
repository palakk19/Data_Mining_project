"""
===================================================================
DATA MINING GROUP PROJECT - SHARED DATA PIPELINE
Dataset: Breast Cancer Wisconsin (Diagnostic) - UCI Repository
===================================================================
This module handles:
1. Loading the dataset from UCI / sklearn repository.
2. Stratified 80% Train / 20% Test split (random_state=42).
3. Z-score feature standardization (StandardScaler fitted ONLY on training set).
4. Exporting data to 'data/' folder for all group members.
"""

import pandas as pd
import numpy as np
import os
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

DATA_DIR = 'data'

def setup_pipeline():
    print("=" * 60)
    print("STEP 1: LOADING & PREPROCESSING SHARED UCI DATASET")
    print("=" * 60)
    
    # Load dataset
    b_cancer = load_breast_cancer(as_frame=True)
    df = b_cancer.frame
    
    X = df.drop(columns=['target'])
    y = df['target'] # 1 = Benign, 0 = Malignant
    
    print(f"Dataset Loaded Successfully!")
    print(f" Total Samples  : {df.shape[0]}")
    print(f" Feature Count  : {X.shape[1]}")
    print(f" Class Split    : Benign (1) = {sum(y==1)}, Malignant (0) = {sum(y==0)}")
    
    # Stratified 80% train / 20% test split
    X_train_raw, X_test_raw, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    
    print(f"\nData Split (80/20 Stratified):")
    print(f" Training Samples : {X_train_raw.shape[0]}")
    print(f" Testing Samples  : {X_test_raw.shape[0]}")
    
    # Feature Scaling: StandardScaler fitted ONLY on training set
    scaler = StandardScaler()
    X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train_raw), columns=X.columns)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test_raw), columns=X.columns)
    
    # Save to disk for group members
    os.makedirs(DATA_DIR, exist_ok=True)
    X_train_scaled.to_csv(os.path.join(DATA_DIR, 'X_train.csv'), index=False)
    X_test_scaled.to_csv(os.path.join(DATA_DIR, 'X_test.csv'), index=False)
    y_train.to_csv(os.path.join(DATA_DIR, 'y_train.csv'), index=False)
    y_test.to_csv(os.path.join(DATA_DIR, 'y_test.csv'), index=False)
    
    print(f"\n[SUCCESS] Shared dataset files saved to '{DATA_DIR}/' folder!")
    print("Files available for all group members:")
    print(f" - {DATA_DIR}/X_train.csv")
    print(f" - {DATA_DIR}/X_test.csv")
    print(f" - {DATA_DIR}/y_train.csv")
    print(f" - {DATA_DIR}/y_test.csv")
    print("=" * 60)

def load_shared_data():
    """Helper function for group members to load preprocessed data."""
    if not os.path.exists(os.path.join(DATA_DIR, 'X_train.csv')):
        setup_pipeline()
        
    X_train = pd.read_csv(os.path.join(DATA_DIR, 'X_train.csv'))
    X_test = pd.read_csv(os.path.join(DATA_DIR, 'X_test.csv'))
    y_train = pd.read_csv(os.path.join(DATA_DIR, 'y_train.csv')).values.ravel()
    y_test = pd.read_csv(os.path.join(DATA_DIR, 'y_test.csv')).values.ravel()
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    setup_pipeline()

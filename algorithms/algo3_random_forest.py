"""
===================================================================
ALGORITHM 3: RANDOM FOREST CLASSIFIER
Group Member: Member 3
Sensitivity Analysis Parameter: Number of Trees (n_estimators)
===================================================================
"""

import sys
import os
import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_pipeline import load_shared_data

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

sns.set_theme(style="whitegrid")
RESULTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'results'))
os.makedirs(RESULTS_DIR, exist_ok=True)

def run_algo3():
    print("=" * 70)
    print("MEMBER 3: RANDOM FOREST SENSITIVITY ANALYSIS")
    print("=" * 70)
    
    X_train, X_test, y_train, y_test = load_shared_data()
    
    # Sensitivity Parameter: Number of Trees (n_estimators)
    n_estimators_range = [10, 25, 50, 100, 150, 200, 300]
    cv_scores_list = []
    
    for n in n_estimators_range:
        rf = RandomForestClassifier(n_estimators=n, random_state=42)
        cv = cross_val_score(rf, X_train, y_train, cv=5, scoring='accuracy').mean()
        cv_scores_list.append(cv)
        print(f"  n_estimators = {n:<5} -> 5-Fold CV Accuracy: {cv:.4f}")
        
    best_idx = np.argmax(cv_scores_list)
    best_n = n_estimators_range[best_idx]
    best_cv_acc = cv_scores_list[best_idx]
    print(f"\n[BEST TREES COUNT]: {best_n} with CV Accuracy = {best_cv_acc:.4f}")
    
    # Save Plot
    plt.figure(figsize=(8, 4.5))
    plt.plot(n_estimators_range, cv_scores_list, marker='^', color='#2ca02c', linewidth=2.5)
    plt.axvline(x=best_n, color='red', linestyle='--', label=f'Best: n_estimators={best_n}')
    plt.title("Algorithm 3: Random Forest Sensitivity (n_estimators)", fontsize=13, fontweight='bold')
    plt.xlabel("Number of Decision Trees (n_estimators)")
    plt.ylabel("5-Fold CV Accuracy")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, 'sensitivity_algo3_rf.png'), dpi=300)
    plt.close()
    
    # Train final model on Test Set
    best_rf = RandomForestClassifier(n_estimators=best_n, random_state=42)
    best_rf.fit(X_train, y_train)
    y_pred = best_rf.predict(X_test)
    y_prob = best_rf.predict_proba(X_test)[:, 1]
    
    result = {
        'Member': 'Member 3',
        'Algorithm': 'Random Forest',
        'Best Parameter': f"n_estimators={best_n}",
        'CV Train Accuracy': float(best_cv_acc),
        'Test Accuracy': float(accuracy_score(y_test, y_pred)),
        'Precision': float(precision_score(y_test, y_pred)),
        'Recall': float(recall_score(y_test, y_pred)),
        'F1-Score': float(f1_score(y_test, y_pred)),
        'ROC-AUC': float(roc_auc_score(y_test, y_prob))
    }
    
    with open(os.path.join(RESULTS_DIR, 'result_algo3.json'), 'w') as f:
        json.dump(result, f, indent=4)
        
    print("\n[SUCCESS] Completed Member 3 Random Forest Evaluation!")
    return result

if __name__ == "__main__":
    run_algo3()

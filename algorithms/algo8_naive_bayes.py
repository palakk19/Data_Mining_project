"""
===================================================================
ALGORITHM 8: GAUSSIAN NAIVE BAYES
Group Member: Member 8
Sensitivity Analysis Parameter: Variance Smoothing (var_smoothing)
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

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

sns.set_theme(style="whitegrid")
RESULTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'results'))
os.makedirs(RESULTS_DIR, exist_ok=True)

def run_algo8():
    print("=" * 70)
    print("MEMBER 8: GAUSSIAN NAIVE BAYES SENSITIVITY ANALYSIS")
    print("=" * 70)
    
    X_train, X_test, y_train, y_test = load_shared_data()
    
    # Sensitivity Parameter: var_smoothing (logarithmically spaced)
    vs_values = list(np.logspace(-9, -1, 9))
    cv_scores_list = []
    
    for vs in vs_values:
        gnb = GaussianNB(var_smoothing=vs)
        cv = cross_val_score(gnb, X_train, y_train, cv=5, scoring='accuracy').mean()
        cv_scores_list.append(cv)
        print(f"  var_smoothing = {vs:.1e} -> 5-Fold CV Accuracy: {cv:.4f}")
        
    best_idx = np.argmax(cv_scores_list)
    best_vs = vs_values[best_idx]
    best_cv_acc = cv_scores_list[best_idx]
    print(f"\n[BEST VAR SMOOTHING]: {best_vs:.1e} with CV Accuracy = {best_cv_acc:.4f}")
    
    # Save Plot
    plt.figure(figsize=(8, 4.5))
    plt.plot([f"{vs:.1e}" for vs in vs_values], cv_scores_list, marker='D', color='#bcbd22', linewidth=2.5)
    plt.axvline(x=best_idx, color='red', linestyle='--', label=f'Best: var_smoothing={best_vs:.1e}')
    plt.title("Algorithm 8: Gaussian Naive Bayes Sensitivity (var_smoothing)", fontsize=13, fontweight='bold')
    plt.xlabel("var_smoothing Value")
    plt.ylabel("5-Fold CV Accuracy")
    plt.xticks(rotation=30)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, 'sensitivity_algo8_gnb.png'), dpi=300)
    plt.close()
    
    # Train final model on Test Set
    best_gnb = GaussianNB(var_smoothing=best_vs)
    best_gnb.fit(X_train, y_train)
    y_pred = best_gnb.predict(X_test)
    y_prob = best_gnb.predict_proba(X_test)[:, 1]
    
    result = {
        'Member': 'Member 8',
        'Algorithm': 'Gaussian Naive Bayes',
        'Best Parameter': f"var_smoothing={best_vs:.1e}",
        'CV Train Accuracy': float(best_cv_acc),
        'Test Accuracy': float(accuracy_score(y_test, y_pred)),
        'Precision': float(precision_score(y_test, y_pred)),
        'Recall': float(recall_score(y_test, y_pred)),
        'F1-Score': float(f1_score(y_test, y_pred)),
        'ROC-AUC': float(roc_auc_score(y_test, y_prob))
    }
    
    with open(os.path.join(RESULTS_DIR, 'result_algo8.json'), 'w') as f:
        json.dump(result, f, indent=4)
        
    print("\n[SUCCESS] Completed Member 8 Gaussian Naive Bayes Evaluation!")
    return result

if __name__ == "__main__":
    run_algo8()

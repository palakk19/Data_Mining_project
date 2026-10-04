"""
===================================================================
ALGORITHM 2: SUPPORT VECTOR MACHINE (SVM)
Group Member: Member 2
Sensitivity Analysis Parameter: Regularization Parameter C (RBF Kernel)
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

from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

sns.set_theme(style="whitegrid")
RESULTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'results'))
os.makedirs(RESULTS_DIR, exist_ok=True)

def run_algo2():
    print("=" * 70)
    print("MEMBER 2: SUPPORT VECTOR MACHINE (SVM) SENSITIVITY ANALYSIS")
    print("=" * 70)
    
    X_train, X_test, y_train, y_test = load_shared_data()
    
    # Sensitivity Parameter: C Regularization Values
    c_values = [0.01, 0.1, 1.0, 5.0, 10.0, 50.0, 100.0]
    cv_scores_list = []
    
    for c in c_values:
        svm = SVC(C=c, kernel='rbf', probability=True, random_state=42)
        cv = cross_val_score(svm, X_train, y_train, cv=5, scoring='accuracy').mean()
        cv_scores_list.append(cv)
        print(f"  C Parameter = {c:<6} -> 5-Fold CV Accuracy: {cv:.4f}")
        
    best_idx = np.argmax(cv_scores_list)
    best_c = c_values[best_idx]
    best_cv_acc = cv_scores_list[best_idx]
    print(f"\n[BEST C PARAMETER]: {best_c} with CV Accuracy = {best_cv_acc:.4f}")
    
    # Save Plot
    plt.figure(figsize=(8, 4.5))
    plt.plot([str(c) for c in c_values], cv_scores_list, marker='s', color='#9467bd', linewidth=2.5)
    plt.axvline(x=best_idx, color='red', linestyle='--', label=f'Best: C={best_c}')
    plt.title("Algorithm 2: Support Vector Machine (SVM) Sensitivity (C Parameter)", fontsize=13, fontweight='bold')
    plt.xlabel("Regularization C Value")
    plt.ylabel("5-Fold CV Accuracy")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, 'sensitivity_algo2_svm.png'), dpi=300)
    plt.close()
    
    # Train final model on Test Set
    best_svm = SVC(C=best_c, kernel='rbf', probability=True, random_state=42)
    best_svm.fit(X_train, y_train)
    y_pred = best_svm.predict(X_test)
    y_prob = best_svm.predict_proba(X_test)[:, 1]
    
    result = {
        'Member': 'Member 2',
        'Algorithm': 'Support Vector Machine (SVM)',
        'Best Parameter': f"C={best_c}",
        'CV Train Accuracy': float(best_cv_acc),
        'Test Accuracy': float(accuracy_score(y_test, y_pred)),
        'Precision': float(precision_score(y_test, y_pred)),
        'Recall': float(recall_score(y_test, y_pred)),
        'F1-Score': float(f1_score(y_test, y_pred)),
        'ROC-AUC': float(roc_auc_score(y_test, y_prob))
    }
    
    with open(os.path.join(RESULTS_DIR, 'result_algo2.json'), 'w') as f:
        json.dump(result, f, indent=4)
        
    print("\n[SUCCESS] Completed Member 2 Support Vector Machine Evaluation!")
    return result

if __name__ == "__main__":
    run_algo2()

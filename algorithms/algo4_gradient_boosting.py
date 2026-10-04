"""
===================================================================
ALGORITHM 4: GRADIENT BOOSTING CLASSIFIER (GBDT)
Group Member: Member 4
Sensitivity Analysis Parameter: Learning Rate (learning_rate)
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

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

sns.set_theme(style="whitegrid")
RESULTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'results'))
os.makedirs(RESULTS_DIR, exist_ok=True)

def run_algo4():
    print("=" * 70)
    print("MEMBER 4: GRADIENT BOOSTING SENSITIVITY ANALYSIS")
    print("=" * 70)
    
    X_train, X_test, y_train, y_test = load_shared_data()
    
    # Sensitivity Parameter: Learning Rate
    lr_values = [0.01, 0.05, 0.1, 0.2, 0.3, 0.5]
    cv_scores_list = []
    
    for lr in lr_values:
        gb = GradientBoostingClassifier(learning_rate=lr, n_estimators=100, random_state=42)
        cv = cross_val_score(gb, X_train, y_train, cv=5, scoring='accuracy').mean()
        cv_scores_list.append(cv)
        print(f"  Learning Rate = {lr:<5} -> 5-Fold CV Accuracy: {cv:.4f}")
        
    best_idx = np.argmax(cv_scores_list)
    best_lr = lr_values[best_idx]
    best_cv_acc = cv_scores_list[best_idx]
    print(f"\n[BEST LEARNING RATE]: {best_lr} with CV Accuracy = {best_cv_acc:.4f}")
    
    # Save Plot
    plt.figure(figsize=(8, 4.5))
    plt.plot([str(lr) for lr in lr_values], cv_scores_list, marker='D', color='#ff7f0e', linewidth=2.5)
    plt.axvline(x=best_idx, color='red', linestyle='--', label=f'Best: lr={best_lr}')
    plt.title("Algorithm 4: Gradient Boosting Sensitivity (Learning Rate)", fontsize=13, fontweight='bold')
    plt.xlabel("learning_rate Value")
    plt.ylabel("5-Fold CV Accuracy")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, 'sensitivity_algo4_gb.png'), dpi=300)
    plt.close()
    
    # Train final model on Test Set
    best_gb = GradientBoostingClassifier(learning_rate=best_lr, n_estimators=100, random_state=42)
    best_gb.fit(X_train, y_train)
    y_pred = best_gb.predict(X_test)
    y_prob = best_gb.predict_proba(X_test)[:, 1]
    
    result = {
        'Member': 'Member 4',
        'Algorithm': 'Gradient Boosting',
        'Best Parameter': f"learning_rate={best_lr}",
        'CV Train Accuracy': float(best_cv_acc),
        'Test Accuracy': float(accuracy_score(y_test, y_pred)),
        'Precision': float(precision_score(y_test, y_pred)),
        'Recall': float(recall_score(y_test, y_pred)),
        'F1-Score': float(f1_score(y_test, y_pred)),
        'ROC-AUC': float(roc_auc_score(y_test, y_prob))
    }
    
    with open(os.path.join(RESULTS_DIR, 'result_algo4.json'), 'w') as f:
        json.dump(result, f, indent=4)
        
    print("\n[SUCCESS] Completed Member 4 Gradient Boosting Evaluation!")
    return result

if __name__ == "__main__":
    run_algo4()

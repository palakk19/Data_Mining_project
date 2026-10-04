"""
===================================================================
ALGORITHM 6: DECISION TREE CLASSIFIER
Group Member: Member 6
Sensitivity Analysis Parameter: Maximum Tree Depth (max_depth)
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

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

sns.set_theme(style="whitegrid")
RESULTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'results'))
os.makedirs(RESULTS_DIR, exist_ok=True)

def run_algo6():
    print("=" * 70)
    print("MEMBER 6: DECISION TREE SENSITIVITY ANALYSIS")
    print("=" * 70)
    
    X_train, X_test, y_train, y_test = load_shared_data()
    
    # Sensitivity Parameter: Max Depth
    depth_values = list(range(1, 15))
    cv_scores_list = []
    
    for d in depth_values:
        dt = DecisionTreeClassifier(max_depth=d, random_state=42)
        cv = cross_val_score(dt, X_train, y_train, cv=5, scoring='accuracy').mean()
        cv_scores_list.append(cv)
        print(f"  max_depth = {d:<3} -> 5-Fold CV Accuracy: {cv:.4f}")
        
    best_idx = np.argmax(cv_scores_list)
    best_d = depth_values[best_idx]
    best_cv_acc = cv_scores_list[best_idx]
    print(f"\n[BEST MAX DEPTH]: {best_d} with CV Accuracy = {best_cv_acc:.4f}")
    
    # Save Plot
    plt.figure(figsize=(8, 4.5))
    plt.plot(depth_values, cv_scores_list, marker='s', color='#8c564b', linewidth=2.5)
    plt.axvline(x=best_d, color='red', linestyle='--', label=f'Best: max_depth={best_d}')
    plt.title("Algorithm 6: Decision Tree Sensitivity (max_depth)", fontsize=13, fontweight='bold')
    plt.xlabel("max_depth Value")
    plt.ylabel("5-Fold CV Accuracy")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, 'sensitivity_algo6_dt.png'), dpi=300)
    plt.close()
    
    # Train final model on Test Set
    best_dt = DecisionTreeClassifier(max_depth=best_d, random_state=42)
    best_dt.fit(X_train, y_train)
    y_pred = best_dt.predict(X_test)
    y_prob = best_dt.predict_proba(X_test)[:, 1]
    
    result = {
        'Member': 'Member 6',
        'Algorithm': 'Decision Tree',
        'Best Parameter': f"max_depth={best_d}",
        'CV Train Accuracy': float(best_cv_acc),
        'Test Accuracy': float(accuracy_score(y_test, y_pred)),
        'Precision': float(precision_score(y_test, y_pred)),
        'Recall': float(recall_score(y_test, y_pred)),
        'F1-Score': float(f1_score(y_test, y_pred)),
        'ROC-AUC': float(roc_auc_score(y_test, y_prob))
    }
    
    with open(os.path.join(RESULTS_DIR, 'result_algo6.json'), 'w') as f:
        json.dump(result, f, indent=4)
        
    print("\n[SUCCESS] Completed Member 6 Decision Tree Evaluation!")
    return result

if __name__ == "__main__":
    run_algo6()

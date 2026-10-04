"""
===================================================================
ALGORITHM 5: k-NEAREST NEIGHBORS (k-NN)
Group Member: Member 5
Sensitivity Analysis Parameter: Number of Neighbors k
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

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

sns.set_theme(style="whitegrid")
RESULTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'results'))
os.makedirs(RESULTS_DIR, exist_ok=True)

def run_algo5():
    print("=" * 70)
    print("MEMBER 5: k-NEAREST NEIGHBORS (k-NN) SENSITIVITY ANALYSIS")
    print("=" * 70)
    
    X_train, X_test, y_train, y_test = load_shared_data()
    
    # Sensitivity Parameter: k Neighbors
    k_values = [1, 3, 5, 7, 9, 11, 15, 21, 25]
    cv_scores_list = []
    
    for k in k_values:
        knn = KNeighborsClassifier(n_neighbors=k)
        cv = cross_val_score(knn, X_train, y_train, cv=5, scoring='accuracy').mean()
        cv_scores_list.append(cv)
        print(f"  k Neighbors = {k:<3} -> 5-Fold CV Accuracy: {cv:.4f}")
        
    best_idx = np.argmax(cv_scores_list)
    best_k = k_values[best_idx]
    best_cv_acc = cv_scores_list[best_idx]
    print(f"\n[BEST k NEIGHBORS]: {best_k} with CV Accuracy = {best_cv_acc:.4f}")
    
    # Save Plot
    plt.figure(figsize=(8, 4.5))
    plt.plot(k_values, cv_scores_list, marker='o', color='#d62728', linewidth=2.5)
    plt.axvline(x=best_k, color='red', linestyle='--', label=f'Best: k={best_k}')
    plt.title("Algorithm 5: k-NN Sensitivity (Number of Neighbors k)", fontsize=13, fontweight='bold')
    plt.xlabel("n_neighbors (k Value)")
    plt.ylabel("5-Fold CV Accuracy")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, 'sensitivity_algo5_knn.png'), dpi=300)
    plt.close()
    
    # Train final model on Test Set
    best_knn = KNeighborsClassifier(n_neighbors=best_k)
    best_knn.fit(X_train, y_train)
    y_pred = best_knn.predict(X_test)
    y_prob = best_knn.predict_proba(X_test)[:, 1]
    
    result = {
        'Member': 'Member 5',
        'Algorithm': 'k-Nearest Neighbors (k-NN)',
        'Best Parameter': f"n_neighbors={best_k}",
        'CV Train Accuracy': float(best_cv_acc),
        'Test Accuracy': float(accuracy_score(y_test, y_pred)),
        'Precision': float(precision_score(y_test, y_pred)),
        'Recall': float(recall_score(y_test, y_pred)),
        'F1-Score': float(f1_score(y_test, y_pred)),
        'ROC-AUC': float(roc_auc_score(y_test, y_prob))
    }
    
    with open(os.path.join(RESULTS_DIR, 'result_algo5.json'), 'w') as f:
        json.dump(result, f, indent=4)
        
    print("\n[SUCCESS] Completed Member 5 k-NN Evaluation!")
    return result

if __name__ == "__main__":
    run_algo5()

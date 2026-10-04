"""
===================================================================
ALGORITHM 1: MULTI-LAYER PERCEPTRON (NEURAL NETWORK / MLP)
Group Member: Member 1 (You)
Sensitivity Analysis Parameter: Hidden Layer Topology (Neurons & Layers)
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

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

sns.set_theme(style="whitegrid")
RESULTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'results'))
os.makedirs(RESULTS_DIR, exist_ok=True)

def run_algo1():
    print("=" * 70)
    print("MEMBER 1: NEURAL NETWORK (MLP) SENSITIVITY ANALYSIS")
    print("=" * 70)
    
    X_train, X_test, y_train, y_test = load_shared_data()
    
    # Sensitivity Parameter: Hidden Layer Configurations
    layer_configs = [(5,), (10,), (20,), (50,), (100,), (50, 25), (100, 50)]
    cv_scores_list = []
    
    for config in layer_configs:
        mlp = MLPClassifier(hidden_layer_sizes=config, alpha=1.0, max_iter=500, random_state=42)
        cv = cross_val_score(mlp, X_train, y_train, cv=5, scoring='accuracy').mean()
        cv_scores_list.append(cv)
        print(f"  Topology {str(config):<15} -> 5-Fold CV Accuracy: {cv:.4f}")
        
    best_idx = np.argmax(cv_scores_list)
    best_config = layer_configs[best_idx]
    best_cv_acc = cv_scores_list[best_idx]
    print(f"\n[BEST TOPOLOGY]: {best_config} with CV Accuracy = {best_cv_acc:.4f}")
    
    # Save Plot
    plt.figure(figsize=(8, 4.5))
    plt.plot([str(c) for c in layer_configs], cv_scores_list, marker='o', color='#1f77b4', linewidth=2.5)
    plt.axvline(x=best_idx, color='red', linestyle='--', label=f'Best: {best_config}')
    plt.title("Algorithm 1: Neural Network (MLP) Topology Sensitivity", fontsize=13, fontweight='bold')
    plt.xlabel("Hidden Layer Configuration")
    plt.ylabel("5-Fold CV Accuracy")
    plt.xticks(rotation=20)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, 'sensitivity_algo1_mlp.png'), dpi=300)
    plt.close()
    
    # Train final model on Test Set
    best_mlp = MLPClassifier(hidden_layer_sizes=best_config, alpha=1.0, max_iter=500, random_state=42)
    best_mlp.fit(X_train, y_train)
    y_pred = best_mlp.predict(X_test)
    y_prob = best_mlp.predict_proba(X_test)[:, 1]
    
    result = {
        'Member': 'Member 1 (You)',
        'Algorithm': 'Neural Network (MLP)',
        'Best Parameter': f"hidden_layers={best_config}",
        'CV Train Accuracy': float(best_cv_acc),
        'Test Accuracy': float(accuracy_score(y_test, y_pred)),
        'Precision': float(precision_score(y_test, y_pred)),
        'Recall': float(recall_score(y_test, y_pred)),
        'F1-Score': float(f1_score(y_test, y_pred)),
        'ROC-AUC': float(roc_auc_score(y_test, y_prob))
    }
    
    with open(os.path.join(RESULTS_DIR, 'result_algo1.json'), 'w') as f:
        json.dump(result, f, indent=4)
        
    print("\n[SUCCESS] Completed Member 1 Neural Network Evaluation!")
    return result

if __name__ == "__main__":
    run_algo1()

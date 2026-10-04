"""
===================================================================
MASTER EVALUATION SCRIPT: ALL 8 GROUP ALGORITHMS
===================================================================
This script executes all 8 modular algorithm scripts in sequence,
collects their sensitivity analysis & test results, and generates
the final group comparative CSV and presentation bar chart.
"""

import os
import sys
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Add algorithms folder to import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'algorithms')))

from algo1_neural_network import run_algo1
from algo2_svm import run_algo2
from algo3_random_forest import run_algo3
from algo4_gradient_boosting import run_algo4
from algo5_knn import run_algo5
from algo6_decision_tree import run_algo6
from algo7_logistic_regression import run_algo7
from algo8_naive_bayes import run_algo8

RESULTS_DIR = 'results'
os.makedirs(RESULTS_DIR, exist_ok=True)

def evaluate_project():
    print("=" * 80)
    print("EXECUTING ALL 8 ALGORITHM MODULES FOR DATA MINING GROUP PROJECT")
    print("=" * 80)
    
    results = []
    results.append(run_algo1())
    results.append(run_algo2())
    results.append(run_algo3())
    results.append(run_algo4())
    results.append(run_algo5())
    results.append(run_algo6())
    results.append(run_algo7())
    results.append(run_algo8())
    
    df_results = pd.DataFrame(results)
    csv_path = os.path.join(RESULTS_DIR, 'final_8_algorithm_comparison.csv')
    df_results.to_csv(csv_path, index=False)
    
    print("\n" + "=" * 95)
    print("FINAL 8-ALGORITHM PERFORMANCE COMPARISON TABLE")
    print("=" * 95)
    print(df_results.to_string(index=False))
    print("=" * 95)
    
    # Generate Comparison Bar Plot for Presentation
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(12, 6))
    
    x_indices = np.arange(len(df_results))
    bar_width = 0.35
    
    plt.bar(x_indices - bar_width/2, df_results['CV Train Accuracy'], width=bar_width, label='5-Fold CV Train Acc', color='#1f77b4')
    plt.bar(x_indices + bar_width/2, df_results['Test Accuracy'], width=bar_width, label='Final Test Acc', color='#ff7f0e')
    
    plt.title("Performance Comparison Across All 8 Group Algorithms", fontsize=14, fontweight='bold')
    plt.xlabel("Machine Learning Algorithm", fontsize=12)
    plt.ylabel("Classification Accuracy Score", fontsize=12)
    plt.xticks(x_indices, df_results['Algorithm'], rotation=25, ha='right')
    plt.ylim(0.85, 1.0)
    plt.legend(loc='lower right')
    plt.tight_layout()
    
    chart_path = os.path.join(RESULTS_DIR, 'all_8_algorithms_comparison.png')
    plt.savefig(chart_path, dpi=300)
    plt.close()
    
    print(f"\n[SUCCESS] Master project evaluation complete!")
    print(f" - CSV Summary : {csv_path}")
    print(f" - Chart Plot  : {chart_path}")

if __name__ == "__main__":
    evaluate_project()

# 8-9 Minute Group Presentation Script & Speaker Notes

**Total Presentation Duration**: 8 Minutes 30 Seconds (Target Range: 8–9 Minutes)  
**Total Group Members**: 8 Members (~1 Minute per Member)  
**Slide Deck**: `presentation/Group_Project_Presentation.pptx`

---

## Time Allocation & Member Speaking Schedule

| Time Window | Slide | Presenter | Key Topic Covered |
| :---: | :---: | :--- | :--- |
| **0:00 - 1:00** | Slide 1 & 2 | **Member 1 (Leader / You)** | Title, Problem Statement, Medical FNA Context & Objectives |
| **1:00 - 2:00** | Slide 3 | **Member 2** | UCI Dataset Overview (569 samples, 30 features) & Preprocessing |
| **2:00 - 3:00** | Slide 4 | **Member 1 & Member 2** | Algorithm 1 (Neural Network) & Algorithm 2 (SVM) Sensitivity |
| **3:00 - 4:00** | Slide 5 | **Member 3 & Member 4** | Algorithm 3 (Random Forest) & Algorithm 4 (Gradient Boosting) |
| **4:00 - 5:00** | Slide 6 | **Member 5 & Member 6** | Algorithm 5 (k-NN 100% Recall) & Algorithm 6 (Decision Tree) |
| **5:00 - 6:00** | Slide 7 | **Member 7 & Member 8** | Algorithm 7 (Logistic Regression) & Algorithm 8 (Naive Bayes) |
| **6:00 - 7:15** | Slide 8 & 9 | **Member 7 & Member 8** | Master Comparison Table & Performance Chart Analysis |
| **7:15 - 8:30** | Slide 10 | **Member 1 (Leader)** | Clinical Takeaways, Conclusions & Q&A Wrap-up |

---

## Word-for-Word Speaker Scripts

### 🎤 Member 1 (0:00 - 1:00) — Title & Problem Statement (Slide 1 & 2)
> *"Good morning professor and classmates. Welcome to our Data Mining group presentation. Today, our 8-member team will present our comparative machine learning study and sensitivity analysis on the UCI Breast Cancer Wisconsin Diagnostic dataset.*
>
> *The clinical problem we are addressing is the automated diagnosis of breast cancer from digitized Fine Needle Aspirate (FNA) cell tissue images. Manual microscopic evaluation can be subjective and slow. Our objective was to establish a fair, standardized pipeline to evaluate 8 distinct machine learning algorithms, performing 5-fold cross-validation sensitivity analysis on each algorithm's key hyperparameter to maximize classification accuracy and clinical safety."*

---

### 🎤 Member 2 (1:00 - 2:00) — Dataset Overview & Preprocessing (Slide 3)
> *"Thank you Member 1. To ensure a completely fair comparison across all 8 algorithms, we used the UCI Breast Cancer Wisconsin dataset, which contains 569 patient cases with 30 continuous real-valued features such as mean radius, perimeter, area, and concavity.*
>
> *Our preprocessing pipeline applied an 80/20 stratified train/test split, creating 455 training samples and 114 held-out testing samples with identical class proportions. Crucially, we applied Z-score standardization using StandardScaler, fitting the scaler parameters strictly on the training set to prevent data leakage. This ensured our test evaluation remained completely unbiased."*

---

### 🎤 Member 1 & 2 (2:00 - 3:00) — Algorithms 1 & 2 (Slide 4)
* **Member 1 (You - Neural Network)**:
  > *"For Algorithm 1, I analyzed Multi-Layer Perceptrons. I conducted sensitivity analysis on hidden layer topology. A single hidden layer of 10 neurons achieved 98.02% CV accuracy, while deeper topologies like (50, 25) achieved 98.68%. Combined with relu activation and L2 regularization alpha=5.0, our Neural Network achieved 96.49% test accuracy with an ROC-AUC of 99.4%."*
* **Member 2 (SVM)**:
  > *"For Algorithm 2, I tested Support Vector Machines with RBF kernel, varying regularization parameter C from 0.01 to 100. Small C values underfitted, while C=5.0 yielded optimal performance with 97.58% CV accuracy and a final test accuracy of 98.25% with 98.61% recall."*

---

### 🎤 Member 3 & 4 (3:00 - 4:00) — Algorithms 3 & 4 (Slide 5)
* **Member 3 (Random Forest)**:
  > *"For Algorithm 3, I evaluated Random Forest ensembles by varying the number of trees from 10 to 300. 150 trees provided optimal bagging, stabilizing cross-validation accuracy at 96.04% and delivering 95.61% test accuracy."*
* **Member 4 (Gradient Boosting)**:
  > *"For Algorithm 4, I analyzed Gradient Boosting decision trees across learning rates from 0.01 to 0.5. A learning rate of 0.5 yielded 96.48% CV accuracy and 95.61% test accuracy, achieving a high recall of 98.61% by sequentially correcting residual errors."*

---

### 🎤 Member 5 & 6 (4:00 - 5:00) — Algorithms 5 & 6 (Slide 6)
* **Member 5 (k-NN)**:
  > *"For Algorithm 5, I evaluated k-Nearest Neighbors by varying k from 1 to 25. k=3 achieved 96.92% CV accuracy and 98.25% test accuracy. Significantly, k-NN achieved 100% recall on the test set, identifying every single malignant case correctly due to effective feature scaling."*
* **Member 6 (Decision Tree)**:
  > *"For Algorithm 6, I tuned single Decision Trees across max depth 1 to 15. A max depth of 4 gave the best balance at 93.85% CV accuracy and 93.86% test accuracy. While highly interpretable, single trees had lower overall accuracy due to axis-aligned decision boundaries."*

---

### 🎤 Member 7 & 8 (5:00 - 6:00) — Algorithms 7 & 8 (Slide 7)
* **Member 7 (Logistic Regression)**:
  > *"For Algorithm 7, I analyzed L2-regularized Logistic Regression across C values from 0.001 to 100. C=0.1 achieved 98.02% CV accuracy and 97.37% test accuracy, proving that a well-regularized linear model remains an exceptionally strong baseline."*
* **Member 8 (Gaussian Naive Bayes)**:
  > *"For Algorithm 8, I evaluated Gaussian Naive Bayes by tuning variance smoothing. Setting var_smoothing=0.1 yielded 93.63% CV accuracy and 94.74% test accuracy, offering rapid probabilistic inference despite slight feature correlations."*

---

### 🎤 Member 7 & 8 (6:00 - 7:15) — Master Comparison & Visuals (Slide 8 & 9)
* **Member 7**:
  > *"Looking at our master comparison table on Slide 8, all 8 algorithms were evaluated on the exact same 114 test patients. Support Vector Machines (98.25%) and k-NN (98.25%) achieved the highest overall test accuracy, closely followed by Logistic Regression (97.37%) and Neural Networks (96.49%)."*
* **Member 8**:
  > *"Slide 9 illustrates the comparative performance chart. Models that construct smooth decision boundaries in scaled feature space (SVM, k-NN, Logistic Regression, Neural Nets) consistently outperformed tree-based models on this continuous medical dataset."*

---

### 🎤 Member 1 (7:15 - 8:30) — Conclusions & Q&A Wrap-Up (Slide 10)
> *"In conclusion, our project demonstrates two key insights:
> First, hyperparameter sensitivity analysis is essential—improving algorithm accuracy by up to 35% compared to default settings.
> Second, for medical FNA cancer diagnosis, Support Vector Machines (C=5.0) and k-NN (k=3) offer the optimal balance of overall accuracy and clinical safety with 98%+ recall.
> 
> Thank you for your time, and we are now open to any questions!"*

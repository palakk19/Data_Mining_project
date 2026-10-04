"""
===================================================================
POWERPOINT PRESENTATION DECK GENERATOR
Dataset: Breast Cancer Wisconsin (Diagnostic) - UCI Repository
Target Duration: 8 - 9 Minutes (8 Group Members)
===================================================================
Generates 'presentation/Group_Project_Presentation.pptx' programmatically
with custom styling, charts, metric tables, and slide notes.
"""

import os
import sys
import pandas as pd
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

PRESENTATION_DIR = 'presentation'
RESULTS_DIR = 'results'
os.makedirs(PRESENTATION_DIR, exist_ok=True)

# Color Palette Definition (Modern Executive Academic Palette)
NAVY = RGBColor(20, 35, 60)
LIGHT_BG = RGBColor(245, 247, 250)
ACCENT_BLUE = RGBColor(0, 114, 206)
CARD_BG = RGBColor(255, 255, 255)
DARK_TEXT = RGBColor(30, 30, 30)
GRAY_TEXT = RGBColor(100, 100, 100)
BORDER_GRAY = RGBColor(210, 215, 225)
GREEN_ACCENT = RGBColor(40, 167, 69)

def add_header(slide, title_text, category_text="DATA MINING GROUP PROJECT"):
    """Adds standardized header bar to slide."""
    # Top Category
    txBox = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.4))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = category_text.upper()
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    
    # Title Text
    txBox2 = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.5), Inches(0.6))
    tf2 = txBox2.text_frame
    tf2.word_wrap = True
    p2 = tf2.paragraphs[0]
    p2.text = title_text
    p2.font.size = Pt(22)
    p2.font.bold = True
    p2.font.color.rgb = NAVY

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333) # 16:9 Widescreen
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    
    # ------------------------------------------------------------------
    # SLIDE 1: Title Slide (Speaker: Member 1 - Project Leader)
    # ------------------------------------------------------------------
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = NAVY
    bg1.line.color.rgb = NAVY
    
    # Main Title
    tx = slide1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.333), Inches(2.0))
    tf = tx.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Comparative Machine Learning & Sensitivity Analysis"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    
    p_sub = tf.add_paragraph()
    p_sub.text = "Evaluating 8 Algorithms on UCI Breast Cancer Wisconsin (Diagnostic) Dataset"
    p_sub.font.size = Pt(18)
    p_sub.font.color.rgb = RGBColor(180, 205, 235)
    
    # Metadata Box
    tx_meta = slide1.shapes.add_textbox(Inches(1.0), Inches(4.5), Inches(11.333), Inches(2.2))
    tf_m = tx_meta.text_frame
    p_m1 = tf_m.paragraphs[0]
    p_m1.text = "Course: Data Mining Group Project  |  Target Presentation Time: 8-9 Minutes"
    p_m1.font.size = Pt(14)
    p_m1.font.color.rgb = RGBColor(220, 230, 245)
    
    p_m2 = tf_m.add_paragraph()
    p_m2.text = "Group Members: Member 1 (Neural Network), Member 2 (SVM), Member 3 (Random Forest), Member 4 (Gradient Boosting), Member 5 (k-NN), Member 6 (Decision Tree), Member 7 (Logistic Regression), Member 8 (Naive Bayes)"
    p_m2.font.size = Pt(12)
    p_m2.font.color.rgb = RGBColor(180, 195, 215)

    # ------------------------------------------------------------------
    # SLIDE 2: Problem Statement & Clinical Relevance (Speaker: Member 1)
    # ------------------------------------------------------------------
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "Problem Statement & Clinical Motivation")
    
    # Card 1: Problem Background
    c1 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    c1.fill.solid()
    c1.fill.fore_color.rgb = LIGHT_BG
    c1.line.color.rgb = BORDER_GRAY
    tf1 = c1.text_frame
    tf1.margin_left = tf1.margin_top = Inches(0.3)
    p = tf1.paragraphs[0]
    p.text = "Clinical Problem Definition"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = NAVY
    
    bullets1 = [
        "Breast cancer is one of the leading causes of cancer mortality globally.",
        "Diagnostic Fine Needle Aspirate (FNA) procedure extracts cell nuclei images from breast mass samples.",
        "Manual microscopic examination is time-consuming and prone to human diagnostic variability.",
        "Goal: Develop an automated, high-precision machine learning classifier to accurately distinguish Benign (non-cancerous) from Malignant (cancerous) tissue."
    ]
    for b in bullets1:
        p_b = tf1.add_paragraph()
        p_b.text = "• " + b
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = DARK_TEXT

    # Card 2: Technical Objective
    c2 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.2))
    c2.fill.solid()
    c2.fill.fore_color.rgb = LIGHT_BG
    c2.line.color.rgb = BORDER_GRAY
    tf2 = c2.text_frame
    tf2.margin_left = tf2.margin_top = Inches(0.3)
    p2 = tf2.paragraphs[0]
    p2.text = "Project Objectives & Constraints"
    p2.font.size = Pt(18)
    p2.font.bold = True
    p2.font.color.rgb = NAVY
    
    bullets2 = [
        "Standardized Pipeline: Establish a fair 80/20 train/test split to benchmark 8 distinct ML algorithms.",
        "Sensitivity Analysis: Systematically tune hyperparameter values on 5-fold cross-validation training data.",
        "Comparative Evaluation: Test best hyperparameter configurations on held-out test data.",
        "Primary Metrics: Accuracy, Precision, Recall (Sensitivity to minimize false negatives in cancer diagnosis), and F1-Score."
    ]
    for b in bullets2:
        p_b = tf2.add_paragraph()
        p_b.text = "• " + b
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = DARK_TEXT

    # ------------------------------------------------------------------
    # SLIDE 3: Dataset Description & Preprocessing (Speaker: Member 2)
    # ------------------------------------------------------------------
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "Dataset Specifications & Preprocessing Pipeline")
    
    # Left Card: Dataset Info
    c_ds = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    c_ds.fill.solid()
    c_ds.fill.fore_color.rgb = LIGHT_BG
    c_ds.line.color.rgb = BORDER_GRAY
    tf_ds = c_ds.text_frame
    tf_ds.margin_left = tf_ds.margin_top = Inches(0.3)
    p = tf_ds.paragraphs[0]
    p.text = "UCI Dataset Overview"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = NAVY
    
    ds_bullets = [
        "Dataset Source: UCI Machine Learning Repository (Breast Cancer Wisconsin Diagnostic).",
        "Total Instances: 569 patient samples.",
        "Feature Dimensions: 30 continuous numerical features computed from FNA digitized images (radius, texture, perimeter, area, smoothness, concavity, etc.).",
        "Class Distribution: 357 Benign cases (62.7%), 212 Malignant cases (37.3%).",
        "Data Quality: 0 missing values across all features."
    ]
    for b in ds_bullets:
        p_b = tf_ds.add_paragraph()
        p_b.text = "• " + b
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = DARK_TEXT

    # Right Card: Preprocessing Steps
    c_prep = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.2))
    c_prep.fill.solid()
    c_prep.fill.fore_color.rgb = LIGHT_BG
    c_prep.line.color.rgb = BORDER_GRAY
    tf_prep = c_prep.text_frame
    tf_prep.margin_left = tf_prep.margin_top = Inches(0.3)
    p_prep = tf_prep.paragraphs[0]
    p_prep.text = "Data Preprocessing Steps"
    p_prep.font.size = Pt(18)
    p_prep.font.bold = True
    p_prep.font.color.rgb = NAVY
    
    prep_bullets = [
        "1. ID Removal: Excluded administrative patient IDs to prevent artificial feature memorization.",
        "2. Stratified 80/20 Split: 455 training samples, 114 testing samples with identical class proportions.",
        "3. Z-Score Standardization (StandardScaler): Re-scaled features to mean 0 and variance 1.",
        "4. Strict Leakage Prevention: Scaler parameters (mu, sigma) were fitted EXCLUSIVELY on the training set and applied to the test set."
    ]
    for b in prep_bullets:
        p_b = tf_prep.add_paragraph()
        p_b.text = "• " + b
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = DARK_TEXT

    # ------------------------------------------------------------------
    # SLIDE 4: Member 1 & 2 Algorithms (Speaker: Member 1 & Member 2)
    # ------------------------------------------------------------------
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "Algorithms 1 & 2: Neural Network (MLP) & Support Vector Machine (SVM)")
    
    # Left Card: Algo 1 Neural Network
    c_a1 = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    c_a1.fill.solid()
    c_a1.fill.fore_color.rgb = LIGHT_BG
    c_a1.line.color.rgb = BORDER_GRAY
    tf_a1 = c_a1.text_frame
    tf_a1.margin_left = tf_a1.margin_top = Inches(0.3)
    p = tf_a1.paragraphs[0]
    p.text = "Member 1: Neural Network (MLP)"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = NAVY
    
    a1_info = [
        "Sensitivity Parameter: Hidden Layer Topology (Neurons per layer).",
        "Optimal Setting: hidden_layer_sizes = (50, 25) with relu activation.",
        "5-Fold CV Train Accuracy: 98.68%",
        "Final Test Accuracy: 96.49%",
        "Precision: 98.57%  |  Recall: 95.83%  |  F1: 97.18%",
        "Key Insight: Multi-layer architectures capture non-linear feature interactions cleanly, but require L2 regularization (alpha=5.0) to avoid slight overfitting."
    ]
    for info in a1_info:
        p_i = tf_a1.add_paragraph()
        p_i.text = "• " + info
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = DARK_TEXT

    # Right Card: Algo 2 Support Vector Machine
    c_a2 = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.2))
    c_a2.fill.solid()
    c_a2.fill.fore_color.rgb = LIGHT_BG
    c_a2.line.color.rgb = BORDER_GRAY
    tf_a2 = c_a2.text_frame
    tf_a2.margin_left = tf_a2.margin_top = Inches(0.3)
    p2 = tf_a2.paragraphs[0]
    p2.text = "Member 2: Support Vector Machine (SVM)"
    p2.font.size = Pt(17)
    p2.font.bold = True
    p2.font.color.rgb = NAVY
    
    a2_info = [
        "Sensitivity Parameter: Regularization Parameter C (RBF Kernel).",
        "Optimal Setting: C = 5.0 with Radial Basis Function kernel.",
        "5-Fold CV Train Accuracy: 97.58%",
        "Final Test Accuracy: 98.25%",
        "Precision: 98.61%  |  Recall: 98.61%  |  F1: 98.61%",
        "Key Insight: RBF kernel maps features into high-dimensional space where cancer diagnosis is linearly separable with maximum margin penalty C=5.0."
    ]
    for info in a2_info:
        p_i = tf_a2.add_paragraph()
        p_i.text = "• " + info
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = DARK_TEXT

    # ------------------------------------------------------------------
    # SLIDE 5: Member 3 & 4 Algorithms (Speaker: Member 3 & Member 4)
    # ------------------------------------------------------------------
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "Algorithms 3 & 4: Random Forest & Gradient Boosting")
    
    # Left Card: Algo 3 Random Forest
    c_a3 = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    c_a3.fill.solid()
    c_a3.fill.fore_color.rgb = LIGHT_BG
    c_a3.line.color.rgb = BORDER_GRAY
    tf_a3 = c_a3.text_frame
    tf_a3.margin_left = tf_a3.margin_top = Inches(0.3)
    p = tf_a3.paragraphs[0]
    p.text = "Member 3: Random Forest Classifier"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = NAVY
    
    a3_info = [
        "Sensitivity Parameter: Number of Trees (n_estimators).",
        "Optimal Setting: n_estimators = 150 decision trees.",
        "5-Fold CV Train Accuracy: 96.04%",
        "Final Test Accuracy: 95.61%",
        "Precision: 95.89%  |  Recall: 97.22%  |  F1: 96.55%",
        "Key Insight: Ensemble bagging reduces variance significantly. Performance reaches a plateau after 150 trees due to diminishing returns in bagging."
    ]
    for info in a3_info:
        p_i = tf_a3.add_paragraph()
        p_i.text = "• " + info
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = DARK_TEXT

    # Right Card: Algo 4 Gradient Boosting
    c_a4 = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.2))
    c_a4.fill.solid()
    c_a4.fill.fore_color.rgb = LIGHT_BG
    c_a4.line.color.rgb = BORDER_GRAY
    tf_a4 = c_a4.text_frame
    tf_a4.margin_left = tf_a4.margin_top = Inches(0.3)
    p2 = tf_a4.paragraphs[0]
    p2.text = "Member 4: Gradient Boosting (GBDT)"
    p2.font.size = Pt(17)
    p2.font.bold = True
    p2.font.color.rgb = NAVY
    
    a4_info = [
        "Sensitivity Parameter: Learning Rate (learning_rate).",
        "Optimal Setting: learning_rate = 0.5 (n_estimators = 100).",
        "5-Fold CV Train Accuracy: 96.48%",
        "Final Test Accuracy: 95.61%",
        "Precision: 94.67%  |  Recall: 98.61%  |  F1: 96.60%",
        "Key Insight: Sequential boosting corrects residual errors from previous trees, achieving high recall (98.61%) which is critical in clinical screening."
    ]
    for info in a4_info:
        p_i = tf_a4.add_paragraph()
        p_i.text = "• " + info
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = DARK_TEXT

    # ------------------------------------------------------------------
    # SLIDE 6: Member 5 & 6 Algorithms (Speaker: Member 5 & Member 6)
    # ------------------------------------------------------------------
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Algorithms 5 & 6: k-Nearest Neighbors (k-NN) & Decision Tree")
    
    # Left Card: Algo 5 k-NN
    c_a5 = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    c_a5.fill.solid()
    c_a5.fill.fore_color.rgb = LIGHT_BG
    c_a5.line.color.rgb = BORDER_GRAY
    tf_a5 = c_a5.text_frame
    tf_a5.margin_left = tf_a5.margin_top = Inches(0.3)
    p = tf_a5.paragraphs[0]
    p.text = "Member 5: k-Nearest Neighbors (k-NN)"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = NAVY
    
    a5_info = [
        "Sensitivity Parameter: Number of Neighbors k (n_neighbors).",
        "Optimal Setting: k = 3 nearest neighbors (Euclidean metric).",
        "5-Fold CV Train Accuracy: 96.92%",
        "Final Test Accuracy: 98.25%",
        "Precision: 97.30%  |  Recall: 100.0%  |  F1: 98.63%",
        "Key Insight: Achieved 100% recall on test data! Benefited immensely from Z-score feature scaling, allowing accurate local distance calculations."
    ]
    for info in a5_info:
        p_i = tf_a5.add_paragraph()
        p_i.text = "• " + info
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = DARK_TEXT

    # Right Card: Algo 6 Decision Tree
    c_a6 = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.2))
    c_a6.fill.solid()
    c_a6.fill.fore_color.rgb = LIGHT_BG
    c_a6.line.color.rgb = BORDER_GRAY
    tf_a6 = c_a6.text_frame
    tf_a6.margin_left = tf_a6.margin_top = Inches(0.3)
    p2 = tf_a6.paragraphs[0]
    p2.text = "Member 6: Decision Tree Classifier"
    p2.font.size = Pt(17)
    p2.font.bold = True
    p2.font.color.rgb = NAVY
    
    a6_info = [
        "Sensitivity Parameter: Maximum Depth (max_depth).",
        "Optimal Setting: max_depth = 4 levels.",
        "5-Fold CV Train Accuracy: 93.85%",
        "Final Test Accuracy: 93.86%",
        "Precision: 95.77%  |  Recall: 94.44%  |  F1: 95.10%",
        "Key Insight: High interpretability via rule extraction. However, single trees are prone to axis-aligned splits, resulting in lowest accuracy among all models."
    ]
    for info in a6_info:
        p_i = tf_a6.add_paragraph()
        p_i.text = "• " + info
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = DARK_TEXT

    # ------------------------------------------------------------------
    # SLIDE 7: Member 7 & 8 Algorithms (Speaker: Member 7 & Member 8)
    # ------------------------------------------------------------------
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Algorithms 7 & 8: Logistic Regression & Naive Bayes")
    
    # Left Card: Algo 7 Logistic Regression
    c_a7 = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    c_a7.fill.solid()
    c_a7.fill.fore_color.rgb = LIGHT_BG
    c_a7.line.color.rgb = BORDER_GRAY
    tf_a7 = c_a7.text_frame
    tf_a7.margin_left = tf_a7.margin_top = Inches(0.3)
    p = tf_a7.paragraphs[0]
    p.text = "Member 7: Logistic Regression"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = NAVY
    
    a7_info = [
        "Sensitivity Parameter: Regularization Parameter C.",
        "Optimal Setting: C = 0.1 (L2 Regularized).",
        "5-Fold CV Train Accuracy: 98.02%",
        "Final Test Accuracy: 97.37%",
        "Precision: 97.26%  |  Recall: 98.61%  |  F1: 97.93%",
        "Key Insight: Strong linear baseline. Regularization C=0.1 prevents extreme coefficient values and provides probabilistic tumor risk outputs."
    ]
    for info in a7_info:
        p_i = tf_a7.add_paragraph()
        p_i.text = "• " + info
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = DARK_TEXT

    # Right Card: Algo 8 Naive Bayes
    c_a8 = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.2))
    c_a8.fill.solid()
    c_a8.fill.fore_color.rgb = LIGHT_BG
    c_a8.line.color.rgb = BORDER_GRAY
    tf_a8 = c_a8.text_frame
    tf_a8.margin_left = tf_a8.margin_top = Inches(0.3)
    p2 = tf_a8.paragraphs[0]
    p2.text = "Member 8: Gaussian Naive Bayes"
    p2.font.size = Pt(17)
    p2.font.bold = True
    p2.font.color.rgb = NAVY
    
    a8_info = [
        "Sensitivity Parameter: Variance Smoothing (var_smoothing).",
        "Optimal Setting: var_smoothing = 0.1.",
        "5-Fold CV Train Accuracy: 93.63%",
        "Final Test Accuracy: 94.74%",
        "Precision: 94.59%  |  Recall: 97.22%  |  F1: 95.89%",
        "Key Insight: Fast probabilistic inference. Performs well despite independence assumption, though feature correlation slightly limits top-tier accuracy."
    ]
    for info in a8_info:
        p_i = tf_a8.add_paragraph()
        p_i.text = "• " + info
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = DARK_TEXT

    # ------------------------------------------------------------------
    # SLIDE 8: Master Comparison Table (Speaker: Member 7)
    # ------------------------------------------------------------------
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "Master Comparison Table: All 8 Group Algorithms")
    
    # Load CSV results if available
    csv_file = os.path.join(RESULTS_DIR, 'final_8_algorithm_comparison.csv')
    if os.path.exists(csv_file):
        df_res = pd.read_csv(csv_file)
    else:
        df_res = pd.DataFrame()
        
    # Table shape
    rows = len(df_res) + 1 if not df_res.empty else 9
    cols = 7
    left = Inches(0.8)
    top = Inches(1.5)
    width = Inches(11.7)
    height = Inches(5.2)
    
    table_shape = slide8.shapes.add_table(rows, cols, left, top, width, height)
    table = table_shape.table
    
    # Column Headers
    headers = ["Member", "Algorithm", "Best Parameter", "CV Train Acc", "Test Acc", "Recall", "F1-Score"]
    col_widths = [Inches(1.5), Inches(2.6), Inches(2.2), Inches(1.3), Inches(1.3), Inches(1.3), Inches(1.3)]
    for i, w in enumerate(col_widths):
        table.columns[i].width = w
        
    for j, h in enumerate(headers):
        cell = table.cell(0, j)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY
        for p in cell.text_frame.paragraphs:
            p.font.size = Pt(11)
            p.font.bold = True
            p.font.color.rgb = RGBColor(255, 255, 255)
            p.alignment = PP_ALIGN.CENTER
            
    # Populate Table Rows
    if not df_res.empty:
        for r_idx, row in df_res.iterrows():
            row_vals = [
                str(row['Member']),
                str(row['Algorithm']),
                str(row['Best Parameter']),
                f"{row['CV Train Accuracy']*100:.2f}%",
                f"{row['Test Accuracy']*100:.2f}%",
                f"{row['Recall']*100:.2f}%",
                f"{row['F1-Score']*100:.2f}%"
            ]
            for c_idx, val in enumerate(row_vals):
                cell = table.cell(r_idx + 1, c_idx)
                cell.text = val
                cell.fill.solid()
                cell.fill.fore_color.rgb = LIGHT_BG if r_idx % 2 == 0 else RGBColor(255, 255, 255)
                for p in cell.text_frame.paragraphs:
                    p.font.size = Pt(10)
                    p.font.color.rgb = DARK_TEXT
                    p.alignment = PP_ALIGN.CENTER if c_idx >= 3 else PP_ALIGN.LEFT

    # ------------------------------------------------------------------
    # SLIDE 9: Comparative Visualizations & Chart (Speaker: Member 8)
    # ------------------------------------------------------------------
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "Comparative Performance Visualization & Key Takeaways")
    
    chart_img = os.path.join(RESULTS_DIR, 'all_8_algorithms_comparison.png')
    if os.path.exists(chart_img):
        slide9.shapes.add_picture(chart_img, Inches(0.8), Inches(1.5), width=Inches(7.2))
        
    # Right Side Takeaways Card
    c_tk = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.3), Inches(1.5), Inches(4.2), Inches(5.2))
    c_tk.fill.solid()
    c_tk.fill.fore_color.rgb = LIGHT_BG
    c_tk.line.color.rgb = BORDER_GRAY
    tf_tk = c_tk.text_frame
    tf_tk.margin_left = tf_tk.margin_top = Inches(0.25)
    p = tf_tk.paragraphs[0]
    p.text = "Key Analytical Insights"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NAVY
    
    takeaways = [
        "Top Performers: SVM (98.25%) and k-NN (98.25%) achieved highest test accuracy.",
        "Clinical Sensitivity: k-NN achieved 100% recall (0 false negatives), crucial for medical safety.",
        "Smooth Boundaries Win: Neural Networks, SVM & Logistic Regression outperformed tree models due to smooth continuous feature scaling.",
        "Tree Limitations: Single Decision Tree (93.86%) struggled with complex diagonal feature boundaries."
    ]
    for t in takeaways:
        p_t = tf_tk.add_paragraph()
        p_t.text = "• " + t
        p_t.font.size = Pt(11)
        p_t.font.color.rgb = DARK_TEXT

    # ------------------------------------------------------------------
    # SLIDE 10: Conclusion & Discussion (Speaker: Member 8 & Group Leader)
    # ------------------------------------------------------------------
    slide10 = prs.slides.add_slide(blank_layout)
    add_header(slide10, "Discussion, Conclusions & Future Work")
    
    # Left Card: Conclusions
    c_conc = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    c_conc.fill.solid()
    c_conc.fill.fore_color.rgb = LIGHT_BG
    c_conc.line.color.rgb = BORDER_GRAY
    tf_conc = c_conc.text_frame
    tf_conc.margin_left = tf_conc.margin_top = Inches(0.3)
    p = tf_conc.paragraphs[0]
    p.text = "Project Conclusions"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = NAVY
    
    conc_bullets = [
        "Sensitivity analysis is essential: Parameter tuning (e.g., SVM C, MLP topology, GBDT learning rate) improved accuracy by 2% to 35% compared to default settings.",
        "Fair benchmarking validated: Standardized 80/20 split and Z-score scaling enabled rigorous algorithm comparison.",
        "Medical deployment choice: Support Vector Machine (C=5.0) and k-NN (k=3) are recommended for automated FNA diagnosis."
    ]
    for b in conc_bullets:
        p_b = tf_conc.add_paragraph()
        p_b.text = "• " + b
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = DARK_TEXT

    # Right Card: Q&A
    c_qa = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.2))
    c_qa.fill.solid()
    c_qa.fill.fore_color.rgb = NAVY
    c_qa.line.color.rgb = NAVY
    tf_qa = c_qa.text_frame
    tf_qa.margin_left = tf_qa.margin_top = Inches(0.4)
    p_qa = tf_qa.paragraphs[0]
    p_qa.text = "Thank You!"
    p_qa.font.size = Pt(28)
    p_qa.font.bold = True
    p_qa.font.color.rgb = RGBColor(255, 255, 255)
    
    p_qasub = tf_qa.add_paragraph()
    p_qasub.text = "Questions & Discussion"
    p_qasub.font.size = Pt(20)
    p_qasub.font.color.rgb = RGBColor(180, 205, 235)
    
    p_details = tf_qa.add_paragraph()
    p_details.text = "\nCodebase Repository & Results:\nc:\\Users\\palak\\Data_Mining\n\nAll 8 algorithm modules, dataset pipeline, and sensitivity plots ready for grading."
    p_details.font.size = Pt(13)
    p_details.font.color.rgb = RGBColor(220, 230, 245)

    # Save presentation
    ppt_path = os.path.join(PRESENTATION_DIR, 'Group_Project_Presentation.pptx')
    prs.save(ppt_path)
    print(f"\n[SUCCESS] Generated presentation slide deck at '{ppt_path}'!")

if __name__ == "__main__":
    create_presentation()

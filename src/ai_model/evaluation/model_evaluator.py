"""
Model Evaluation Module - Testing and Validation
Final Version Implementation
"""

from sklearn.metrics import (
    accuracy_score, 
    precision_score, 
    recall_score, 
    f1_score,
    confusion_matrix,
    classification_report
)
import numpy as np

class ModelEvaluator:
    """Evaluate vulnerability classification model performance"""
    
    @staticmethod
    def evaluate(y_true, y_pred):
        """
        Comprehensive model evaluation
        Returns accuracy, precision, recall, F1-score
        """
        metrics = {
            'accuracy': accuracy_score(y_true, y_pred),
            'precision': precision_score(y_true, y_pred, average='weighted', zero_division=0),
            'recall': recall_score(y_true, y_pred, average='weighted', zero_division=0),
            'f1_score': f1_score(y_true, y_pred, average='weighted', zero_division=0),
            'confusion_matrix': confusion_matrix(y_true, y_pred).tolist(),
            'classification_report': classification_report(y_true, y_pred, output_dict=True)
        }
        return metrics
    
    @staticmethod
    def print_metrics(metrics):
        """Print evaluation metrics"""
        print("\n=== Model Evaluation Metrics ===")
        print(f"Accuracy:  {metrics['accuracy']:.4f}")
        print(f"Precision: {metrics['precision']:.4f}")
        print(f"Recall:    {metrics['recall']:.4f}")
        print(f"F1-Score:  {metrics['f1_score']:.4f}")
        print("================================\n")

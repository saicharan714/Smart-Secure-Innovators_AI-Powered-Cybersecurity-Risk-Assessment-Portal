"""
Test Suite for AI Model
Unit tests for vulnerability classifier
"""

import unittest
from src.ai_model.vulnerability_classifier import VulnerabilityClassifier
import numpy as np

class TestVulnerabilityClassifier(unittest.TestCase):
    """Test cases for VulnerabilityClassifier"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.classifier = VulnerabilityClassifier()
    
    def test_model_initialization(self):
        """Test model initializes without errors"""
        self.assertIsNone(self.classifier.model)
    
    def test_model_training(self):
        """Test model training functionality"""
        # Generate synthetic training data
        X_train = np.random.rand(100, 10)
        y_train = np.random.randint(0, 3, 100)  # 3 risk levels
        
        self.classifier.train(X_train, y_train)
        self.assertIsNotNone(self.classifier.model)
    
    def test_prediction(self):
        """Test model prediction"""
        X_train = np.random.rand(100, 10)
        y_train = np.random.randint(0, 3, 100)
        self.classifier.train(X_train, y_train)
        
        X_test = np.random.rand(10, 10)
        predictions = self.classifier.predict(X_test)
        
        self.assertEqual(len(predictions), 10)

if __name__ == '__main__':
    unittest.main()

import sys
sys.path.append(".")

from train import train_model

def test_accuracy():
    assert train_model() >= 0.90

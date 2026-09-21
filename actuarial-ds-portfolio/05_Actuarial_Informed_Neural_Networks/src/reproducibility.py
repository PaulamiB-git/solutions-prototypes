"""
Reproducibility utilities for Project 05.

Ensures deterministic behaviour across training runs (when using a fixed seed)
and provides multi-seed execution helpers.
"""

import os
import random
import numpy as np
import tensorflow as tf


def set_seed(seed: int = 42):
    """Set all random seeds for reproducibility."""
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)


def get_seed_list(n_seeds: int = 5) -> list:
    """Return the standard list of seeds for multi-seed robustness analysis."""
    return [42, 77, 256, 512, 1024][:n_seeds]

"""
Global reproducibility configuration.
Sets seeds for all random number generators used in the project.
"""

import os
import random
import numpy as np

GLOBAL_SEED = 42


def set_global_seed(seed=GLOBAL_SEED):
    """
    Fix all random seeds for full reproducibility.
    Must be called before any TensorFlow/Keras imports or operations.
    """
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)

    # TensorFlow seed (imported here to avoid forcing TF import in non-DL notebooks)
    try:
        import tensorflow as tf
        tf.random.set_seed(seed)
        # Force deterministic operations where possible
        os.environ['TF_DETERMINISTIC_OPS'] = '1'
    except ImportError:
        pass

    print(f"[Reproducibility] Global seed set to {seed}")

"""
Custom loss functions for Actuarial-Informed Neural Networks (AINN).

This module implements differentiable actuarial constraint penalties
that can be combined with standard MSE loss during LSTM training.
"""

import tensorflow as tf


def coherence_penalty(k_specific_pred):
    """
    Penalise divergence of country-specific factors from zero.
    
    Li-Lee assumes specific factors are stationary (mean-reverting to zero).
    This penalty acts as a soft regulariser toward cluster coherence.
    
    Args:
        k_specific_pred: Predicted country-specific factors, shape (batch, n_countries).
    
    Returns:
        Scalar penalty (mean squared magnitude of specific factors).
    """
    return tf.reduce_mean(tf.square(k_specific_pred))


def monotonicity_penalty(log_mx_reconstructed, age_start=40, age_end=90):
    """
    Penalise violations of Gompertzian monotonicity in reconstructed mortality.
    
    Mortality must increase with age (m_{x+1} >= m_x) for ages 40-90.
    Penalises any decrease as a squared hinge loss.
    
    Args:
        log_mx_reconstructed: Reconstructed log-mortality rates, shape (batch, n_ages).
        age_start: Start of the monotonicity enforcement range.
        age_end: End of the monotonicity enforcement range.
    
    Returns:
        Scalar penalty (mean squared violation).
    """
    # Differences along the age axis (should be >= 0 for monotonicity)
    age_diffs = log_mx_reconstructed[:, 1:] - log_mx_reconstructed[:, :-1]
    # Only penalise negative differences (violations)
    violations = tf.nn.relu(-age_diffs)
    return tf.reduce_mean(tf.square(violations))


def stationarity_penalty(k_specific_pred):
    """
    Penalise unit-root behaviour in predicted specific factors.
    
    Encourages smooth mean-reversion by penalising large temporal changes
    in country-specific factors.
    
    Args:
        k_specific_pred: Predicted specific factors over time, shape (batch, time, n_countries)
                         or (batch, n_countries) for single-step predictions.
    
    Returns:
        Scalar penalty (mean squared first-difference of specific factors).
    """
    if len(k_specific_pred.shape) == 3:
        # Multi-step: penalise temporal changes
        diffs = k_specific_pred[:, 1:, :] - k_specific_pred[:, :-1, :]
        return tf.reduce_mean(tf.square(diffs))
    else:
        # Single-step: penalty is equivalent to coherence (magnitude)
        return tf.reduce_mean(tf.square(k_specific_pred))


def ainn_loss(y_true, y_pred, k_specific_pred=None, log_mx_reconstructed=None,
              lambda_coherence=0.0, lambda_monotonicity=0.0, lambda_stationarity=0.0):
    """
    Combined AINN loss: MSE + weighted actuarial constraint penalties.
    
    Args:
        y_true: Ground truth targets.
        y_pred: Model predictions.
        k_specific_pred: Predicted country-specific factors (for coherence/stationarity).
        log_mx_reconstructed: Reconstructed log-mortality (for monotonicity).
        lambda_coherence: Weight for coherence penalty.
        lambda_monotonicity: Weight for monotonicity penalty.
        lambda_stationarity: Weight for stationarity penalty.
    
    Returns:
        Total loss (scalar).
    """
    mse = tf.reduce_mean(tf.square(y_true - y_pred))
    
    total_loss = mse
    
    if k_specific_pred is not None and lambda_coherence > 0:
        total_loss += lambda_coherence * coherence_penalty(k_specific_pred)
    
    if log_mx_reconstructed is not None and lambda_monotonicity > 0:
        total_loss += lambda_monotonicity * monotonicity_penalty(log_mx_reconstructed)
    
    if k_specific_pred is not None and lambda_stationarity > 0:
        total_loss += lambda_stationarity * stationarity_penalty(k_specific_pred)
    
    return total_loss

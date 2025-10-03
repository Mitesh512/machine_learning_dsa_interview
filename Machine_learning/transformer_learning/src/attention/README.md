# Self-Attention: Theory, Math & Code

This module explains the self-attention mechanism, its mathematics, and provides a PyTorch implementation.

## What is Self-Attention?
Self-attention allows each position in a sequence to attend to all other positions, enabling context-aware representations.

## Math
Given queries $Q$, keys $K$, and values $V$:

$$Attention(Q, K, V) = softmax(\frac{QK^T}{\sqrt{d_k}})V$$

## Code Example
See `self_attention.py` for a minimal PyTorch implementation.

---

## Exercises
- Visualize attention weights for a toy example.
- Modify the code to support masking.

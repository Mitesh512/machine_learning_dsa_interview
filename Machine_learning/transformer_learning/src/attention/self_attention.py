import torch
import torch.nn as nn
import math

class SelfAttention(nn.Module):
    def __init__(self, embed_size, heads):
        super(SelfAttention, self).__init__()
        self.embed_size = embed_size
        self.heads = heads
        self.head_dim = embed_size // heads
        assert self.head_dim * heads == embed_size
        self.q_linear = nn.Linear(embed_size, embed_size)
        self.k_linear = nn.Linear(embed_size, embed_size)
        self.v_linear = nn.Linear(embed_size, embed_size)
        self.fc_out = nn.Linear(embed_size, embed_size)
    def forward(self, query, key, value, mask=None):
        N = query.shape[0]
        value_len, key_len, query_len = value.shape[1], key.shape[1], query.shape[1]
        query = self.q_linear(query).reshape(N, query_len, self.heads, self.head_dim)
        key = self.k_linear(key).reshape(N, key_len, self.heads, self.head_dim)
        value = self.v_linear(value).reshape(N, value_len, self.heads, self.head_dim)
        query = query.transpose(1, 2)
        key = key.transpose(1, 2)
        value = value.transpose(1, 2)
        energy = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(self.head_dim)
        if mask is not None:
            energy = energy.masked_fill(mask == 0, float('-1e20'))
        attention = torch.softmax(energy, dim=-1)
        out = torch.matmul(attention, value)
        out = out.transpose(1, 2).contiguous().reshape(N, query_len, self.embed_size)
        return self.fc_out(out)

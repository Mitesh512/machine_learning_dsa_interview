import torch
import torch.nn as nn
from src.attention.self_attention import SelfAttention

class TransformerEncoderLayer(nn.Module):
    def __init__(self, embed_size, heads, dropout, forward_expansion):
        super(TransformerEncoderLayer, self).__init__()
        self.attention = SelfAttention(embed_size, heads)
        self.norm1 = nn.LayerNorm(embed_size)
        self.norm2 = nn.LayerNorm(embed_size)
        self.feed_forward = nn.Sequential(
            nn.Linear(embed_size, forward_expansion * embed_size),
            nn.ReLU(),
            nn.Linear(forward_expansion * embed_size, embed_size),
        )
        self.dropout = nn.Dropout(dropout)
    def forward(self, x, mask=None):
        attention = self.attention(x, x, x, mask)
        x = self.norm1(attention + x)
        x = self.dropout(x)
        forward = self.feed_forward(x)
        out = self.norm2(forward + x)
        out = self.dropout(out)
        return out

class TransformerEncoder(nn.Module):
    def __init__(self, embed_size, num_layers, heads, device, forward_expansion, dropout, max_length):
        super(TransformerEncoder, self).__init__()
        self.embed_size = embed_size
        self.device = device
        self.position_embedding = nn.Embedding(max_length, embed_size)
        self.layers = nn.ModuleList([
            TransformerEncoderLayer(
                embed_size,
                heads,
                dropout=dropout,
                forward_expansion=forward_expansion,
            )
            for _ in range(num_layers)
        ])
        self.dropout = nn.Dropout(dropout)
    def forward(self, x, mask=None):
        N, seq_length = x.shape[0], x.shape[1]
        positions = torch.arange(0, seq_length).expand(N, seq_length).to(self.device)
        out = self.dropout(x + self.position_embedding(positions))
        for layer in self.layers:
            out = layer(out, mask)
        return out

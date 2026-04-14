from typing_extensions import Self
import math
import torch
import torch.nn as nn

print(torch.__version__)
print(f'CUDA available: {torch.cuda.is_available()}')
print(f'Device name: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else "None"}')


# class TokenEmbedding(nn.Module):
#     super(TokenEmbedding, Self).__init__()
#     self.vocab_size = vocab_size
#     self.d_model = d_model
#     pass
import torch
print("CUDA 是否可用：", torch.cuda.is_available())
print("CUDA 版本：", torch.version.cuda)
print("cuDNN 是否可用：", torch.backends.cudnn.is_available())


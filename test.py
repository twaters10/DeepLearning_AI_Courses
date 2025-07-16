import torch

if torch.backends.mps.is_available():
    device = torch.device("mps")
    print("Using Apple GPU with Metal backend.")
else:
    device = torch.device("cpu")
    print("Using CPU.")

x = torch.rand(1000, 1000).to(device) # Move tensor to GPU
y = torch.rand(1000, 1000).to(device)
z = x + y
print(f"Tensor z is on device: {z.device}")

# import tensorflow as tf

# # Check if a GPU is available
# if tf.config.list_physical_devices('GPU'):
#     print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
#     device = tf.device('/GPU:0')
# else:
#     print("No GPU found, using CPU.")
#     device = tf.device('/CPU:0')
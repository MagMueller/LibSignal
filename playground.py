import torch 
# check if mps is available
if torch.backends.mps.is_available():
    print("MPS is available")
else:
    print("MPS is not available")

# repeat the same process and ckeck time
import time

start_time = time.time()

for i in range(300):
    x = torch.randn(1000, 1000)
    y = torch.randn(1000, 1000)
    z = x + y
    if i % 10 == 0:
        print("Iteration", i, "completed")
end_time = time.time()

print(f"Time taken: {end_time - start_time} seconds")


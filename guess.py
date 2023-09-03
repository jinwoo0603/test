import numpy as np
slb = np.array([chr(code) for code in range(44032, 55204)])
slb = slb.reshape(19, 21, 28)
print(slb)
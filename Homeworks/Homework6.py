#How Many Plots?
import numpy as np
import matplotlib.pyplot as plt

def sinusoid(x, A, w):
    return A * np.sin(w * x)
x = np.linspace(0, 2 * np.pi, 1000)
Avalues = np.array([1, 2, 3, 4, 5])  
wvalues = np.array([1, 2, 3, 4, 5])  
plt.figure()

for A in Avalues:
    for w in wvalues:
        y = sinusoid(x, A, w)
        plt.plot(x, y)
plt.title("Sinusoids for Different Amplitude (A) and Frequency (w) Values")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

#Randomness
import numpy as np
import matplotlib.pyplot as plt

list1 = np.random.randint(0, 101, 40) 
list2 = np.random.randint(0, 101, 40)  
plt.figure(figsize=(10, 6))
plt.plot(list1, color="orange", linewidth=10, label="List 1 (Orange)")
plt.plot(list2, color="red", linestyle="--", label="List 2 (Red, Dashed)")
plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Random Data from Two Lists")
plt.legend()
plt.show()

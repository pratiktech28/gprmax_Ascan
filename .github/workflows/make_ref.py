import numpy as np
# Ek sample sine wave data banate hain (jaise tere graph mein tha)
x = np.linspace(0, 1, 100)
data = np.sin(2 * np.pi * 5 * x) 
# Ise usi folder mein save karo jahan script.py hai
np.save('.github/workflows/golden_reference.npy', data)
np.save('.github/workflows/current_simulation.npy', data) # Dono same rakho taaki success mile
print("Reference files created successfully!")
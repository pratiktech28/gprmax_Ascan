import numpy as np
import matplotlib.pyplot as plt
import sys

def calculate_nrmse(reference, current):
    rmse = np.sqrt(np.mean((reference - current) ** 2))
    return rmse / (np.max(reference) - np.min(reference))

# Data Load karna (Assuming .npy or text files)
try:
    ref_data = np.load('golden_reference.npy')
    cur_data = np.load('current_simulation.npy')
    
    nrmse = calculate_nrmse(ref_data, cur_data)
    print(f"NRMSE Calculated: {nrmse}")

    # Plotting for Proof
    plt.figure(figsize=(10, 5))
    plt.plot(ref_data, label='Golden Reference', linestyle='--')
    plt.plot(cur_data, label='Current Simulation', alpha=0.7)
    plt.title(f'A-scan Validation (NRMSE: {nrmse:.5f})')
    plt.legend()
    plt.savefig('ascan_comparison.png') # Ye artifact banega

    # Threshold Check (0.01 se kam hona chahiye)
    if nrmse > 0.01:
        print("Data Integrity Check Failed!")
        sys.exit(1)
    else:
        print("Data Integrity Check Passed!")
        sys.exit(0)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
import numpy as np
import matplotlib.pyplot as plt

print("\n--- First-Order Thermal System Step Response ---\n")

# 1. Input: Final Temperature
T_final = float(input("Enter final steady-state temperature (e.g., 100): "))

# 2. Input: Time constants
tau_input = input("Enter time constants (comma-separated, e.g., 2,5,10): ")
taus = [float(t.strip()) for t in tau_input.split(',')]

# 3. Time array (based on largest tau)
t_max = 6 * max(taus)
t = np.linspace(0, t_max, 300)

# 4. Create plot
plt.figure(figsize=(10, 6))

# 5. Plot curves for each tau
for tau in taus:
    T = T_final * (1 - np.exp(-t / tau))
    plt.plot(t, T, label=f'τ = {tau}', linewidth=2)

    # Mark the time constant point (63%)
    T_tau = T_final * (1 - np.exp(-1))
    plt.scatter(tau, T_tau)

# 6. Add 63% reference line
T_tau = T_final * (1 - np.exp(-1))
plt.axhline(y=T_tau, linestyle='--', label=f'63.2% Level ({T_tau:.1f})')

# 7. Labels and title
plt.title('Step Response of First-Order Thermal Systems')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.grid(True)
plt.legend()

# 8. Show plot
plt.show()

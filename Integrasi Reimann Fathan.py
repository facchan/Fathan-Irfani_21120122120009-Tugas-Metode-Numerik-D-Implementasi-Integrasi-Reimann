import time
import numpy as np
import matplotlib.pyplot as plt

#Fathan Irfani
#21120122120009
#Integrasi Metode Reimann
#Metode Numerik D


# Hitung integral metode Reimann
def riemann_integral(f, a, b, N):
    x = np.linspace(a, b, N+1)
    dx = (b - a) / N
    midpoints = (x[:-1] + x[1:]) / 2
    integral = np.sum(f(midpoints) * dx)
    return integral

# f(x) = 4 / (1 + x**2)
def f(x):
    return 4 / (1 + x**2)

# Batas integral
a = 0
b = 1

# Nilai untuk pi
pi_reference = 3.14159265358979323846

# Variasi N
N_values = [10, 100, 1000, 10000]

# hasil
results = []

# Loop integral, galat RMS, dan waktu eksekusi
for N in N_values:
    start_time = time.time()
    pi_approx = riemann_integral(f, a, b, N)
    end_time = time.time()
    
    # Menghitung galat RMS
    rms_error = np.sqrt((pi_approx - pi_reference) ** 2)
    
    # waktu eksekusi
    execution_time = end_time - start_time
    
    results.append((N, pi_approx, rms_error, execution_time))


print(f"{'N':>10} {'Pi Approximation':>20} {'RMS Error':>20} {'Execution Time (s)':>20}")
for result in results: 
    print(f"{result[0]:>10} {result[1]:>20.15f} {result[2]:>20.15f} {result[3]:>20.15f}")

# Pisahkan hasil ke dalam array terpisah
N_array = np.array([result[0] for result in results])
pi_approx_array = np.array([result[1] for result in results])
rms_error_array = np.array([result[2] for result in results])
execution_time_array = np.array([result[3] for result in results])

# plot
plt.figure(figsize=(14, 6))

# Plot galat RMS
plt.subplot(1, 2, 1)
plt.plot(N_array, rms_error_array, 'o-', color='blue')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N (Jumlah Segmen)')
plt.ylabel('RMS Error')
plt.title('RMS Error vs Jumlah Segmen')
plt.grid(True)

# Plot waktu eksekusi
plt.subplot(1, 2, 2)
plt.plot(N_array, execution_time_array, 'o-', color='red')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N (Jumlah Segmen)')
plt.ylabel('Execution Time (s)')
plt.title('Execution Time vs Jumlah Segmen')
plt.grid(True)

# Tampilkan plot
plt.tight_layout()
plt.show()

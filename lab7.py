from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np
import time
#task 1
start = time.perf_counter()
arr1 = np.random.rand(1000000)
arr2 = np.random.rand(1000000)
np.multiply(arr1, arr2)
print(np.multiply(arr1, arr2))
end = time.perf_counter()
print(end-start)


#task 2
time = []
temperature = []
turnovers = []
i = 0
with open('D:\VScode\lab7\data1.txt', 'r') as txt_file:
    for line in txt_file:
        parts = line.split(';')
        if i > 0:
            time.append(parts[0])
            temperature.append(parts[1])
            turnovers.append(parts[4])
        i += 1
        
time = list(map(float, time))

plt.figure(figsize=(10, 6))
plt.plot(time, temperature, label='Temperature', color='blue')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Time vs Temperature')

plt.plot(time, turnovers, label='Turnovers', color='red')
plt.ylabel('Turnovers')
plt.title('Time vs Turnovers')
plt.show()

plt.figure(figsize=(6, 4))
plt.scatter(temperature, turnovers, color='green')
plt.xlabel('Temperature')
plt.ylabel('Turnovers')
plt.title('Temperature vs Turnovers Correlation')
plt.show()

#task 3
x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x) * np.cos(x)
z = np.sin(x)

# Создаем трехмерную графику
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

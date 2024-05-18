import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Configurar los valores de omega a lo largo del tiempo
tiempo_total = 10  # Duración total en segundos
frames = 200  # Número de frames en la animación

# Definir una función para actualizar el gráfico en cada frame
def update(num, ax, fig):
    ax.cla()  # Limpiar el gráfico actual para dibujar el nuevo frame
    t = num / frames * tiempo_total  # Calcular el valor actual del tiempo
    omega = 2 * np.pi * t  # Omega varía linealmente con el tiempo
    x = np.cos(omega)
    y = -np.sin(omega)
    z = t  # Usar el tiempo como la tercera dimensión para el eje z

    # Dibujar la espiral trigonométrica
    t_vals = np.linspace(0, t, 1000)
    x_spiral = np.cos(2 * np.pi * t_vals)
    y_spiral = -np.sin(2 * np.pi * t_vals)
    z_spiral = t_vals
    ax.plot(x_spiral, y_spiral, z_spiral, label='Espiral', color='gray', alpha=0.5)

    # Dibujar el vector del fasor
    ax.quiver(0, 0, z-0.1, x, y, 0, length=0.5, normalize=True, color='b')

    # Configurar las características del gráfico
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([0, tiempo_total])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Tiempo (s)')
    ax.view_init(elev=20., azim=num*3)  # Cambiar la vista para rotar el gráfico

# Crear la figura y los ejes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crear la animación
ani = FuncAnimation(fig, update, frames=frames, fargs=(ax, fig), interval=50)

# Mostrar la animación
plt.show()

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(15, 7))

x = np.linspace(4, 10, 100)
y = np.linspace(4, 10, 100)
X, Y = np.meshgrid(x, y)

Z1 = X**0.25 + Y**0.25
ax1 = fig.add_subplot(231, projection='3d')
ax1.plot_surface(X, Y, Z1, cmap='cool')
ax1.set_title("z = x^0.25+y^0.25")
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

Z2 = X**2 - Y**2
ax2 = fig.add_subplot(232, projection='3d')
ax2.plot_surface(X, Y, Z2, cmap='inferno')
ax2.set_title('z = x^2 - y^2')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

Z3 = 2*X + 3*Y
ax3 = fig.add_subplot(233, projection='3d')
ax3.plot_surface(X, Y, Z3, cmap='viridis')
ax3.set_title('z = 2x + 3y')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')

Z4 = X**2 + Y**2
ax4 = fig.add_subplot(234, projection='3d')
ax4.plot_surface(X, Y, Z4, cmap='winter')
ax4.set_title('z = x^2 + y^2')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Z')

Z5 = 2 + 2*X + 2*Y - X**2 - Y**2
ax5 = fig.add_subplot(235, projection='3d')
ax5.plot_surface(X, Y, Z5, cmap='summer')
ax5.set_title('z = 2 + 2x + 2y - x^2 - y^2')
ax5.set_xlabel('X')
ax5.set_ylabel('Y')
ax5.set_zlabel('Z')

plt.tight_layout() 
plt.show()
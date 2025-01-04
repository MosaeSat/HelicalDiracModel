import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from galpy.potential import MiyamotoNagaiPotential, HernquistPotential, MWPotential2014
from galpy.orbit import Orbit

# Define Galactic Potential with a Central Black Hole
black_hole_potential = HernquistPotential(a=0.01, amp=1.0)  # Black hole potential
disk_potential = MiyamotoNagaiPotential(a=3.0, b=0.1, amp=1.0)  # Disk potential
combined_potential = [MWPotential2014, black_hole_potential, disk_potential]

# Initial Conditions for the Orbit (Helical Path)
R0 = 1.0  # Initial radial position (kpc)
vR0 = 0.1  # Radial velocity (kpc/Myr)
vT0 = 1.0  # Tangential velocity (kpc/Myr)
z0 = 0.1  # Vertical position (kpc)
vz0 = 0.2  # Vertical velocity (kpc/Myr)
phi0 = 0.0  # Initial angle (rad)

# Create Orbit Object
o = Orbit(vxvv=[R0, vR0, vT0, z0, vz0, phi0], ro=8.0, vo=220.0)

# Integrate the Orbit in Combined Potential
times = np.linspace(0, 200, 2000)  # Time in Myr
o.integrate(times, combined_potential)

# 3D Plot: Helical Path with Central Potential
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(o.x(times), o.y(times), o.z(times), label='Helical Orbit')

# Add the black hole as a point at the origin
ax.scatter(0, 0, 0, color='black', s=100, label='Black Hole')

# Add vectors to show angular momentum direction
for i in range(0, len(times), 200):  # Plot every 200th point
    ax.quiver(o.x(times[i]), o.y(times[i]), o.z(times[i]),
              o.vx(times[i]), o.vy(times[i]), o.vz(times[i]),
              color='red', length=0.5, normalize=True)

# Labels and Title
ax.set_xlabel('X (kpc)')
ax.set_ylabel('Y (kpc)')
ax.set_zlabel('Z (kpc)')
ax.set_title('Helical Orbit with Black Hole and Stress Vectors')
ax.legend()

# Show the plot
plt.show()

# Energy and Angular Momentum Analysis
energy = o.E(times, pot=combined_potential)  # Total energy over time
lz = o.Lz(times)  # Angular momentum along the z-axis

# Plot Energy vs Time
plt.figure(figsize=(8, 5))
plt.plot(times, energy, label='Total Energy')
plt.xlabel('Time (Myr)')
plt.ylabel('Energy (kpc^2/Myr^2)')
plt.title('Energy Conservation Over Time')
plt.legend()
plt.grid(True)
plt.show()

# Plot Angular Momentum vs Time
plt.figure(figsize=(8, 5))
plt.plot(times, lz, label='Angular Momentum (Lz)')
plt.xlabel('Time (Myr)')
plt.ylabel('Lz (kpc^2/Myr)')
plt.title('Angular Momentum Conservation Over Time')
plt.legend()
plt.grid(True)
plt.show()

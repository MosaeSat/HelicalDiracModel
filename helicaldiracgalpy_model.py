# ===================================================================
# Title: Helical Orbit Simulation with Black Hole and Galactic Disk
# Author: F. Hanna Campbell / mods with chatGPT 4o formating
# License: MIT License
# Date: 2024
#
# Description:
# This script experimentally simulates the helical dynamics of imaginary stars and planetary objects
# influenced by black holes using Galpy, by simulating their orbits under the combined gravitational 
# potential of these structures.  It models rotational stability and stress redistribution, 
# visualizing trajectories and conservation properties.
#
# Features:
# - 3D visualization of helical orbits affected by central black holes.
# - Energy and angular momentum conservation plots.
# - Editable parameters for black hole and disk potentials.
#
# Dependencies:
# - Python 3.7 or later
# - Packages: galpy, matplotlib, numpy
# ===================================================================

# -----------------------
# Import Required Libraries
# -----------------------
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from galpy.potential import MiyamotoNagaiPotential, HernquistPotential, MWPotential2014
from galpy.orbit import Orbit

# -----------------------
# Define Galactic Potentials
# -----------------------
# Black Hole Potential
# Users can adjust the scale (a) and amplitude (amp) to modify black hole strength.
black_hole_potential = HernquistPotential(a=0.01, amp=1.0)  # Default: Compact black hole

# Disk Potential
# Customize parameters a and b to change the disk size and density.
disk_potential = MiyamotoNagaiPotential(a=3.0, b=0.1, amp=1.0)  # Flattened disk

# Combine Potentials (Includes Milky Way Default Potential)
combined_potential = [MWPotential2014, black_hole_potential, disk_potential]

# -----------------------
# Initial Conditions
# -----------------------
# Set starting position and velocities for the orbit.
R0 = 1.0      # Radial position (kpc)
vR0 = 0.1     # Radial velocity (kpc/Myr)
vT0 = 1.0     # Tangential velocity (kpc/Myr)
z0 = 0.1      # Vertical position (kpc)
vz0 = 0.2     # Vertical velocity (kpc/Myr)
phi0 = 0.0    # Initial angle (rad)

# Create Orbit Object
o = Orbit(vxvv=[R0, vR0, vT0, z0, vz0, phi0], ro=8.0, vo=220.0)

# -----------------------
# Integrate Orbit in Time
# -----------------------
# Time array for simulation (adjust range and steps as needed).
times = np.linspace(0, 200, 2000)  # Time in Myr
o.integrate(times, combined_potential)

# -----------------------
# Visualization: 3D Helical Path
# -----------------------
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the helical trajectory
ax.plot(o.x(times), o.y(times), o.z(times), label='Helical Orbit')

# Mark the black hole at the origin
ax.scatter(0, 0, 0, color='black', s=100, label='Black Hole')

# Display angular momentum vectors (edit length and frequency if needed).
for i in range(0, len(times), 200):  # Show every 200th point
    ax.quiver(o.x(times[i]), o.y(times[i]), o.z(times[i]),
              o.vx(times[i]), o.vy(times[i]), o.vz(times[i]),
              color='red', length=0.5, normalize=True)

# Add Labels
ax.set_xlabel('X (kpc)')
ax.set_ylabel('Y (kpc)')
ax.set_zlabel('Z (kpc)')
ax.set_title('Helical Orbit with Black Hole and Stress Vectors')
ax.legend()
plt.show()

# -----------------------
# Conservation of Energy and Angular Momentum Analysis
# -----------------------
# Calculate energy over time
energy = o.E(times, pot=combined_potential)  # Total energy
lz = o.Lz(times)  # Angular momentum along the z-axis

# Energy vs. Time Plot to check the stability of the motion
plt.figure(figsize=(8, 5))
plt.plot(times, energy, label='Total Energy') # tracks how total energy oscillates, verifying conservation during orbital transitions
plt.xlabel('Time (Myr)')
plt.ylabel('Energy (kpc^2/Myr^2)')
plt.title('Energy Conservation Over Time')
plt.legend()
plt.grid(True)
plt.show()

# Angular Momentum vs. Time Plot which tests whether rotational stability holds, validating the Dirac twisted belt analogy.
plt.figure(figsize=(8, 5))
plt.plot(times, lz, label='Angular Momentum (Lz)')
plt.xlabel('Time (Myr)')
plt.ylabel('Lz (kpc^2/Myr)')
plt.title('Angular Momentum Conservation Over Time')
plt.legend()
plt.grid(True)
plt.show()

# -----------------------
# Notes for Further Exploration
# -----------------------
# 1. Experiment with disk and black hole parameters to test different scenarios.
# 2. Analyze perturbations to simulate torsional stress redistribution effects.
# 3. Compare with observational data from Sagittarius A* and M87*.
# 4. Add relativistic corrections for Kerr metrics if needed.

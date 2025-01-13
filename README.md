# HelicalDiracModel

This repository contains the code and resources for the paper:

**"A Unified Rotational Model of Black Holes and Galactic Dynamics: The Helical Path and Dirac Twisted Belt Phenomenon"**  
*Author: F. Hanna Campbell*  https://doi.org/10.5281/zenodo.14639156
*Date: 2024*  

---

## Overview

This project presents a novel framework that models the helical dynamics of stars and planetary objects influenced by black holes. It focuses on rotational stability and stress redistribution through multidimensional compensation mechanisms, using the **Dirac twisted belt analogy** as a theoretical foundation.  

## Attribution and Citation  

If you use this code in your research or projects, please cite the following:  

Farida Hanna Campbell,M.E.B.E. (2024-2025)  Mosae Zorg Industries (Maastricht, NL)
**"A Unified Rotational Model of Black Holes and Galactic Dynamics: The Helical Path and Dirac Twisted Belt Phenomenon,"**  

For proper acknowledgment, include a link to this repository and the author's contact information.  
See also 

## Relevance to Einstein Telescope (ET) Projects

This model can potentially be adapted for **Einstein Telescope (ET)** projects, especially in areas related to **gravitational wave detection** and **black hole dynamics modeling**.  

### Applications:
- **Gravitational Wave Source Modeling:**  
  Simulates orbital dynamics near black holes, which can predict **gravitational wave signatures** emitted by compact binaries or merging black holes. The model can provide test cases for verifying signals detected by the **Einstein Telescope**.

- **Testing Alternative Theories of Gravity:**  
  Models stress redistribution and torsional stability, potentially relevant for **alternative gravitational theories** and **higher-dimensional models** studied by the Einstein Telescope.

- **Multidimensional Effects:**  
  The **helical dynamics** and **Dirac twisted belt analogy** offer insights into **multidimensional compensatory mechanisms** that may influence gravitational waveforms.

- **Orbit Stability in Extreme Fields:**  
  Simulates dynamics near **supermassive black holes** (e.g., **Sagittarius A***), applicable for detecting **low-frequency gravitational waves** targeted by the **Einstein Telescope**.

---

## Why the Milky Way Potential?

The script includes the **Milky Way potential** (`MWPotential2014`) as a **default galactic framework** in **Galpy**. It represents the gravitational influence of the Milky Way's **disk, bulge, and halo**, making it suitable for modeling **stellar orbits** near **Sagittarius A***—the **supermassive black hole** at the center of the Milky Way.

### Key Reasons:
1. **Baseline Framework:** Provides a realistic gravitational background for testing generic orbits influenced by a central black hole.
2. **Supermassive Black Hole in Milky Way:** Models dynamics near **Sagittarius A***, the **4-million-solar-mass** black hole at the Milky Way's core.
3. **Scalable and Customizable:** Users can easily **replace or modify** the potential to study other galaxies, isolated black holes, or exotic systems.

### Customization Options:
- **Remove Milky Way Influence:** Use only the black hole and disk potentials:
  ```python
  combined_potential = [black_hole_potential, disk_potential]
  ```
- **Study External Galaxies:** Replace the Milky Way model with custom elliptical or early-universe potentials.

This flexibility allows exploration of scenarios ranging from **isolated black holes** to **galaxies like M87** with **larger black holes**.

---

## Steps to Run the Code

**Note:** If you do not have Python installed, download and install it from [python.org](https://python.org). Use **Python 3.7 or later** for compatibility with Galpy. Virtual environments are recommended for dependency management.  

### 1. Install Dependencies:
```bash
pip install galpy matplotlib
```

### 2. Save the Python Script:
Save the provided Python code as `galpy_model.py` or run it directly in **Jupyter Notebook**.  

### 3. Execute the Script:
Run the script in your Python environment to generate:  
- **3D Helical Orbit** — visualizing the trajectory influenced by the black hole and galactic disk.  
- **Energy vs. Time Plot** — to verify conservation of energy.  
- **Angular Momentum vs. Time Plot** — to test rotational stability and torsional effects.  

---

## Expected Outputs

### 3D Helical Orbit:
A trajectory showing **helical motion** influenced by central black holes and disk potentials.  

### Energy vs. Time Plot:
Demonstrates **periodic exchanges** between **kinetic and potential energy**.  

### Angular Momentum vs. Time Plot:
Verifies **angular momentum conservation**, reinforcing the stability of torsional stresses.  

---
## Run in Google Colab  

You can also run this model directly in Google Colab:  

[Open in Google Colab](https://colab.research.google.com/drive/1-uukQnAdUyL_ibgOdEnpwYpoOXfQ7FBv?authuser=1)

## Troubleshooting

### Issue 1: "ModuleNotFoundError" for `galpy` or `matplotlib`
**Solution:** Ensure dependencies are installed by running:  
```bash
pip install galpy matplotlib
```

### Issue 2: Graphs or Plots Not Displaying
**Solution:** If using Jupyter Notebook, include the following line before running the code:  
```python
%matplotlib inline
```

---

## Next Steps

### Parameter Tuning:
- Test perturbations or changes to **initial conditions** to simulate **torsional stress redistribution**.  

### Comparison with Observations:
- Match results with data from **Sagittarius A***, **M87***, and **gravitational wave signals** detected by **LIGO**.  

### Higher-Dimensional Extensions:
- Explore effects of **multidimensional compensation mechanisms** beyond **Kerr metrics**.  

### Relativistic Extensions:
- Investigate **relativistic corrections** and **frame-dragging effects** based on the **Kerr metric** for more accurate predictions.  

### Observational Data Matching:
- Integrate **star trajectories** or **gravitational wave observations** to test model predictions.  

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.  

---

## Contact and Contributions

For inquiries, feel free to contact:  
**Farida Hanna Campbell**  
Email: [FHCampbell@MosaeZorg.com](mailto:FHCampbell@MosaeZorg.com)  

**Contributions are welcome!**  
Please submit pull requests or raise issues for enhancements.

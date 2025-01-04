# HelicalDiracModel

This repository contains the code and resources for the paper:

**"A Unified Rotational Model of Black Holes and Galactic Dynamics: The Helical Path and Dirac Twisted Belt Phenomenon"**  
**Author:** F. Hanna Campbell, M.E.,B.E.
**Date:** 2024-01-04

---

## **Overview**

This project presents a novel framework that models the **helical dynamics** of stars and planetary objects influenced by black holes. It focuses on **rotational stability** and **stress redistribution** through multidimensional compensation mechanisms, using the **Dirac twisted belt** analogy as a theoretical foundation.

---

### **How This Approach Differs from Hawking’s Work:**  

Stephen Hawking’s research primarily revolved around **black hole thermodynamics**, **event horizons**, and the **information paradox**, emphasizing black holes as thermal systems governed by entropy principles. Hawking proposed that black holes emit **Hawking radiation**, leading to gradual mass loss and evaporation over time.  

**Key Difference:**  
This model treats black holes as **dynamic energy redistribution nodes** rather than thermally isolated objects. Instead of focusing on entropy and thermal dissipation, it examines:  

- **Rotational energy conservation**  
- **Torsional stability**  

Black holes in this framework redistribute rotational stresses through **multidimensional compensatory mechanisms**, forming structures analogous to the **Dirac twisted belt** to stabilize surrounding dynamics.  

---

### **Key Contributions of this Model:**  

- Models **rotational stability** and **helical trajectories** influenced by central black holes and galactic disks.  
- Uses **Galpy** numerical simulations to demonstrate **energy and angular momentum conservation**.  
- Explores **topological structures** and **multidimensional compensation** as mechanisms for stress redistribution, offering an alternative to thermodynamic frameworks.  
- Provides **visualizations** to validate dynamic stability, linking the model to observational possibilities such as **gravitational waves** and **Kerr metric precessions**.  

This model builds a bridge between **theoretical predictions** and **observational data**, including recent findings from gravitational wave events and black hole imaging (e.g., **Event Horizon Telescope**). It highlights the potential for further exploration through comparisons with **LIGO/Virgo gravitational wave signals** and **trajectories of stars near Sagittarius A***.  

---

## Run in Google Colab  

You can also run this model directly in Google Colab:  

[Open in Google Colab](https://colab.research.google.com/drive/1-uukQnAdUyL_ibgOdEnpwYpoOXfQ7FBv?authuser=1)


## **Steps to Run the Code**  

**Note:** If you do not have Python installed, download and install it from [python.org](https://python.org). Use **Python 3.7 or later** for compatibility with Galpy. Virtual environments are recommended for dependency management.  

### **1. Install Dependencies:**  
```bash
pip install galpy matplotlib
```

### **2. Save the Python Script:**  
Save the provided Python code as **`galpy_model.py`** or run it directly in **Jupyter Notebook**.  

---

### **3. Execute the Script:**  
Run the script in your Python environment to generate:  

- **3D Helical Orbit** — visualizing the trajectory influenced by the black hole and galactic disk.  
- **Energy vs. Time Plot** — to verify conservation of energy.  
- **Angular Momentum vs. Time Plot** — to test rotational stability and torsional effects.  

---

## **Expected Outputs**  

### **3D Helical Orbit:**  
A trajectory showing **helical motion** influenced by central black holes and disk potentials.  

### **Energy vs. Time Plot:**  
Demonstrates **periodic exchanges** between **kinetic and potential energy**.  

### **Angular Momentum vs. Time Plot:**  
Verifies **angular momentum conservation**, reinforcing the stability of torsional stresses.  

---

## **Troubleshooting**  

### **Issue 1:** `"ModuleNotFoundError"` for `galpy` or `matplotlib`  
**Solution:** Ensure dependencies are installed by running:  
```bash
pip install galpy matplotlib
```

### **Issue 2:** Graphs or Plots Not Displaying  
**Solution:** If using Jupyter Notebook, include the following line before running the code:  
```python
%matplotlib inline
```

---

## **Next Steps**  

### **Parameter Tuning:**  
- Test perturbations or changes to initial conditions to simulate torsional stress redistribution.  

### **Comparison with Observations:**  
- Match results with data from **Sagittarius A***, **M87***, and gravitational wave signals detected by **LIGO**.  

### **Higher-Dimensional Extensions:**  
- Explore effects of multidimensional compensation mechanisms beyond Kerr metrics.  

### **Relativistic Extensions:**  
- Investigate relativistic corrections and frame-dragging effects based on the Kerr metric for more accurate predictions.  

### **Observational Data Matching:**  
- Integrate star trajectories or gravitational wave observations to test model predictions.  

---

## **License**  

This project is licensed under the **MIT License** — see the LICENSE file for details.  

---

## **Contact and Contributions**  

For inquiries, feel free to contact:  
**F. Hanna Campbell**  
**Email:** FHCampbell@MosaeZorg.com  

**Contributions are welcome!**  
Please submit pull requests or raise issues for enhancements.

# EPyT-C: A Python package for water quality modeling in water distribution systems

tags: EPANET; Python; water quality; chlorine; bacteria

authors:
  - name: Gopinathan R. Abhijith
    orcid: 0000-0002-7390-7848
    affiliation: 1
    corresponding: true
  - name: Avi Ostfeld
    affiliation: 2

affiliations:
 - name: Gopinathan R. Abhijith, Assistant Professor, BITS Pilani Hyderabad Campus, Telanagana, India
   index: 1
 - name: Avi Ostfeld, Technion - Israel Institite of Technology, Haifa, Isrel
   index: 2


# Summary

Water distribution systems (WDS) comprise numerous components, such as reservoirs, tanks, pipes, and hydraulic control elements. Inarguably they are one of the most critical infrastructures of every society. At the same time, they are vulnerable to accidents, attacks, and related public health risks owing to their spatial spread and accessibility. Computer-based tools that simulate water quality variations in WDS are functional solutions for monitoring WDS integrity. This paper presents EPyT-C (in which C stands for contaminant), a Python-based package allowing the simulation of the transport and fate of multiple water quality parameters in WDS. EPyT-C constitute in-built modules that conceptualize the scientific understanding of the physical, physicochemical, and biochemical interactions concerning water quality parameters within the distribution network realm, mathematize them as one-dimensional advective-reactive equations, and numerically solve them to emulate the spatiotemporal distribution of the quality of water delivered via WDS. 

# Statement of need

Generally, computer-based water quality simulation tools for WDS built on mathematical models depict the time-series behavior of water quality parameters within the spatial peripheries of WDS. EPANET-MSX [(Shang et al., 2007)](#5) has become the de-facto WDS water quality modeling tool due to its direct collaboration with EPANET 2.0 [(Rossman et al., 2000)](#3), the most commonly used software package for WDS modeling. Nevertheless, two challenges are encountered while using EPANET-MSX for WDS water quality modeling. They are (a) the conceptualization of the physical, physicochemical, and biochemical interactions between water quality parameters and (b) the evolution of scientific depictions (generating mathematical expressions) of these interactions. In addition, owing to its complex user interface, the EPANET-MSX application requires programming knowledge. To overcome these limitations of the EPANET-MSX application, [Abhijith and Ostfeld (2022)](#2) have built EPANET-C, which comprises in-built function directories integrating all the input information required for executing EPANET-MSX. EPANET-C also simplified EPANET-MSX execution by providing a simple command-line MATLAB interface with an exhaustive set of instructions. 

However, EPANET-C, utilizing EPANET-MSX solver for solving advective-reactive equations, can be quite computationally intensive when solving stiff equations [(Abhijith and Ostfeld, 2021)](#1). Also, EPANET-C is based on MATLAB, a commercial numeric computing environment. If available in Python, a user-friendly and more portable open-source language, such a simulation tool could become accessible to the scientific community and water supply managers. This paper presents EPyT-C, an open-source umbrella WDS water quality modeling tool based on the recently developed EPANET-Python Toolkit (EPyT) to help researchers and practitioners in the WDS analysis domain. Users are welcome to further develop, improve and extend these open-source scripts. Above and beyond, further modifications will be added to enhance the capability of EPyT-C to simulate the fate and transport of numerous water quality parameters and to introduce the effects of dispersion in WDS water quality modeling.

# Functionality

EPyT is an open-source software, initially developed by the KIOS Research and Innovation Center of Excellence, University of Cyprus, operating within the Python environment to provide a programming interface for the latest version of EPANET 2.2 [(Rossman et al., 2020)](#4). It calls EPANET a shared object and employs an Object-Oriented approach for interfacing EPANET with Python. Though EPyT can be employed for performing single-species water quality analysis, which comes within the scope of EPANET 2.2, it lacks multi-species reactive-transport modeling capability in its current form. In other words, EPyT can only analyze one water quality parameter at a time. Consequently, the water quality modeling compartment of EPyT needs to be improved to solve several real-world problems concerning water quality variations during delivery via WDS. A fully independent water quality modeling extension, EPyT-C, is developed in this direction. The source code of EPyT-C calls EPyT and employs the hydraulic solver of EPANET 2.2 for performing hydraulic simulation, which the in-built water quality solver then utilizes for performing MSRT modeling. The conceptual framework of EPyT-C is described in Figure 1.

<figure>
<figcaption align = "center"><b>Figure 1</b>. Conceptual framework of EPyT-C.</figcaption>
<img src="Figure 1.png" width="512"/>
</figure>

In its current form, EPyT-C comprises two in-built modules - the 'Chlorine decay and Trihalomethanes formation' module and the 'Bacterial regrowth' module. The former EPyT-C module encompasses all the required details on the physical and physicochemical interactions of the following three water quality parameters: free available chlorine (FAC), total organic carbon (TOC), and trihalomethanes. The latter contains details on the physical, physicochemical, and biochemical interactions of the five water quality parameters: FAC, recalcitrant dissolved organic carbon, biodegradable dissolved organic carbon, free-living bacteria (suspended heterotrophic bacteria), and free dead bacteria.

Based on the module selected for WDS analysis, EPyT-C evolves partial differential equations and ordinary differential equations governing the propagation and formation/ degradation of the corresponding water quality parameters within the distribution network realm. Once the governing equations (advective-reactive equations) are framed, the numerical method that involves the explicit method of characteristics and the fourth-order Runge-Kutta method, initially presented by [Tzatchkov et al. (2002)](#6), is applied to derive numerical solutions - spatiotemporal distribution of complex water quality parameters in WDS. 

EPyT-C offers the following flexibilities, making it a handy tool for research and industry:
1. Allows time-series variations in the input values for the water quality parameters at the sources (reservoirs and booster nodes).
2. Customize the random fluctuations in the input values for the water quality parameters at the sources.
3. Customize the perturbations in the reaction rate coefficient values.
4. Customize the outputs and export the data as Excel files or other formats (Figure 2).
5. Customize the numerical accuracy by altering the model parameters (time step, velocity tolerance, etc.).
6. Control the computational efficiency by adjusting the accuracy of the numerical solutions.

<figure>
<figcaption align = "center"><b>Figure 2</b>. Spatial distribution of FAC at time = 12 hrs within the benchmark test network (EPANET Network 3) corresponding to FAC concentration 0.5 mg/L at the river and lake water source outlets. The TOC concentration values at the river and lake sources outlets were maintained at 3 mg/L and 1 mg/L, respectively. The simulations were performed using the 'Chlorine decay and Trihalomethanes formation' module of EPyT-C. The squares denote reservoirs, stars indicate tanks, and circles indicate junctions. The lines specify links connecting reservoirs, tanks, and nodes.</figcaption>
<img src="Figure 2.png" width="1024"/>
</figure>

In conclusion, EPyT-C is a practical tool that can assist the scientific community and water utility managers examine WDS performance under different operating scenarios. EPyT-C scripts are under continuous development and can be further extended and improved by users and developers for specific applications. Forthcoming works involve advancing EPyT-C modeling capability to simulate dispersive transport. The example provided includes simulating the spatiotemporal distribution of FAC and THMs in a benchmark WDS considering the uncertainties in the physicochemical interactions governing the FAC degradation and THMs formation within the aquatic domain.

# Acknowledgements

This research was supported by a grant from the Ministry of Science and Technology of the State of Israel and the Federal Ministry of Education and Research (BMBF), Germany.

## References
<a id="1"></a> 
Abhijith, G. R., and Ostfeld, A. (2021). 
Modeling the Response of Nonchlorinated, Chlorinated, and Chloraminated Water Distribution Systems toward Arsenic Contamination. 
Journal of Environmental Engineering, 147(10), 04021045.

<a id="2"></a> 
Abhijith, G. R., and Ostfeld, A. (2022). 
Contaminant Fate and Transport Modeling in Distribution Systems: EPANET-C. 
Water (Switzerland), 14(10), 1665.

<a id="3"></a> 
Rossman, L, A. (2000). 
EPANET 2: Users Manual. 
Natl. Risk Manag. Res. Lab. US Environ. Prot. Agency, Cincinatti.

<a id="4"></a> 
Rossman, L. A., Woo, H., Tryby, M., Shang, F., Janke, R., Haxton, T. (2020). 
EPANET 2.2: Users Manual. 
Water Infrastructure Division, Center for Environmental Solutions and Emergency Response, U.S. Environmental Protection Agency, Cincinnati.

<a id="5"></a> 
Shang, F., Uber, J., and Rossman, L, A. (2007). 
EPANET Multi-Species Extension User's Manual. 
Cincinnati US Environ. Prot. Agency Natl. Risk Manag. Res. Lab.

<a id="6"></a> 
Tzatchkov, V. G., Aldama, A. A., Arreguin, F. I. (2002) 
Advection-Dispersion-Reaction Modeling in Water Distribution Networks. 
Journal of Water Resources Planning and Management, 128(5), 334-342.

# EPyT-C - Fully independent multi-species reactive transport modelling extension for EPyT (EPANET-Python)

# EPANET-PYTHON toolkit
EPyT is an open-source software, initially developed by the KIOS Research and Innovation Center of Excellence, University of Cyprus, operating within the Python environment for providing a PYTHON programming interface for the latest version of EPANET (Rossman et al., 2020). It calls EPANET as a shared object and employs an Object-Oriented approach for interfacing EPANET with PYTHON.

# Water quality modeling extension – EPyT-C
Though EPyT can be employed for performing water quality analysis, which comes within the scope of EPANET 2.2, it does not have any multi-species reactive-transport (MSRT) modeling capability in its current form. A fully independent water quality modeling extension, EPyT-C (in which C stands for contaminant), is developed toward this limitation. The source code of EPyT-C calls EPyT and employs the hydraulic solver of EPANET 2.2 for performing hydraulic simulation, which the in-built water quality solver then utilizes for performing MSRT modeling.
	
 The default modules of EPyT-C conceptualize scientific knowledge about the physical, physicochemical, and biochemical exchanges concerning water quality, mathematize them as partial differential equations (PDE), and numerically solve them to simulate the spatiotemporal distribution of complex water quality parameters in WDS. EPyT-C employs the numerical method initially presented by (Tzatchkov et al., 2002), which solves the advective-reactive equations by combining the explicit method of characteristics and the fourth-order Runge-Kutta method.

# Chlorine decay and Trihalomethanes formation module
The ‘Chlorine decay and Trihalomethanes formation’ module of the EPyT-C encompasses a one-dimensional mechanistic MSRT model integrating the advective transport and physicochemical exchanges of the following three water quality parameters: free available chlorine (FAC), total organic carbon (TOC), and trihalomethanes (THMs).

# Bacterial regrowth module
The ‘Bacterial regrowth’ module of the EPyT-C encompasses a one-dimensional mechanistic MSRT model integrating the advective transport and physicochemical exchanges of the following five water quality parameters: free available chlorine (FAC), recalictrant dissolved organic carbon (RDOC), biodegradable dissolved organic carbon (BDOC), free living bacteria (FLB), and free dead bacteria (FDB).

# References
Rossman, L.A., Woo, H., Tryby, M., Shang, F., Janke, R., Haxton, T., 2020. Epanet 2.2 User ’s Manual, USEPA. Cincinnati, Ohio.

Tzatchkov, V.G., Aldama, A.A., Arreguin, F.I., 2002. Advection-Dispersion-Reaction Modeling in Water Distribution Networks. J. Water Resour. Plan. Manag. 128, 334–342. https://doi.org/10.1061/(asce)0733-9496(2002)128:5(334)

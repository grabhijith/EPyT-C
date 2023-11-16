``EPyT-C``
============

An open-source Python package for modeling water quality in water distribution systems. Find the `documentation here`_.

.. _`documentation here`: https://viswaternet.readthedocs.io


*Dependencies*
------------
◉ EPyT ◉ NumPy 1.2.6 ◉ Pandas 2.1.3 ◉ XlsxWriter 3.1.9 ◉

EPyT-C has been tested on Python **3.11**.

*Flexibilities*
--------
EPyT-C offers the following flexibilities, making it a handy tool for research and industry:

1. Allows time-series variations in the input values for the water quality parameters at the sources (reservoirs and booster nodes).

2. Customize the random fluctuations in the input values for the water quality parameters at the sources.

3. Customize the perturbations in the reaction rate coefficient values.

4. Customize the outputs and export the data as Excel files or other formats.

5. Customize the numerical accuracy by altering the model parameters (time step, velocity tolerance, etc.).

6. Control the computational efficiency by adjusting the accuracy of the numerical solutions.

*Installation*
---------------
To install EPyT-C, run this command in your terminal:

.. code:: python

    pip install epyt_c
    
Alternatively, the sources for EPyT-C can be downloaded from the Github repo. You can clone the public repository:

.. code:: python

    git clone git://github.com/tylertrimble/viswaternet

Getting Started
---------------
To get started, import the VisWaterNet package:

.. code:: python

    import viswaternet as vis
    
Next, initialize a VisWaterNet model. For example purposes, we use the CTown network from `Ostfeld (2016)`_ included in the Examples folder:

.. code:: python

    model = vis.VisWNModel('Networks/CTown.inp')

.. _`Ostfeld (2016)`: https://uknowledge.uky.edu/wdst_models/2/
    
Then, call on any of the plotting functions with the argument inputs of your choice. For example, the following line of code displays the network layout of CTown with each node colored according its mean pressure (in *psi*). This is a **continuous** node plot, where the nodal colors are assigned based a gradient scale:

.. code:: python

    model.plot_continuous_nodes(parameter="pressure", value='mean', unit="psi")
    
.. figure:: logo/readme1.png
   :width: 600
   :alt: Basic network layout

We can represent the same data in a different way by generating a **discrete** node plot in which mean pressure data is grouped into 4 discrete intervals and node colors are assigned based on the corresponding value shown on a legend:

.. code:: python

    model.plot_discrete_nodes(parameter="pressure", value='mean', unit="psi",
                              legend_loc_2 = 'lower left', intervals = [0,40,80,120],
                              legend_sig_figs =0)

.. figure:: logo/readme2.png
   :width: 600
   :alt: Basic network layout

If the plot does not show up after you run the script, it is possible that your IDE does not support interactive plotting (e.g., IDLE) or interactive mode is off. To see the plot, add the following line to display the figures: 

.. code:: python

    plt.show()

Since several VisWaterNet function arguments rely on Matplotlib visualization inputs, it is recommended to visit the `Matplotlib docs`_ to view customization options for `colors`_, `colorbars`_, `node markers`_, `line styles`_, etc.

.. _`Matplotlib docs`: https://matplotlib.org/stable/index.html
.. _`colors`: https://matplotlib.org/stable/gallery/color/named_colors.html
.. _`colorbars`: https://matplotlib.org/stable/tutorials/colors/colormaps.html#sphx-glr-tutorials-colors-colormaps-py
.. _`node markers`: https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html
.. _`line styles`: https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html

More examples that demonstrate the range of VisWaterNet's plotting abilities can be found in the `Example Applications`_ section of the docs.

.. _`Example Applications`: https://viswaternet.readthedocs.io/en/latest/examples.html

*Contributing*
------------
We welcome contributions in the form of suggestions, feedback, reports of bugs, and additions to code functionality and documentation from all users! You can find instructions to raise issues, submit pull requests, and `run automated tests`_ in the `docs`_ or the `CONTRIBUTING page`_.

.. _`CONTRIBUTING page`: https://github.com/tylertrimble/viswaternet/blob/main/CONTRIBUTING.rst
.. _`docs`: https://viswaternet.readthedocs.io/en/latest/contributing.html
.. _`run automated tests`: https://viswaternet.readthedocs.io/en/latest/contributing.html#testing

*Contact*
-------
**Gopinbathan R Abhijith** - abhijith@iitk.ac.in

**Avi Ostfeld** - ostfeld@technion.ac.il

*Credits*
-------

The **Smart Water Infrastructure Laboratory**, **Indian Institute of Technology Kanpur** and **Technion Israel Institute of Technology** jointly created this package.

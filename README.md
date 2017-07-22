# Workshop: Python in Science and Research

Dive into the following topics

- Numeric Computation
- Data Visualization
    - basic plotting
- Text Analysis
- Social Network Analysis

## Up Front Preparations

As this is a notebook class, you should try to setup Python and Git on your machine before we start with the actual workshop.

### Git Installation
The course will be available in github. The most convenient way to fetch it and updates of it from there is installing a [Git Client](https://git-scm.com/downloads).

Please refer to [Basic Git](https://git-scm.com/book/en/v2) for further information, how to work with `git`.


### Python Distribution Installation
The easiest way to do so is by installing the [Anaconda Distribution](https://www.continuum.io/).
Just download and install the current distribution with Python 3.6 or higher as described [in the Anaconda Installation Instructions](https://docs.continuum.io/anaconda/install).

Then test the Anaconda installation by running your first notebook:
Therefore 
- `git clone https://github.com/plipp/informatica-pfr-2017.git` and 
- run in a terminal:
```bash
$ jupyter-notebook
```
, open in your browser [The Jupyter Notebook for the initial Installation Test](./nbs/0-a-Test%20of%20the%20Installation.ipynb) and run it ... 
If all runs through and you see as output in the last cell `All looks good!` you are done!

### Additional Python Package Installation

Further on in the workshop the following additional packages are required. 
If you don't succeed to install them upfront, don't worry: If help is needed, we will have enough time to install them together in the course.
```bash
    conda install seaborn

    conda install -c scitools cartopy=0.15.0
    # or
    conda install -c conda-forge cartopy=0.15.1
    
    conda install networkx
    pip install python-louvain

    pip install graphviz
```
On OS-Level you also will need graphviz.
Please check the [Graphviz Homepage](http://www.graphviz.org/) about how to install on your Machine.

You can check, whether the additional packages also work fine, with [The Jupyter Notebook for the Test of the additional Components](./nbs/0-b-Additional%20Component%20Installation%20Test.ipynb).

## Refresher - Python(3) Basics
If you need a refresher of your Python knowledge the [Interactive Python Tutorial](https://www.learnpython.org/) is a good starting point.

The Lectures 
- `Learn the Basics`: All and
- `Advanced Tutorials` 
    - Generators
    - List Comprehensions
    - Multiple Function Arguments
    - Sets
    - Partial functions

should be sufficient for attending the Workshop `IF PRO 02 Python für Wissenschaft und Forschung`.

# Further Reading/Resources

This Workshop is inspired by

## MOOCs

### In Python
- [edX - Python for Research](https://www.edx.org/course/using-python-research-harvardx-ph526x) (free)
- [Coursera - Applied Data Science with Python Specialization](https://www.coursera.org/specializations/data-science-python) (free audit)
- [Udacity - Intro to Data Analysis](https://www.udacity.com/course/intro-to-data-analysis--ud170) (free)

### In R
- [The Analytics Edge](https://www.edx.org/course/analytics-edge-mitx-15-071x-3)

## Primers
- [Python Data Science Primer](https://github.com/docmarionum1/python-data-science-primer) (free)

## Books

- [Packt - Practical Datascience Cookbook](https://www.packtpub.com/big-data-and-business-intelligence/practical-data-science-cookbook)

## Free Books/Juypter-Notebooks

- [Python Data Science Handbook](http://nbviewer.jupyter.org/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/Index.ipynb)
- [Materials and IPython notebooks for "Python for Data Analysis" by Wes McKinney](https://github.com/wesm/pydata-book)(jupyter-nbs free)


## Library Documentation

- [Numpy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [Matplotlib](http://matplotlib.org/)
- [NetworkX](http://networkx.readthedocs.io)

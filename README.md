# IBMLab
This is the IBM lab repo of quantum progamming course taught by professor Jens Palsberg


# Environment set up

I suggest that you should create a new lightweight virtual environment to avoid conflict of packgae dependency.
First, please ensure that you have installed virtialenv:

```console
python -m pip install --user virtualenv
python -m virtualenv --help
```

You can visit the document page of virtualenv to get more detailed explanation of how this works:
[Documentation of virtualenv](https://virtualenv.pypa.io/en/stable/installation.html)


Next, create a new virtual enviroment using virtualenv under the same directory.

```console
python -m venv ./IBMLabVenv
```

You will notice that a new folder IBMLabVenv/ appear in the same directory of this IBMlab. This folder store all information of python package and compiled library that you might need later.


You can visit the document page of venv command to get more detailed explanation of how this works:
[Documentation of venv](https://docs.python.org/3/library/venv.html)


After create the virtual enviroment, you can activate it by running the following instruction:


```console
python -m venv ./IBMLabVenv
```



I use the python version 3.12.4. Please make sure that you have installed the latest pip and install all required package by:


```console
py -m pip install -r requirements.txt 
```

Please make sure that you can execute the jupyter notebook through your web browser or inside IDE like visual studio 


# Run Jupyter note book


First, activate you jupyter notebook 



# IBM Lab1: Quantum Circuits


# IBM Lab2: Accuracy of Quantum Phase Estimation


# IBM Lab3: Scalable Shor's algorithm









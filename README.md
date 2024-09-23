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
.\IBMLabVenv\Scripts\activate
```


Install all required package by:


```console
pip install -r requirements.txt 
```



# Run Jupyter note book


First, activate you jupyter notebook 



# IBM Lab1: Quantum Circuits


In this lab, you will learn and practice how to create quantum circuit and implement basic logic gates.



# IBM Lab2: Accuracy of Quantum Phase Estimation


In this lab, you will implement quantum phase estimtation.



# IBM Lab3: Scalable Shor's algorithm


In this lab, you will learn how to implement scalable shor's algorithm.









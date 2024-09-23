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


First activate your virtual environment, then start the jupyter notebook:

```console
jupyter notebook
```


# Basic of qiskit

Here we will explore some most important interface that is related to the homework. To have a better understanding, you can copy and execute all the code snippets to jupyter notebook and play around with it by yourselves.


## Circuit construction and visualization
To initialize a quantum circuit with qiskit, import qiskit package and use QuantumCircuit function:


```python
from qiskit import QuantumCircuit
qc=QuantumCircuit(3,2) # Initialize a circuit with 3 qubits and 2 classical bits
```

To add quantum gate to the quantum circuit, you can either 
```python
qc.x(0) #Add PauliX gate to qubit 0
qc.h(1) #Add Hadamard gate to qubit 1
qc.cx(0,1) #Add a CNOT gate to qubit 0,1 controlled by qubit 0
```

Visualization is a good way to debug your circuit interactively. Qiskit has implemented a built-in method draw for visualization:
```python
qc.draw('mpl')
```

Sometimes you may want to store the figure to your local computer, to do that, pass another parameter filename to the draw method:

```python
qc.draw('mpl',filename='filename.png')
```

(Here a figure should be included)


If you are curious about the matrix of your circuit, you can get it by running the following commands:

```python
qc.draw('mpl')
```




Another way to add quantum gates is by calling method append method:

```python
from qiskit.circuit.library import XGate,HGate,CXGate
qc.append(XGate(),[0]) #Add PauliX gate to qubit 0
qc.append(HGate,[1]) #Add Hadamard gate to qubit 1
qc.append(CXGate(),[0,1]) #Add a CNOT gate to qubit 0,1 controlled by qubit 0
```


To append a small user defined quantum circuit to a larger one, you can also use the method append:

```python
from qiskit import QuantumCircuit
qc=QuantumCircuit(3,2) # Initialize a circuit with 3 qubits and 2 classical bits
qc.h(0)
qc.h(1)
qc.h(2)
qc.barrier()
subqc=QuantumCircuit(2,0,name="subqc") # Initialize your subcircuit. You can label it a new name
subqc.cx(1,0)
subqc.h(1)
subqc.y(0)
subqc.cx(0,1)
# Append the subcircuit to your original circuit. 
# You should specify where you want to insert you subcircuit on your second parameter.
# Here, the 0th qubit of subqc is mapped to the 1th qubit, the 1th qubit of subqc is mapped to the 2nd qubit
qc.append(subqc,[1,2]) 
```


If you want to debug 




## Run simulation and plot results

QuantumCircuit class that we initialized above won't calculate automatically for you. To execute your circuit, you have to run it by yourselves.



## Simulation on fake provider


Transpilation




# IBM Lab1: Quantum Circuits


In this lab, you will learn and practice how to create quantum circuit and implement basic logic gates, such as AND, OR, XOR gate. 



# IBM Lab2: Accuracy of Quantum Phase Estimation


In this lab, you will implement quantum phase estimtation.



# IBM Lab3: Scalable Shor's algorithm


In this lab, you will learn how to implement scalable shor's algorithm.








# Reference


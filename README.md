# QuantumLab

This is the lab repository for the **Quantum Programming course (CS238)** taught by Professor Jens Palsberg in the Fall 2024 quarter.  
In this lab, you will gain hands-on experience with **quantum programming using Qiskit**.  

You will:

* Learn how to create and compile quantum circuits with Qiskit.  
* Learn how to run and debug circuits using simulation.  
* Become familiar with quantum gates, the Quantum Fourier Transform (QFT), Quantum Phase Estimation (QPE), and Shor’s Algorithm.  
* Learn how to simulate your algorithms on noisy backends and fake quantum computers provided by Qiskit.  

---


# Environment set up

The installation process has been tested with **Python 3.11**.  
If you encounter issues, please downgrade to Python 3.11:  

👉 [Download Python 3.11](https://www.python.org/downloads/release/python-3110/)

It is recommended to use a **lightweight virtual environment** to avoid dependency conflicts.  

First, install `virtualenv`:

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




Or by calling method append method:

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

Visualization is a good way to debug your circuit interactively. Qiskit has implemented a built-in method draw for visualization:
```python
qc.draw('mpl')
```

Sometimes you may want to store the figure to your local computer, to do that, pass another parameter filename to the draw method:

```python
qc.draw('mpl',filename='filename.png')
```

![alt text](Figure/qcexample.png)


If you are curious about the matrix of your circuit, you can get it by running the following commands:

```python
from qiskit.quantum_info import Operator
U = Operator(qc)
print(U.data)
```





![alt text](Figure/subqc.png)


## Run simulation and plot results

QuantumCircuit class that we initialized above won't calculate automatically for you. To execute your circuit, you have to run it by yourselves.
A quantum citcuit in qiskit has both quantum registers and classical registers, the measurement result is stored in classical register.


To run simulation, don't foget to add measurement:

```python
from qiskit import QuantumCircuit
qc=QuantumCircuit(3,3) # Initialize a circuit with 3 qubits and 2 classical bits
qc.x(0) #Add PauliX gate to qubit 0
qc.h(1) #Add Hadamard gate to qubit 1
qc.cx(0,1) #Add a CNOT gate to qubit 0,1 controlled by qubit 0
qc.cx(2,1) #Add a CNOT gate to qubit 2,1 controlled by qubit 2
qc.barrier()
qc.measure([0,1,2],[0,1,2]) # Add measurement on the computational basis.
qc.draw("mpl")
```

![alt text](Figure/measurement.png)


To run the ideal simulation and get the result, we need to include a backend AerSimulator


you can run the following codes:
```python
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
backend = AerSimulator()
job = backend.run(qc, shots=1000) # Run the circuit 1000 times 
output = job.result().get_counts() 
plot_histogram(output) #Plot the result
```

![alt text](Figure/histogram.png)



## Simulation with customized noise model

You are asked to run your circuit simulation with some noise level.


you can run the following codes:
```python
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from noisemodel import construct_bitphaseflip_noise_model
backend = AerSimulator()
noise_model=construct_bitphaseflip_noise_model(0.1,0.1,0.1)
job = backend.run(qc, shots=1000,noise_model=noise_model) # Run the circuit 1000 times 
output = job.result().get_counts() 
plot_histogram(output) #Plot the result
```

![alt text](Figure/noisemodelexample.png)


## Simulation on fake provider

In this lab, you are required to run your simulation on IBM fake provider, which simulate the real noisy environment on a superconducting quantum computer. 


```python
from qiskit import QuantumCircuit, transpile
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.visualization import plot_histogram
 
# Generate a 20-qubit simulated backend
backend = GenericBackendV2(num_qubits=20)
 

qc=QuantumCircuit(3,3) # Initialize a circuit with 3 qubits and 2 classical bits
qc.x(0) #Add PauliX gate to qubit 0
qc.h(1) #Add Hadamard gate to qubit 1
qc.cx(0,1) #Add a CNOT gate to qubit 0,1 controlled by qubit 0
qc.cx(2,1) #Add a CNOT gate to qubit 2,1 controlled by qubit 2
qc.barrier()
qc.measure([0,1,2],[0,1,2]) # Add measurement on the computational basis.
 
# Transpile the ideal circuit to a circuit that can be directly executed by the backend
transpiled_circuit = transpile(qc, backend)
transpiled_circuit.draw('mpl')
 
# Run the transpiled circuit using the simulated backend
job = backend.run(transpiled_circuit,shots=1000)
counts = job.result().get_counts()
plot_histogram(counts)
```

The transpiled circuit is shown as:

![alt text](Figure/transpiled_circuit.png)


You can also draw the layout and visulize the mapping of the virtual qubit to the real qubit by:

```python
from qiskit.visualization import plot_circuit_layout
fig=plot_circuit_layout(transpiled_circuit,backend)   

# Save the figure to a file, e.g., as 'layout.png'
fig.savefig('Figure/layout.png')
```

![alt text](Figure/layout.png)


The result of the above simulation is:

![alt text](Figure/histogramnoise.png)




# IBM Lab1: Quantum Circuits


In this lab, you will learn how to create quantum circuits and implement basic logic gates such as AND, OR, and XOR.  
Grading will be based in part on the correctness of your logic gate implementations.

To run the autotests for functions `NOT`, `AND`, `NAND`, `OR`, and `ANDOR`, copy your implementation into `test/testlogic.py` and execute:


```console
cd test
python testlogic.py
```






# IBM Lab2: Accuracy of Quantum Phase Estimation

In this lab, you will implement **Quantum Phase Estimation (QPE)**.

To run the autotests for your implementations of qc4 and qc4improved, copy your code into test/testPhaseEstimation.py and execute:
```console
cd test
python testPhaseEstimation.py
```


# IBM Lab3: Scalable Shor's algorithm


In this lab, you will implement a scalable version of Shor’s Algorithm.
Specifically, you will build circuits for factoring 15, 21, and 63.

We provide the implementation for factoring 15.
You are required to implement the versions for 21 and 63.

To run the autotests for Shor21 and Shor63, copy your implementations into test/testShor.py and execute:

```console
cd test
python testShor.py
```





# Reference


Here are some relevant references for the lab.


* [Qiskit Documentation](https://qiskit.org/documentation/)  
* Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information*, Cambridge University Press, 2010.  
* [Qiskit Textbook: Learn Quantum Computation Using Qiskit](https://qiskit.org/textbook/)  
* John Preskill, *Lecture Notes for Physics 219: Quantum Computation* (Caltech), available online.  
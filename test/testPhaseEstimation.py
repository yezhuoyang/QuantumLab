from qiskit import *
from qiskit_aer import AerSimulator
import numpy as np
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import math
from qiskit.circuit.library import QFT
from termcolor import colored


def qft(n):
    """Creates an n-qubit QFT circuit"""
    circuit = QuantumCircuit(n)
    def swap_registers(circuit, n):
        for qubit in range(n//2):
            circuit.swap(qubit, n-qubit-1)
        return circuit
    def qft_rotations(circuit, n):
        """Performs qft on the first n qubits in circuit (without swaps)"""
        if n == 0:
            return circuit
        n -= 1
        circuit.h(n)
        for qubit in range(n):
            circuit.cp(np.pi/2**(n-qubit), qubit, n)
        qft_rotations(circuit, n)
    
    qft_rotations(circuit, n)
    swap_registers(circuit, n)
    return circuit




def qc4():
    ## Start your code to create the circuit
    circuit=QuantumCircuit(5, 4)


    ##Your circuit construction goes here:




    ##Your circuit construction ends here


    # We'll run the program on a simulator
    backend = AerSimulator()

    # Transpile the ideal circuit to a circuit that can be directly executed by the backend
    transpiled_circuit = transpile(circuit, backend)

    # Since the output will be deterministic, we can use just a single shot to get it
    job = backend.run(transpiled_circuit, shots=1000, memory=True)
    output = job.result().get_counts()

    return circuit, output


def qc4improved():
    pass




def testqc4():
    circuit,output=qc4()
    result=max(output, key=output.get)
    if(result=='0101'):
        print(colored('Congrats, qc4 Test passed ','green')+"\U0001f600")
    else:
        print(colored('OOPS, qc4 Test failed! Your result '+result+" is not correct!",'red')+"\U0001F923")    



def testqc4improved():
    pass







if __name__ == '__main__':
    print("-----------Strating the tests of IBM Lab2: Quantum phase estimation-----------")

    testqc4()
    print("--------------------------Your score is:--------------------------")    


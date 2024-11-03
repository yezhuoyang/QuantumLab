from qiskit import *
from qiskit_aer import AerSimulator
import numpy as np
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt




def _cU_multi(U,m,k):
    circ = QuantumCircuit(m)
    for _ in range(2**k):
        circ.append(U, range(m))
    
    U_multi = circ.to_gate()
    U_multi.name = '7Mod15_[2^{}]'.format(k)
    
    cU_multi = U_multi.control()
    return cU_multi


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


def Shor15():
    ## Code for constructing shor_QPE for factoring 15 starts here
    N = 15
    m = int(np.ceil(np.log2(N)))
    
    U_qc = QuantumCircuit(m)
    U_qc.x(range(m))
    U_qc.swap(1, 2)
    U_qc.swap(2, 3)
    U_qc.swap(0, 3)
    
    U = U_qc.to_gate()
    U.name ='{}Mod{}'.format(7, N)

    # QPE circuit for Shor15
    t = 3 
    shor_QPE = QuantumCircuit(t+m, t)
    shor_QPE.h(range(t))
    
    shor_QPE.x(t)
    for idx in range(t-1):
        shor_QPE.append(_cU_multi(U,m,idx), [idx]+ list(range(t,t+m)))
    
    qft_dag = qft(t).inverse()
    qft_dag.name = 'QFT+'
    
    shor_QPE.append(qft_dag, range(t))
    shor_QPE.measure(range(t), range(t))
    ## Code for constructing shor_QPE for factoring 15 ends here    

    
    backend = AerSimulator()
    transpiled_circuit = transpile(shor_QPE, backend)
    job = backend.run(transpiled_circuit, shots=1000, memory=True)
    count_QPE= job.result().get_counts()
    return shor_QPE, count_QPE


def Shor21():
    ##Your circuit for creating quantum circuit shor_QPT of factoring 21 starts here
    shor_QPE=None




    
    ##Your circuit for creating quantum circuit shor_QPT of factoring 21 ends here    
    backend = AerSimulator()
    transpiled_circuit = transpile(shor_QPE, backend)
    job = backend.run(transpiled_circuit, shots=1000, memory=True)
    count_QPE= job.result().get_counts()
    return shor_QPE, count_QPE



def Shor63():
    ##Your circuit for creating quantum circuit shor_QPT of factoring 63 starts here
    shor_QPE=None





    
    ##Your circuit for creating quantum circuit shor_QPT of factoring 63 ends here    
    backend = AerSimulator()
    transpiled_circuit = transpile(shor_QPE, backend)
    job = backend.run(transpiled_circuit, shots=1000, memory=True)
    count_QPE= job.result().get_counts()
    return shor_QPE, count_QPE


def testMod21():
    pass


def testMod63():
    pass





if __name__ == '__main__':
    print("-----------Strating the tests of IBM Lab3: Scalable Shor's algorithm-----------")


    print("--------------------------Your score is:--------------------------")    
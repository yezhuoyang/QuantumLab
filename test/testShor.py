from qiskit import *
from qiskit_aer import AerSimulator
import numpy as np
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import math
from termcolor import colored


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
    a = 7
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
    return a, shor_QPE, count_QPE


def Shor21():
    ##Your circuit for creating quantum circuit shor_QPT of factoring 21 starts here
    a=0
    shor_QPE=None



    
    ##Your circuit for creating quantum circuit shor_QPT of factoring 21 ends here    
    backend = AerSimulator()
    transpiled_circuit = transpile(shor_QPE, backend)
    job = backend.run(transpiled_circuit, shots=1000, memory=True)
    count_QPE= job.result().get_counts()
    return a, shor_QPE, count_QPE



def Shor63():
    ##Your circuit for creating quantum circuit shor_QPT of factoring 63 starts here
    a=0
    shor_QPE=None




    
    ##Your circuit for creating quantum circuit shor_QPT of factoring 63 ends here    
    backend = AerSimulator()
    transpiled_circuit = transpile(shor_QPE, backend)
    job = backend.run(transpiled_circuit, shots=1000, memory=True)
    count_QPE= job.result().get_counts()
    return a,shor_QPE, count_QPE



def orderfinding(a,N):
    r=2
    tmp=(a**2)%N
    while(tmp!=1):
        r+=1
        tmp=(tmp*a)%N
    return r



# find the closest N/M to a value, such that N<Nmax, M<Mmax 
def find_closest_fraction(value,Nmax,Mmax):
    currentBest=(-1,-1)
    currentdiff=10000000000
    for N in range(1,Nmax):
        for M in range(N+1,Mmax):
            diff=abs(value-N/M)
            if diff<currentdiff:
                currentBest=(N,M)
                currentdiff=diff
    return currentBest[0],currentBest[1]



def binary_string_to_float(bstr,nq):
    value=int(bstr, base=2)/(2**(nq))
    return value



def testMod15():
    a, shor_QPE,count_QPE=Shor15()
    '''
    For each large count, try to use that as and order and factor 15
    '''
    if(math.gcd(a,15)!=1):
        print(colored('OOPS, Shor15 Test failed! '+str(a)+' you use has no order modular 15','red')+"\U0001F923")  
        return
    r=orderfinding(a,15)
    if((r%2)==1):
        print(colored('OOPS, Shor15 Test failed! '+str(a)+' you use has odd order modular 15','red')+"\U0001F923")  
        return          
    
    factor=math.gcd(a**(r//2)-1,15)
    if(factor==1): 
        print(colored('OOPS, Shor15 Test failed! '+str(a)+' you use won\'t give you non-trivial divisor of 15','red')+"\U0001F923")  
        return               


    # Sort dictionary by value in descending order and keep top r keys
    nq=len(list(count_QPE.keys())[0])

    top_prob_measurement = list((dict(sorted(count_QPE.items(), key=lambda item: item[1], reverse=True)[:r])).keys())
    top_prob_value=[binary_string_to_float(x,nq) for x in top_prob_measurement]
    
    top_prob_value=[x for x in top_prob_value if x !=0]


    closestNMpair=[find_closest_fraction(value,15,15) for value in top_prob_value]
    Mlist=[x[1] for x in closestNMpair]
    rtest=math.lcm(*Mlist)
    if(rtest!=r):
        print(colored('OOPS, Shor15 Test failed! The order you find is not correct for '+str(a),'red')+"\U0001F923")  
        return        
    
    print(colored('Congrats, Shor15 Test passed!','green')+"\U0001f600")    



def testMod21():
    a, shor_QPE,count_QPE=Shor21()
    '''
    For each large count, try to use that as and order and factor 21
    '''
    if(math.gcd(a,21)!=1):
        print(colored('OOPS, Shor21 Test failed! '+str(a)+' you use has no order modular 21','red')+"\U0001F923")  
        return
    r=orderfinding(a,21)
    if((r%2)==1):
        print(colored('OOPS, Shor21 Test failed! '+str(a)+' you use has odd order modular 21','red')+"\U0001F923")  
        return          
    
    factor=math.gcd(a**(r//2)-1,21)
    if(factor==1): 
        print(colored('OOPS, Shor21 Test failed! '+str(a)+' you use won\'t give you non-trivial divisor of 21','red')+"\U0001F923")  
        return               


    # Sort dictionary by value in descending order and keep top r keys
    nq=len(list(count_QPE.keys())[0])

    top_prob_measurement = list((dict(sorted(count_QPE.items(), key=lambda item: item[1], reverse=True)[:r])).keys())
    top_prob_value=[binary_string_to_float(x,nq) for x in top_prob_measurement]
    
    top_prob_value=[x for x in top_prob_value if x !=0]


    closestNMpair=[find_closest_fraction(value,21,21) for value in top_prob_value]
    Mlist=[x[1] for x in closestNMpair]
    rtest=math.lcm(*Mlist)
    if(rtest!=r):
        print(colored('OOPS, Shor21 Test failed! The order you find is not correct for '+str(a),'red')+"\U0001F923")  
        return        
    
    print(colored('Congrats, Shor21 Test passed!','green')+"\U0001f600")




def testMod63():
    a, shor_QPE,count_QPE=Shor63()
    '''
    For each large count, try to use that as and order and factor 63
    '''
    if(math.gcd(a,63)!=1):
        print(colored('OOPS, Shor63 Test failed! '+str(a)+' you use has no order modular 63','red')+"\U0001F923")  
        return
    r=orderfinding(a,63)
    if((r%2)==1):
        print(colored('OOPS, Shor63 Test failed! '+str(a)+' you use has odd order modular 63','red')+"\U0001F923")  
        return          
    
    factor=math.gcd(a**(r//2)-1,63)
    if(factor==1): 
        print(colored('OOPS, Shor63 Test failed! '+str(a)+' you use won\'t give you non-trivial divisor of 63','red')+"\U0001F923")  
        return               


    # Sort dictionary by value in descending order and keep top r keys
    nq=len(list(count_QPE.keys())[0])

    top_prob_measurement = list((dict(sorted(count_QPE.items(), key=lambda item: item[1], reverse=True)[:r])).keys())
    top_prob_value=[binary_string_to_float(x,nq) for x in top_prob_measurement]
    
    top_prob_value=[x for x in top_prob_value if x !=0]


    closestNMpair=[find_closest_fraction(value,63,63) for value in top_prob_value]
    Mlist=[x[1] for x in closestNMpair]
    rtest=math.lcm(*Mlist)
    if(rtest!=r):
        print(colored('OOPS, Shor63 Test failed! The order you find is not correct for '+str(a),'red')+"\U0001F923")  
        return        
    
    print(colored('Congrats, Shor63 Test passed!','green')+"\U0001f600")





if __name__ == '__main__':
    print("-----------Starting the tests of IBM Lab3: Scalable Shor's algorithm-----------")
    #testMod15()
    testMod21()
    testMod63()
    print("--------------------------Your score is:--------------------------")    
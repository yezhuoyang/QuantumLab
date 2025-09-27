
# IBM Lab1: Quantum Circuits


In this lab, you will learn how to create quantum circuits and implement basic logic gates such as AND, OR, and XOR.  
Grading will be based in part on the correctness of your logic gate implementations.

To run the autotests for functions `NOT`, `AND`, `NAND`, `OR`, and `ANDOR`, copy your implementation into `test/testlogic.py` and execute:


```console
cd test
python testlogic.py
```

### Grading Policy for Lab1

Your grade for **Lab1: Quantum Circuits** will be determined based on both the correctness of your implementations and your ability to demonstrate them on a fake quantum backend. Points are distributed as follows:

1. **XOR gate implementation** — 10 points  
2. **AND gate implementation** — 10 points  
3. **NAND gate implementation** — 10 points  
4. **OR gate implementation** — 10 points  
5. **Running AND gate on a fake quantum computer** — 10 points  
6. **Transpiling the AND gate correctly** — 10 points  
7. **Choosing and justifying the best 3-qubit initial layout** — 10 points  
8. **ANDOR gate implementation** — 30 points  

**Total: 100 points**

You are encouraged to use the provided autotests to validate your solutions before submission. Correctness will be assessed based on whether your implementations produce the expected outputs across a range of test cases.




# IBM Lab2: Accuracy of Quantum Phase Estimation

In this lab, you will implement **Quantum Phase Estimation (QPE)**.

To run the autotests for your implementations of qc4 and qc4improved, copy your code into test/testPhaseEstimation.py and execute:
```console
cd test
python testPhaseEstimation.py
```






### Grading Policy for Lab2

Your grade for **Lab3: Accuracy of Quantum Phase Estimation** will be determined based on both the correctness of your implementations and your ability to analyze simulation results. Points are distributed as follows:

1. **Correct implementation of qc4** — 10 points  
3. **Compute the probability of success** — 10 points  
2. **Correct implementation of qc4improved** — 10 points  

**Total: 100 points**

You are encouraged to use the provided autotests to validate your solutions before submission. In addition to correctness, partial credit will be awarded for clear explanations of your simulation results and design choices.




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


### Grading Policy for Lab3

Your grade for **Lab3: Scalable Shor’s Algorithm** will be determined based on both the correctness of your implementations and your ability to analyze simulation results. Points are distributed as follows:

1. **Build test circuit for 7X mod 15** — 10 points  
2. **Verify that U^(2^2) = I** — 10 points  
3. **Execute the reduced circuit for 7X mod 15** — 10 points  
4. **Perform noisy simulation of `shor_Orig` and `shor_QPE` for N=15, and explain the results** — 10 points  
5. **Redo the lab for N=21** — 30 points  
6. **Redo the lab for N=63** — 30 points  

**Total: 100 points**

You are encouraged to use the provided autotests to validate your solutions before submission. In addition to correctness, partial credit will be awarded for clear explanations of your simulation results and design choices.
#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import *
get_ipython().run_line_magic('matplotlib', 'inline')
circuit = QuantumCircuit(3,3)
circuit.draw(output='mpl')


# In[2]:


circuit.draw()


# In[3]:


circuit.x(0)
circuit.barrier()
circuit.draw(output='mpl')


# In[4]:


circuit.h(1)
circuit.cx(1,2)
circuit.cx(0,1)
circuit.h(0)
circuit.draw(output='mpl')


# In[5]:


circuit.barrier()
circuit.measure([0,1], [0,1])
circuit.draw()


# In[6]:


circuit.barrier()
circuit.cx(1,2)
circuit.cz(0,2)
circuit.draw()


# In[7]:


circuit.measure(2,2)
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots = 1024).result()
counts = result.get_counts()
from qiskit.tools.visualization import plot_histogram
plot_histogram(counts)


# In[8]:


print(counts)


# In[ ]:





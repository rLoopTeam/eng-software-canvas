# eng-software-canvas
CAN simulation framework for rLoop avionics developement
For help getting started talk to @vookungdoofu in #eng-software


CANVAS (CAN Virtual Approximation Simulator) is meant to simulate the behaviour of the hardware nodes and CAN bus in the flight 
version of rPod. This is still an early "beta" version of the framework. Currently it simulates the adressing scheme of CAN nodes, but not the bus arbitration or message priority mechanics. This will change in later versions.


Hardware nodes can only be written in Python for now, but support for other languages can be added if needed.


CANVAS consists of two main components: the Supervisor process management framework, and python bindings for a CAN-like interprocess communication library developed by @vookungdoofu. Each node must include this library to be able to talk with the rest of the system over the simulated CAN bus. See "node1.py" and "node2.py" in /nodes for code examples (with handy comments in node2). The comm library uses the excellent ZeroMQ messaging lib as its low-level communication mechanism (used by both CERN and NASA backends). The canvas comm library is found in "canvas.py" in /nodes and must be included in all nodes that wants to talk on the bus. 

Supervisor is used to manage the start and manage the node processes, and also takes care of logging their output. The supervisord.conf file points Supervisor to the .py files you want to run as nodes, tells it how to start/manage them, and how the output should be logged. The docs for supervisor are well-maintained and can be found at: www.supervisord.org


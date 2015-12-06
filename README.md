# eng-software-canvas
CAN simulation framework for rLoop avionics developement
For help getting started talk to @vookungdoofu in #eng-software


CANVAS (CAN Virtual Approximation Simulator) is meant to simulate the behaviour of the hardware nodes and CAN bus in the flight 
version of rPod. This is still an early "beta" version of the framework. Currently it simulates the adressing scheme of CAN nodes, but not the bus arbitration or message priority mechanics. This will change in later versions.


Hardware nodes can only be written in Python for now, but support for other languages can be added if needed.


CANVAS consists of two main components: the Supervisor process management framework, and python bindings for a CAN-like interprocess communication library developed by @vookungdoofu. Each node must include this library to be able to talk with the rest of the system of the simulated CAN bus. 

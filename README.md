# eng-software-canvas
CAN simulation framework for rLoop avionics developement.
For help getting started talk to @vookungdoofu in #eng-software.


CANVAS (CAN Virtual Approximation Simulator) is meant to simulate the behaviour of the hardware nodes and CAN bus in the flight version of rPod. This is still an early "beta" version of the framework. Currently it simulates the adressing scheme of CAN nodes, but not the bus arbitration or message priority mechanics. This will change in later versions.


Hardware nodes can only be written in Python for now, but support for other languages can be added if needed.


CANVAS consists of two main components: the Supervisor process management framework, and python bindings for a CAN-like interprocess communication library developed by @vookungdoofu. Each node must include this library to be able to talk with the rest of the system over the simulated CAN bus. The comm library uses the excellent ZeroMQ messaging lib as its low-level communication mechanism (used by both CERN and NASA backends). The canvas comm library is found in "canvas.py" in /nodes and must be included in all nodes that wants to talk on the bus. 

Supervisor is used to start and manage the node processes, and also takes care of logging their output. When you start the system, Supervisor first looks for a file called 'supervisord.conf'. This is where you tell Supervisor what .py files you want to run as nodes, tells it how to start/manage them, and how the output should be logged. An example config file for starting node1, node2 and the canvas server in included in the repo. For more details on config file options check out: www.supervisord.org/configuration.html


## Installing the Supervisor and ZMQ environment:

1. install easy_install:
wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python

2. install supervisor:
sudo easy_install supervisor

3. install python dev libraries (you might have this already, needed to build ZMQ):
sudo apt-get install python-dev

4. install linux build tools (most likely you have this already):
sudo apt-get install build-essential

5. install pyzmq, python's ZMQ module:
sudo easy_install pyzmq

The last step might throw a bunch of warnings, errors and something that looks like a self-destruct sequence at you. Do not be alarmed, this is normal.
If all is well you should see something like this when it's done:

Adding pyzmq 15.1.0 to easy-install.pth file
Installed /usr/local/lib/python2.7/dist-packages/pyzmq-15.1.0-py2.7-linux-x86_64.egg
Processing dependencies for pyzmq
Finished processing dependencies for pyzmq

## Installing and running CANVAS in Supervisor:

Make a directory called "canvas" somewhere on your system, then pull this repo into it. I like to keep my supervisor folders in my home dir, for example /home/joakim/canvas, but anywhere is fine. In your canvas folder, create two new directories called "node_logs" and "supervisor_logs". Now open a terminal in your canvas folder (or cd to it) and run "supervisord -n". If all is well you should see the canvas server and 2 nodes come online and start talking to eachother.

Supervisor always looks for the supervisord.conf file in the directory where you run the "supervisord -n" command. So it's important to run the command in the correct directory. 

## Supervisor and logging

Supervisor will log output on stdout and stderr from the nodes. They way it does this is changed in supervisord.conf. Each node has a separate 'stdout_logfile' and 'stderr_logfile' parameter, meaning each node gets it's own logs for both stdout and stderr. There is also a separate logfile for Supervisor itself. For more details about logging see http://supervisord.org/configuration.html#program-x-section-settings

By default Supervisor captures the output on stdout and stderr from its managed processes and outputs it in the terminal. With many nodes running this can get messy, so you can turn the output from the nodes off in supervisord.conf by changing the "loglevel" parameter in the "supervisord" section. DEBUG shows output from all processes, INFO shows only supervisor info like nodes starting/stopping etc. If INFO is set the output from a node is still logged in it's logfiles.

But wait, there's more! Supervisor also comes with a handy web-based gui to contorl your system. Open a web browser and go to 127.0.0.1:9001. From here you can bring nodes up/down and see the output from a single node with it's 'tail -f' option.

## Code examples

To get started, check out "node1.py" and "node2.py" in /nodes. Node2 comes with handy comments on how to use the messaging library. "canvas.py" contains the actual library code if you want to check out the ZMQ magic!

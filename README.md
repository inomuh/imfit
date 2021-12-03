# IM-FIT

IM-FIT provides to find the weaknesses on Python and ROS. 
The user can use IM-FIT with workload and/or code snippets. At the same time the user can create custom workload and code snippets for its codes.
The codes scan by IM-FIT to detect the lines. The user can select the lines to use for execution. At the execution modul, the user can select what it wants features to run.
The user can show informations about the its tested codes. If the user wants to watch the created scenarios by IM-FIT, it can do it on Gazebo.


Installations
-------------------------------
- Firstly, you must install python3 and some requirements:

        sudo apt-get update && sudo apt-get install python3 python3-venv python3-pip

- Install PySide6:

        pip install PySide6

- Install PyQt6:

        pip install PyQt6==6.1.0

Usage
-------------------------------
Terminal command to open interface

    python3 main.py

PS: Before first run IM-FIT, the command 

    chmod +x * 

must enter the terminal opened from IM-FIT folder.

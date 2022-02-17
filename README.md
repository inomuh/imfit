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

### Credits

<a href="http://valu3s.eu">
  <img align=left img src="https://valu3s.eu/wp-content/uploads/2020/04/VALU3S_green_transparent-1024x576.png" 
       alt="valu3s_logo" height="100" >
</a>

This work is done by [Inovasyon Muhendislik](https://www.inovasyonmuhendislik.com/) and [ESOGU-SRLAB](https://srlab.ogu.edu.tr/) under [VALU3S](https://valu3s.eu) project. This project has received funding from the [ECSEL](https://www.ecsel.eu) Joint Undertaking (JU) under grant agreement No 876852. The JU receives support from the European Union’s Horizon 2020 research and innovation programme and Austria, Czech Republic, Germany, Ireland, Italy, Portugal, Spain, Sweden, Turkey.

### License

See the [LICENSE](LICENSE.md) file for license rights and limitations (Apache-2.0 Licence).

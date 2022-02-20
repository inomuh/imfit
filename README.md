# IM-FIT
![last_commit](https://img.shields.io/github/last-commit/inomuh/imfit?color=green) ![repo_size](https://img.shields.io/github/repo-size/inomuh/imfit) ![Apache-2.0 License](https://img.shields.io/github/license/inomuh/imfit?color=blue) ![lang](https://img.shields.io/github/languages/top/inomuh/imfit) [![CodeFactor](https://www.codefactor.io/repository/github/akerdogmus/imfit/badge)](https://www.codefactor.io/repository/github/akerdogmus/imfit)

IM-FIT provides to find the weaknesses on Python and ROS. 
The user can use IM-FIT with workload and/or code snippets. At the same time the user can create custom workload and code snippets for its codes.
The codes scan by IM-FIT to detect the lines. The user can select the lines to use for execution. At the execution modul, the user can select what it wants features to run.
The user can show informations about the its tested codes. If the user wants to watch the created scenarios by IM-FIT, it can do it on Gazebo.

Details of IM-FIT
-------------------------------
IM-FIT is a software tool for industrial robot software that can customize. By using IM-FIT, you can scan the mutation-applicable lines in source codes for **Python, ROS-Py, Launch, Yaml, SRV, MSG** file types, create fault plans, execute according to fault plans, and get a V&V report containing the information obtained in the process.

![Image of IM-FIT Home Page](https://github.com/inomuh/imfit/blob/main/home-page.png)
<p align="center">
        <b><i>Fig 1. IM-FIT Home Page</i></b>
</p>

With IM-FIT, the user can inject fault loads that the user has created, either selected from the fault library or already created, into the workload. By running IM-FIT fault-injected codes in a virtual operating system environment with Docker software, it is possible to collect the data of the fault results, while the injected faults are prevented from affecting each other and the system with this method. In the display of the collected data, classical analyzes and log analyzes are provided. By using graphics and Gazebo simulation environment in the visualization part, it is provided to show which events may occur as a result of fault injections. These analyzes are made into a “json” type report and presented to the user as a V&V report, thus completing the process verification.

![Image of IM-FIT Start Page](https://github.com/inomuh/imfit/blob/main/start-page.png)

<p align="center">
        <b><i>Fig 2. IM-FIT Start Page</i></b>
</p>

IM-FIT checks if the user has source codes loaded into IM-FIT, the workload usage status, and whether it has selected code snippets. If the user is going to use the workload, it loads the workload or creates them within the IM-FIT interface. The user selects which code snippets to use in the scanning process from the table of code snippets. If the user wants to create its own code snippets, it does so within the IM-FIT interface.


![Image of IM-FIT Scan Page](https://github.com/cembglm/create_readmeS/blob/main/scan-page.png)
<p align="center">
        <b><i>Fig 3. IM-FIT Scan Page</i></b>
</p>

On the start page, when all the operations for the scanning step are completed, the scan page is entered.


![Image of IM-FIT ROS Page](https://github.com/inomuh/imfit/blob/main/ros-page.png)
<p align="center">
        <b><i>Fig 4. IM-FIT ROS Page</i></b>
</p>

IM-FIT collects this data by running the file that the user wants to mutate to display nodes, topics, services, parameters and messages on the ROS page. IM-FIT performs mutation operations on ROS-Py and Launch files according to the collected data and user requests.
On the execution page, IM-FIT runs the mutants on Docker. At the end of the execution process, you can go to the monitoring page to take detailed information about the V&V process.

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
  <img align=left img src="https://upload.wikimedia.org/wikipedia/tr/d/d0/TUBITAK-Logo.jpg" 
       alt="tübitak_logo" height="100" >
</a>

---

This work is supported by [TÜBİTAK](https://www.tubitak.gov.tr/) Project under grant number 120N803 which conducted by the İnovasyon Mühendislik.

---

<a href="http://valu3s.eu">
  <img align=right img src="https://valu3s.eu/wp-content/uploads/2020/04/VALU3S_green_transparent-1024x576.png" 
       alt="valu3s_logo" height="100" >
</a>

  This work is also done by [Inovasyon Muhendislik](https://www.inovasyonmuhendislik.com/) and [ESOGU-SRLAB](https://srlab.ogu.edu.tr/) under [VALU3S](https://valu3s.eu) project. This project has received funding from the [ECSEL](https://www.ecsel.eu) Joint Undertaking (JU) under grant agreement No 876852. The JU receives support from the European Union’s Horizon 2020 research and innovation programme and Austria, Czech Republic, Germany, Ireland, Italy, Portugal, Spain, Sweden, Turkey.

### License

See the [LICENSE](LICENSE.md) file for license rights and limitations (Apache-2.0 Licence).

# IM-FIT
![repo_size](https://img.shields.io/github/repo-size/inomuh/imfit) ![Apache-2.0 License](https://img.shields.io/github/license/inomuh/imfit?color=blue) ![lang](https://img.shields.io/github/languages/top/inomuh/imfit) [![CodeFactor](https://www.codefactor.io/repository/github/akerdogmus/imfit/badge)](https://www.codefactor.io/repository/github/akerdogmus/imfit)

IM-FIT applies mutation testing to **Python, ROS-Py, Launch, Yaml, SRV, MSG** file types.

![Image of IM-FIT Home Page](https://github.com/inomuh/imfit/blob/main/home-page.png)
<p align="center">
        <b><i>Fig 1. IM-FIT Home Page</i></b>
</p>

IM-FIT, which presents a user manual to the user when opened, aims to provide an efficient and detailed use to the user with this manual.

![Image of IM-FIT Start Page](https://github.com/inomuh/imfit/blob/main/start-page.png)

<p align="center">
        <b><i>Fig 2. IM-FIT Start Page</i></b>
</p>

IM-FIT scans are fully customizable for workloads and selected code snippets. After the scanning process is applied, fault plans are created to be used in test processes. Fault plans keep information about which file to apply a code mutation.

![Image of IM-FIT Scan Page](https://github.com/inomuh/imfit/blob/main/scan-page.png)
<p align="center">
        <b><i>Fig 3. IM-FIT Scan Page</i></b>
</p>

Mutants that are compared to the original code in the run are classified as killed or survived. Killing a mutant is the main objective of our testing process. Surviving mutants show that the software we tested works with the fault.

![Image of IM-FIT ROS Page](https://github.com/inomuh/imfit/blob/main/ros-page.png)
<p align="center">
        <b><i>Fig 4. IM-FIT ROS Page</i></b>
</p>

IM-FIT performs mutation operations on ROS-Py and Launch files according to the collected data and user requests.
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

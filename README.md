<h1 align="center">
   <p> COMPort 🐍</p>  
</h1>

<br>

<h1 align="center">
  <img 
    src="./Doc/demo.gif"
  />
</h1>

---
## 🧾 About
**COMPort** is a Python project to capture a data stream from an Arduino device connected to a specific COM port. Also, it exports a binary file (.bin), a hexadecimal file (.hex), and an Excel file (.xlsx) at the end of the streaming session.

---
## 🕖 Versioning
- COMPort v2.0 (relased in 09/01/2022)
- COMPort v1.5 (relased in 11/10/2021)
- COMPort v1.0 (relased in 24/09/2021)

---
## ✅ Main features
- [x] Read data stream from COM port.
- [x] Sets buffer size.
- [x] Visualize data stream. 
- [x] Generate binary, hexadecimal and xlsx file.   

---
## 🔧 Technology
- [Python](https://www.python.org/) 💚

---
## 👨‍💻 How to Setup
Download and install: 
 - [Python 3.7.7](https://www.python.org/downloads/release/python-377/)
 - [Visual Studio Code 1.67.2](https://code.visualstudio.com/Download)
 - [Null-modem emulator](https://sourceforge.net/projects/com0com/)
 - [COM Port Data Emulator](https://www.aggsoft.com/com-port-emulator/download.htm)
 - [Virtual Serial Port Driver](https://www.eltima.com/vspd-post-download.html?_ga=2.148845943.135235865.1634060891-52484055.1634060891)
 
 - Install [Null-modem emulator](https://sourceforge.net/projects/com0com/). This software create a virtual portal (COM3, COM4) that we will use it. When finished, it will ask to install a Virtual Device. Accept it.
At the end, check that all parameters are like the image below:
<h1 align="center">
  <img 
    src="./Doc/nullModem.png"
  />
</h1>

Also, check that the virtual ports are listed in Device Manager as follow:
<h1 align="center">
  <img 
    src="./Doc/deviceManager.jpg"
  />
</h1>
Note: You may have a different COM number if your PC has other components.


- Install [COM Port Data Emulator](https://www.aggsoft.com/com-port-emulator/download.htm). This one it generates the traffic needed for the COM port using data from a .bin file.
At the end, check that all parameters in Device menu are like the image below:
<h1 align="center">
  <img 
    src="./Doc/dataEmulator1.png"
  />
</h1>

Also, check that the Data source is setted as follow:
<h1 align="center">
  <img 
    src="./Doc/dataEmulator2.jpg"
  />
</h1>


- Install [Virtual Serial Port Driver](https://www.eltima.com/vspd-post-download.html?_ga=2.148845943.135235865.1634060891-52484055.1634060891). This software allow us to view traffic and apps that are connected with COM ports. Once installed, click on "New bundle" / "Share" and select the COM3 port in the "Real port to share" option.
When finished, something similar to the image below should appear. This way the Virtual Serial Port Drive is listening to COM3 waiting for some activity.
<h1 align="center">
  <img 
    src="./Doc/virtualSerial.png"
  />
</h1>
 
  
```bash
  # Clone the project
  $ git clone https://github.com/abelgonzalez/COMPort.git
```
```bash
  # Enter directory
  $ cd COMPort
```

 

---
## 😎 How to Run
- Open the COM Port Data Emulator and Virtual Serial Port apps.
- In COM Port Data Emulator, click on the Start button
- The following should appear:
<h1 align="center">
  <img 
    src="./Doc/dataTx.png"
  />
</h1>
On the left, COM Port Data Emulator appears, indicating that Tx information is present, and on the right, Virtual Serial Port Driver Pro informs that COM3 is being used, that it has some active activity.

Now, we will run our script
 
- In root folder (**COMPort**) run:
  ```bash
    # Run
    $ python main.py
  ```
- It will apper "Enter the participant's name. Ex: Lucas" message. Fill it and press Enter
- Then, will appear "Enter the participant's date of birth in DD/MM/YYYY format. Ex: 20/10/1996". Isert it with DD/MM/YYYY format and press Enter.
- Then,  "Which HRmax analysis method do you want to use? Enter the number only. Ex: 1" message appears. Pick one and press Enter.
- Insert the COM port in "Enter the port to connect and press Enter. Ex: COM3" message and press Enter.
- Finally, define how many seconds you want to capture in "Enter the quantity of measurements to capture and press Enter. Ex: 10" message. Insert it and press Enter.




We will see all data Tx as follow
<h1 align="center">
  <img 
    src="./Doc/dataTx.png"
  />
</h1>

Note:
- Check that the info is being Tx through COM3.
- After installing all the components, restart the computer if the reception of data in Python is not working.

---
## 👉 Additional information
* In case of sensitive bugs like security vulnerabilities, don't hesitate to contact me at abelgodev@gmail.com instead of using the issue tracker. I value your effort to improve the security and privacy of this project!

---
## 📝 License
This project is under the MIT license. See the file <a href="https://github.com/abelgonzalez/UnifyRequirements/LICENSE">LICENCE</a> for more details.

---
## 🧑‍💻 Autor
<p align="center">Done with 💙 by Abel González Mondéjar</p>


[![LinkedIn Badge](https://img.shields.io/badge/-Abel_González_Mondéjar-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/abelgonzalezmondejar/)](https://www.linkedin.com/in/abelgonzalezmondejar/)

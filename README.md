# HackerspaceWorkbench
External workbenches in FreeCAD add extra tools for specific tasks.




**Prerequisites**

 - Install FreeCAD (>=0.20)

 - Install Python3 and Git

 - Know basics of Python and FreeCAD API (especially Part, Gui, App modules)



**Setup Directory Structure**



```

```



**Mod directory**

**App.getUserAppDataDir() in the Python console)**


```
>>> App.getUserAppDataDir()
'/home/cnc/.local/share/FreeCAD/'



Paste the repository into this location:

/home/cnc/.local/share/FreeCAD/Mod/


```



**Use this command to create the symlink:**

```
ln -s /home/cnc/Desktop/MY_GIT/HackerspaceWorkbench/HackerspaceWorkbench /home/cnc/.local/share/FreeCAD/Mod/HackerspaceWorkbench



rm /home/cnc/.local/share/FreeCAD/Mod/HackerspaceWorkbench

```



**Todo**





**help**


```

https://github.com/FreeCAD/freecad.workbench_starterkit

```

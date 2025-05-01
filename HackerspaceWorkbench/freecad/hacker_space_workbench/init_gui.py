import os
import FreeCADGui as Gui
import FreeCAD as App
from freecad. hacker_space_workbench import my_numpy_function
from PySide2.QtWidgets import QMessageBox

translate=App.Qt.translate
QT_TRANSLATE_NOOP=App.Qt.QT_TRANSLATE_NOOP

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")
TRANSLATIONSPATH = os.path.join(os.path.dirname(__file__), "resources", "translations")

# Add translations path
Gui.addLanguagePath(TRANSLATIONSPATH)
Gui.updateLocale()


class MySimpleCommand:
    def GetResources(self):
        return {
            'Pixmap': os.path.join(ICONPATH, 'cool.svg'),
            'MenuText': "Say Hello",
            'ToolTip': "Prints Hello from Hackerspace"
        }

    def Activated(self):
        QMessageBox.information(None, "Hackerspace", "Hello from Hackerspace!")

    def IsActive(self):
        return True




# class MySimpleCommand:
#     def GetResources(self):
#         return {
#             'Pixmap': os.path.join(ICONPATH, 'cool.svg'),  # icon
#             'MenuText': "Say Hello",
#             'ToolTip': "Prints Hello from Hackerspace"
#         }
# 
#     def Activated(self):
#         #App.Console.PrintMessage("Hello from Hackerspace!\n")
#         print("Hello from Hackerspace!")
# 
# 
#     def IsActive(self):
#         return True


class HKWorkBench(Gui.Workbench):
    """
    class which gets initiated at startup of the gui
    """
    MenuText = translate("Workbench", "HackerspaceWorkbench")
    ToolTip = translate("Workbench", "a simple HackerspaceWorkbench")
    Icon = os.path.join(ICONPATH, "cool.svg")
    toolbox = []

    def GetClassName(self):
        return "Gui::PythonWorkbench"


    def Initialize(self):
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """


        App.Console.PrintMessage(translate("Log", "Switching to hacker_space_workbench") + "\n")
        App.Console.PrintMessage(translate("Log", "Run a numpy function:") + "sqrt(100) = {}\n".format(my_numpy_function.my_foo(100)))

        # NOTE: toolbox
        self.toolbox = ['My_Hello_Command']

        # NOTE: Context for this commands must be "Workbench"
        self.appendToolbar(QT_TRANSLATE_NOOP("Workbench", "Tools"), self.toolbox)
        self.appendMenu(QT_TRANSLATE_NOOP("Workbench", "Tools"), self.toolbox)


    def Activated(self):
        '''
        code which should be computed when a user switch to this workbench
        '''
        App.Console.PrintMessage(translate(
            "Log",
            "Workbench hacker_space_workbench activated.") + "\n")

    def Deactivated(self):
        '''
        code which should be computed when this workbench is deactivated
        '''
        App.Console.PrintMessage(translate(
            "Log",
            "Workbench hacker_space_workbench de-activated.") + "\n")


Gui.addWorkbench(HKWorkBench())
Gui.addCommand('My_Hello_Command', MySimpleCommand())
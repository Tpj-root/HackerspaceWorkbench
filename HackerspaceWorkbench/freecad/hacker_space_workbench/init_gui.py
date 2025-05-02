import os
import FreeCADGui as Gui
import FreeCAD as App
from freecad.hacker_space_workbench import my_numpy_function
from PySide2.QtWidgets import QMessageBox

translate = App.Qt.translate
QT_TRANSLATE_NOOP = App.Qt.QT_TRANSLATE_NOOP

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")
TRANSLATIONSPATH = os.path.join(os.path.dirname(__file__), "resources", "translations")

# Add translations path
Gui.addLanguagePath(TRANSLATIONSPATH)
Gui.updateLocale()


class MySimpleCommand:
    def GetResources(self):
        return {
            'Pixmap': '',  # Optional icon
            'MenuText': "count",
            'ToolTip': "Displays shape info"
        }

    def Activated(self):
        if Gui.ActiveDocument is None:
            QMessageBox.warning(None, "Error", "No active document.")
            return

        selection = Gui.Selection.getSelection()
        if not selection:
            QMessageBox.warning(None, "Error", "No object selected.")
            return

        obj = selection[0]

        if hasattr(obj, 'Shape') and obj.Shape and not obj.Shape.isNull():
            shape = obj.Shape
            if shape.isValid():
                face_count = len(shape.Faces)
                edge_count = len(shape.Edges)
                vertex_count = len(shape.Vertexes)

                QMessageBox.information(None, "Object Info",
                    f"Object: {obj.Name}\nFace count: {face_count}\nEdge count: {edge_count}\nVertex count: {vertex_count}")
                return

        QMessageBox.warning(None, "Error", "No valid shape object found.")

    def IsActive(self):
        return True


class HKWorkBench(Gui.Workbench):
    MenuText = translate("Workbench", "HackerspaceWorkbench")
    ToolTip = translate("Workbench", "A simple HackerspaceWorkbench")
    Icon = os.path.join(ICONPATH, "cool.svg")
    toolbox = []

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        App.Console.PrintMessage(translate("Log", "Switching to hacker_space_workbench") + "\n")
        App.Console.PrintMessage(translate("Log", "Run a numpy function:") + f" sqrt(100) = {my_numpy_function.my_foo(100)}\n")

        self.toolbox = ['My_Hello_Command']
        self.appendToolbar(QT_TRANSLATE_NOOP("Workbench", "Tools"), self.toolbox)
        self.appendMenu(QT_TRANSLATE_NOOP("Workbench", "Tools"), self.toolbox)

    def Activated(self):
        App.Console.PrintMessage(translate("Log", "Workbench hacker_space_workbench activated.") + "\n")

    def Deactivated(self):
        App.Console.PrintMessage(translate("Log", "Workbench hacker_space_workbench de-activated.") + "\n")


Gui.addWorkbench(HKWorkBench())
Gui.addCommand('My_Hello_Command', MySimpleCommand())

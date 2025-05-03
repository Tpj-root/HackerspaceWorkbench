# HackerspaceWorkbench
External workbenches in FreeCAD add extra tools for specific tasks.



To list all objects in your FreeCAD document and get their names via Python:

1. Open the **Python Console** (View → Panels → Python Console).
2. Use the following code:

```python
import FreeCAD
doc = FreeCAD.ActiveDocument

# List all object names in the active document
for obj in doc.Objects:
    print(obj.Name)
```

This will output the names of all objects in the active document.



---



FreeCAD (Part or Part Design workbench):

    Select the object in the tree.

    Open the Python Console (View → Panels → Python console).

    Run this code:


```
obj = App.ActiveDocument.getObject("YourObjectName")
shape = obj.Shape
print("Faces:", len(shape.Faces))
print("Vertices:", len(shape.Vertexes))
print("Edges:", len(shape.Edges))


```


Replace "YourObjectName" with the actual name of your object.


---



Select the object in the 3D view or Combo Tree.

Go to the Top Menu:

    Part → Check Geometry

In the Check Geometry task panel:

    Click Analyze

    It shows details like number of vertices, edges, faces, and any geometry issues.











```
import FreeCAD as App
import FreeCADGui as Gui

# Get the active document
doc = App.ActiveDocument

# Replace with the name of your object in the document
obj_name = "Box"  # Replace with your object name
obj = doc.getObject(obj_name)

# Check if the object exists
if obj:
    shape = obj.Shape
    
    # Shape info
    print(f"Checked object: {obj.Name}")
    print(f"Shape type: {shape.ShapeType}")
    print(f"Vertices: {len(shape.Vertexes)}")
    print(f"Edges: {len(shape.Edges)}")
    print(f"Wires: {len(shape.Wires)}")
    print(f"Faces: {len(shape.Faces)}")
    print(f"Shells: {len(shape.Shells)}")
    print(f"Solids: {len(shape.Solids)}")
    print(f"CompSolids: {len(shape.CompSolids)}")
    print(f"Compounds: {len(shape.Compounds)}")
    print(f"SubShapes (for Solids): {len(shape.SubShapes)}")  # SubShapes for Solids
    
    # Area and volume
    area = shape.Area
    volume = shape.Volume
    print(f"----------")
    print(f"Area: {area}")
    print(f"Volume: {volume}")
    
#    # Mass properties (assuming the object is a valid solid)
#    if shape.isValid():
#        # Get the mass properties
#        mass_properties = shape.getMassProperties()
#        print(f"Mass: {mass_properties[0]}")  # Mass is the first value
#        print(f"Center of mass: {mass_properties[1]}")  # Center of mass is the second value
#        print(f"Moments of inertia: {mass_properties[2]}")  # Moments of inertia
#        print(f"Radius of Gyration: {mass_properties[3]}")  # Radius of gyration
#    else:
#        print("The shape is not a valid solid object.")
#    
#    # Length (if applicable, like for a wire)
#    if hasattr(shape, 'Length'):
#        print(f"Length: {shape.Length}")
#    
#    # Orientation and symmetry (using placement)
#    placement = shape.Placement
#    print(f"Global placement = {placement}")
#    
#    # Symmetry (based on the specific object, might need custom checks)
#    print(f"Symmetry Axis: {shape.isSymmetric()}")
#    print(f"Symmetry Point: {shape.isSymmetric()}")

else:
    print(f"Object with name '{obj_name}' not found.")


```




To list all workbenches with their index numbers in FreeCAD using Python:

```python
for i, wb in enumerate(Gui.listWorkbenches()):
    print(f"{i}: {wb}")
```

This will output something like:

```
0: NoneWorkbench
1: AssemblyWorkbench
2: BIMWorkbench
3: CAMWorkbench
4: DraftWorkbench
5: FemWorkbench
6: InspectionWorkbench
7: MaterialWorkbench
8: MeshWorkbench
9: OpenSCADWorkbench
10: PartWorkbench
11: PartDesignWorkbench
12: PointsWorkbench
13: ReverseEngineeringWorkbench
14: RobotWorkbench
15: SketcherWorkbench
16: SpreadsheetWorkbench
17: SurfaceWorkbench
18: TechDrawWorkbench
19: TestWorkbench
20: A2plusWorkbench
21: HKWorkBench
```

Then you can use `Gui.runCommand('WorkbenchName', index)` accordingly.




```
Gui.runCommand('Std_Workbench',19)

```



**To enable or disable the status bar via FreeCAD Python console:**

```python
# Hide status bar
Gui.getMainWindow().statusBar().hide()

# Show status bar
Gui.getMainWindow().statusBar().show()
```


```

Gui.runCommand('Std_ViewStatusBar',0)
Gui.runCommand('Std_ViewStatusBar',1)
```









**HELP**



```

https://github.com/FreeCAD/FreeCAD/blob/b3a3b13603e7c48c6349080a893471ae9c105bc1/src/Mod/Part/Gui/Command.cpp#L2042
```
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
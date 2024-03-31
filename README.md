# temptower-gcode-adjustment
Set the temperature adjustment for your temptower gcode file.
This is a python-postprocessing-script for temptower gcode files.
Enter the values ​​you use in your slicer in the temptower-postprocessing.py file instead of the default values with an texteditor of your choice.


## Configuration:
- Set the filepath of your gcode.
```python
gcode_file_path = "./Temptower.gcode"
```
- Set outputpath. You can set new_Temptower to any name you want. For default it will create a folder named "output" in the current directory.
```python
gcode_output_file_path = "./output/new_Temptower.gcode"
```
- Set your start temperature. 
```python
temp = 250
``` 
- Set the temperature increase per level
```python
temp_increase = 5
```
- Set the baseheight in millimeters. If no base exists, set to 0.
```python
base_layer_heigt_in_mm = 1
```
- Set the height of your levels in millimeters.
```python
temp_step_height_in_mm = 10
```
- Set the layerheight of your gcode. The height of your first layer has to be the same as the other layers.
```python
layer_height = 0.2
```

## Usage:
```bash
py temptower-postprocessing.py
```


## Downloads:
[Printables Temperature-Tower](https://www.printables.com/de/model/827333-temperature-tower/files)

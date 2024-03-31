import os
if not os.path.isdir("./output"):
    os.mkdir("./output")
gcode_file_path = "./Temptower.gcode"
gcode_output_file_path = "./output/new_Temptower.gcode"
temp = 250
temp_increase = 5
base_layer_heigt_in_mm = 1
temp_level_height_in_mm = 10
layer_height = 0.2

new_lines = []
layer = 0
layer_count = 0

with open(gcode_file_path) as gcode_file:
    lines = gcode_file.readlines()

for line in lines:
    if line.startswith(";LAYER_CHANGE"):
        layer += 1
layer_z = layer * layer_height


for line in lines:
    if line.startswith(";LAYER_CHANGE"):
        layer_count += 1
        new_lines.append(line)
        if layer_count in [x for x in range(round((base_layer_heigt_in_mm + layer_height) / layer_height), layer,
                                            round(temp_level_height_in_mm / layer_height))]:
            new_lines.append("M104 S" + str(temp))
            temp -= temp_increase
    else:
        new_lines.append(line)

with open(gcode_output_file_path, "w") as new_gcode_file:
    new_gcode_file.writelines(new_lines)

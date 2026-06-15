# Automatic House Maker

## What does it do?
A Maya tool that creates a building from configuration parameters.
Attributes for each element can be edited as desired by the user.

## Features
-Core geometry functions
-Data-driven configuration
-Error handing in case of invalid parameters

##Project Structure
```
house_geometry.py  #create_body, create_porch, create_door, create_window, create_roof, create_chimney
house_materials.py # create_material, assign_material
main.py            # Entry point, config, build_house()
README.md          # This file
```

### Functions

### fortress_geometry.py
- `create_body(body_width, body_height, body_length, position)` -a rectangular body of the house
- `create_porch(wall_width, wall_height, wall_thickness, position)` — a rectangular porch
- `create_door(door_width, door_height, door_thickness, position)` — a rectangular door
- `create_window(window_width, window_height, window_thickness, position)` — a rectangular window
- `create_roof(roof_width, roof_height, roof_length, position)` — a rectangular roof
- `create_chimney(chimney_radius, roof_height, position)` — a cyllindrical chimney with a base and a topper
  
### fortress_materials.py
- `create_material(name, color)` — Lambert shader with RGB color
- `assign_material(obj_name, shader_name)` — Apply shader to object/group

## How to Run
1. Open Maya
2. Open Script Editor (Windows > General Editors > Script Editor)
3. Source `main.py` from the Automatic_House_Maker folder

## Author
Anton Yemelianov | DIGM 131 | Drexel University

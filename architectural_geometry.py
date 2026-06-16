"""
architectural_geometry.py -- Builder for a simple house structure
=========================================================================
DIGM 131 Final | Author: Anton Yemelianov

Each function creates one type of house element with input
validation and debug logging. No materials or scene logic here.

Usage:
    import house_geometry as geo
    geo.create_roof(roof_length=10, roof_height=1, roof_width=5, position=(0, 0, 8))
"""

import maya.cmds as cmds
import random

DEBUG = True


def create_body(body_width=5.0,
                body_height=0.3,
                body_length=5.0,
                position=(0, 0 ,0)):
    """Create a rectangular body of the building

    Args:
        body_width (float):     Body width. Default 5.
        body_thickness (float): Body Height. Default 3.
        body_length (float):    Body length. Default 5.
        position (tuple):  (x, y, z) center of the body.

    Returns:
        Str: Name of the body transform node or none if failure.
    """
    if DEBUG:
        print("[DEBUG] create_body: bw={}, bh{}, bl={}, pos={}".format(
        body_width, body_height, body_length, position))

    if body_width < 1.0:
        cmds.warning("invalid body width {} -- using default 5".format(body_width))
        body_width = 5
    if body_height < 0.5:
        cmds.warning("invalid body height {} -- using default 0.5".format(body_height))
        body_height = 3
    if body_length < 1.0:
        cmds.warning("invalid body length {} -- using default 5".format(body_length))
        body_length = 5

    try:
        body = cmds.polyCube(width=body_width,
                          height=body_height,
                          depth=body_length,
                          name="body_#"
        )[0]
        cmds.move(
              position[0],
              position[1] + body_height / 2.0,
              position[2],
              body
        )
    except Exception as error:
            cmds.warning("Failed to create body: {}".format(error))
            return None

    return body

def create_door(door_width=0.5,
                door_height=1,
                door_thickness=0.1,
                position=(0, 0, 0)):
    """Create a rectangular door

    Args:
        door_width (float):     Door width. Default 0.5.
        door_height (float):    Door Height. Default 1.
        door_thickness (float): Door length. Default 0.1.
        position (tuple):  (x, y, z) center of the body.

    Returns:
        Str: Name of the door transform node or none if failure.
    """
    if DEBUG:
        print("[DEBUG] create_door: dw={}, dh{}, dt={}, pos={}".format(
      door_width, door_height, door_thickness, position))

    if door_width < 0.1:
        cmds.warning("invalid door width {} -- using default 0.5".format(door_width))
        door_width = 0.5
    if door_height < 0.2:
        cmds.warning("invalid door height {} -- using default 1".format(door_height))
        door_height = 1
    if door_thickness < 0.05:
        cmds.warning("invalid door thickness {} -- using default 0.1".format(door_length))
        door_thickness = 0.1
      
    try:
        door = cmds.polyCube(
                             width=door_width, 
                             height=door_height,
                             depth=door_thickness,
                             name="door_#"
        )[0]
        cmds.move(
            position[0],
            position[1] + door_height / 2.0 + porch_height,
            position[2] + body_length / 2.0 + door_thickness / 2.0,
            door
        )
    except Exception as error:
        cmds.warning(warning("Failed to create door: {}".format(error))
        return None
      
    return door


def create_window(window_width=0.5,
                  window_height=0.5,
                  window_thickness=0.1,
                  position=(0, 0, 0)):
    """Create a rectangular (default square) window

    Args:
        window_width (float):     Window width. Default 0.5.
        window_height (float):    Window Height. Default 1.
        window_thickness (float): Window length. Default 0.1.
        position (tuple):  (x, y, z) center of the window.

    Returns:
        Str: Name of the window transform node or none if failure.
    """
    if DEBUG:
        print("[DEBUG] create_window: ww={}, wh{}, wt={}, pos={}".format(
      window_width, window_height, window_thickness, position))

    if window_width < 0.1:
        cmds.warning("invalid window width {} -- using default 0.5".format(window_width))
        window_width = 0.5
    if window_height < 0.1:
        cmds.warning("invalid window height {} -- using default 1".format(window_height))
        window_height = 0.5
    if window_thickness < 0.05:
        cmds.warning("invalid window thickness {} -- using default 0.1".format(window_length))
        window_thickness = 0.1
      
    try:
        window = cmds.polyCube(
                             width=window_width, 
                             height=window_height,
                             depth=window_thickness,
                             name="window_#"
        )[0]
        displace1 = -3/4 * body_width
        displace2 = 3/4 * body_width
        random_displace=random.choice([displace1, displace2])
      
        cmds.move(
            position[0] + random_displace,
            position[1] + window_height / 2.0 + porch_height,
            position[2] + body_length / 2.0 + window_length / 2.0,
            window
        )
    except Exception as error:
        cmds.warning(warning("Failed to create window: {}".format(error))
        return None
      
    return window
        
      

def create_porch(porch_width=1, porch_height=0.5, porch_length=1,
                 stair_width=porch_width / 2.0,
                 stair_height=porch height / 4.0,
                 stair_length=porch_length / 10.0
                 position=(0, 0 ,0)):
    """Create a rectangular porch with some stairs 

    Args:
        porch_width (float):  Porch width. Default 1.
        porch_height (float): Porch height. Default 0.5.
        porch_length (float): Porch length. Default 1.
        position (tuple):     (x, y, z) center of the porch base.

    Returns:
        Str: Name of the wall transform node or none if failure.
    """
    if DEBUG:
        print("[DEBUG] create_porrch: pw={}, ph{}, pl={}, pos={}".format(
        porch_width, porch_height, porch_thickness, position))

    if porch_width < 0.1:
        cmds.warning("invalid porch width {} -- using default 5".format(porch_length))
        wall_width = 1
    if porch_height < 0.05:
        cmds.warning("invalid porch height {} -- using default 0.5".format(porch_height))
        wall_height = 0.5
    if porch_length < 0.1:
        cmds.warning("invalid porch thickness {} -- using default 5".format(porch_length))
        porch_length = 10

    try:
        porch = cmds.polyCube(width=porch_width, 
            height=porch_height,
            depth=porch_length,
            name="porch_#"
        )[0]
        cmds.move(
            (position[0],
             position[1] + porch_height / 2.0,
             position[2] + body_length / 2.0
             porch
        )    
    except Exception as error:
    cmds.warning("Failed to create porch: {}".format(error))
        return None

    return porch

def create_roof(roof_width=body_width+0.1,
                roof_height=0.5,
                roof_length=body_length+0.1,
                position=(0, 0, 0)):
    """Creates a rectangular roof
    Args:
        roof_width (float):  Roof width. Default body width + 0.1.
        roof_height (float): Roof height. Default 0.5.
        roof_length (float): Roof length. Default body length + 0.1.
        position (tuple):    (x, y, z) center of the roof base.

    Returns:
        Str: Name of the roof transform node or none if failure.
    """
    if DEBUG:
        print("[DEBUG] create_roof: rw={}, rh{}, rl={}, pos={}".format(
            roof_width, roof_height, roof_length, position))

    if roof_width < body_width
        cmds.warning("invalid roof length {} -- using default body length + 0.1".format(roof_width))
        roof_width=body_width + 0.1
    if roof_height < 0.1:
        cmds.warning("invalid wall height {} -- using default 0.5".format(roof_height))
        roof_height = 0.5
    if roof_length < body_width
        cmds.warning("invalid wall thickness {} -- using default body legth + 0.1".format(roof_length))
        roof_length = body_length + 0.1
    try:
        roof = cmds.polyCube(width=roof_width, 
                            height=roof_height, 
                            depth=roof_length,
                            name="roof_#"
        )[0]
        cmds.move(
            position[0],
            position[1] / 2.0 + body_height,
            position[2], 
            roof
        )
    except Exception as error:
        cmds.warning("Failed to create roof: {}".format(error))
        return None

    return roof

def create_chimney(chimney_base_radius=0.2,
                   chimney_base_height=1,
                   chimney_top_radius=chimney_radius * 1.5,
                   chimney_top_height=chimney_height * 0.2,
                   position=(0, 0, 0)):
    """Create a chimney consisting of two cylinders

    Args:
        chimney_base_radius(float): Chimney radius. Default 0.2.
        chimney_base_height(float): Chimney's height. Default 1.
        position (tuple):           (x, y, z) center of the chimney base.
    Returns:
        str: Name of the gatehouse group, or None on failure.
    """
    if DEBUG:
        print("[DEBUG] create_chimney: cr={}, ch={} pos={}".format(
            chimney_radius, chimney_height, position))

    if chimney_radius < 0.01
        cmds.warning("invalid chimney radius {} -- using default 0.2".format(chimney_radius))
        chimney_radius = 0.2
    if chimney_base_height < 0.05:
        cmds.warning("invalid chimney height {} -- using default 0.5".format(chimney_height))
        chimney_base_height=1
        
    parts = []

    try:
        #base
        chimney_base = cmds.polyCylinder(
            radius=chimney_base_radius,
            height=chimney_base_height,
            name="chimney_base_#"
        )[0]
        cmds.move(
            position[0],
            position[1] + chimney_base_height / 2.0,
            position[2],
            chimney_base
        )

        #topper
        chimney_top = cmds.polyCylinder(
            radius=chimney_top_radius,
            height=chimney_top_height,
            name="chimney_top_#"
        )[0]
        cmds.move(
            position[0],
            position[1] + chimney_top_height / 2.0 + chimney_base_height,
            position[2]
        )
        cmds.group(chimney_base, chimney_top, name="chimney_#")
        cmds.move(
            position[0],
            position[1] + body_height + roof_height,
            position[2],
            chimney
        )
    except Exception as error:
        cmds.warning("Failed to create chimney: {}".format(error))
        return None

return cmds.group(chimney_base, chimney_top, name="chimney_#")
                     

if __name__ == "__main__":
    cmds.file(new=True, force=True)

    create_body(body_width=10, body_height=5, body_length=10, position=(0, 0, 0))
    create_porch(porch_width=1, porch_height=0.2, porch_length=2, position=(0, 0, 0))
    create_roof(roof_width=11, roof_height=0.1, roof_length=11, position=(0, 0, 0))
    create_chimney(chimney_radius=0.3, chimney_height=0.2, position=(0, 0, 0))
    create_window(window_thickness=1, window_height=1, window_width=1, position=(0, 0, 0))
    create_door(door_width=thickness, door_height=2, door_width=1, position=(0, 0, 0))

    # Test error handling
    print("\n--- Error handling tests ---")
    create_body(body_width=-1, body_height=-1, body_length=-1) # should warn, use defaults
    create_door(door_thickness=0, door_height=0.0001, door_width=-4
    cmds.viewFit(allObjects=True)
    print("house_geometry self-test complete!")

      
                 

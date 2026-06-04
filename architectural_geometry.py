import maya.cmds as cmds

DEBUG = True


def create_body(body_width=5.0, body_height=0.5, body_length=5.0,
                 position=(0, 0 ,0):
    """Create a rectangular body of the building

    Args:
        body_width (float):     Body width. Default 5.
        body_thickness (float): Body Height. Default 3.
        body_length (float):    Body length. Default 5.
        position (tuple):  (x, y, z) center of the body.

    Returns:
        Str: Name of the floor transform node or none if failure.
    """
if DEBUG:
    print("[DEBUG] create_body: bw={}, bh{}, bl={}, pos={}".format(
      body_width, body_height, body_length, position))

if body_width < 1.0:
    cmds.warning("invalid body width {} -- using default 5".format(body_width))
    body_width=5
if body_height < 0.5:
    cmds.warning("invalid body height {} -- using default 0.5".format(body_height))
    body_height=0.
if body_length < 1.0:
    cmds.warning("invalid body length {} -- using default 5".format(body_length))
    body=length=5

    try:
        floor = cmds.polyCube(width=floor_width, 
                          height=floor_thickness,
                          depth=floor_length,
                          name="floor_#"
        )[0]
        cmds.move(
            (position[0], position[1] + floor_thickness / 2.0, position[2], wall
        )
    except Exception as error:
      cmds.warning("Failed to create body: {}".format(error))
      return none

return body


def create_porch(porch_width=1, porch_height=0.5, porch_width=1,
                 stair_width=porch_width / 2.0,
                 stair_height=porch height / 4.0,
                 position=(0, 0 ,0):
    """Create a rectangular porch with some stairs 

    Args:
        porch_length (float):    Porch length. Default 5.
        porch_height (float):    Porch height. Default 3.
        porch_width (float): Floor length. Default 0.2.
        position (tuple):  (x, y, z) center of the floor base.

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
            (position[0], position[1] + porch_height/ 2.0, position[2], porch
        )
        stair1 = cmds.polyCube(width=stair_width, 
                          height=stair_height,
                          depth=porch_length,
                          name="stair_#
        )                      
        
    except Exception as error:
    cmds.warning("Failed to create porch: {}".format(error))
      return none

def create_roof(roof_width=floor_width+wall_thickness+0.1,
               roof_height=0.5,
               roof_length=floor_length+wall_thickness+0.1
               ):
    """Creates a rectangular roof
Args:
        wall_length (float):    Floor width. Default 5.
        wall_height (float):    Floor thickness. Default 3.
        wall_thickness (float): Floor length. Default 0.2.
        position (tuple):  (x, y, z) center of the floor base.

    Returns:
        Str: Name of the wall transform node or none if failure.
    """
if DEBUG:
    print("[DEBUG] create_wall: wl={}, wh{}, wt={}, pos={}".format(
      roof_length, roof_height, roof_thickness, position))

if roof_width < floor_length + wall_thickness:
    cmds.warning("invalid roof length {} -- using default 5".format(wall_length))
    roof_width=10
if roof_height < 0.1:
    cmds.warning("invalid wall height {} -- using default 0.5".format(wall_height))
    roof_height=0.5
if roof_height < 0.1:
    cmds.warning("invalid wall thickness {} -- using default 5".format(wall_thickness))
    roof_length=10
try:
      roof = cmds.polyCube(width=roof_width, 
            height=roof_height, 
            depth=roof_length,
            name="roof_#"
        )[0]
  cmds.move(
      (position[0], position[1] / 2.0, position[2], roof
  )
    except Exception as error:
      cmds.warning("Failed to create roof: {}".format(error))
      return None

    return wall

def create_chimney(chimney_radius=0.2, chimney_height=1,
                   chimney_top_radius=chimney_radius * 1.5,
                   chimney_top_height=chimney_height * 0.2,
                   position=(0, 0, 0)):
    """Create a chimney consisting of two cylinders

    Args:
        chimney_radius(float): Chimney radius. Default 0.2.
        chimney_height(float): Chimney's height. Default 1.
        chimney_top_radius: Radius of the chimney topper. 
        Default to chimney_top_radius=chimney_radius * 1.5

    Returns:
        str: Name of the gatehouse group, or None on failure.
    """
if DEBUG:
    print("[DEBUG] create_chimney: cr={}, ch={} pos={}".format(
      chimney_radius, chimney_height, position))

if roof_width < floor_length + wall_thickness:
    cmds.warning("invalid roof length {} -- using default 5".format(wall_length))
    roof_width=10
if roof_height < 0.1:
    cmds.warning("invalid wall height {} -- using default 0.5".format(wall_height))
    roof_height=0.5
if roof_height < 0.1:
    cmds.warning("invalid wall thickness {} -- using default 5".format(wall_thickness))
    roof_length=10
try:
      roof = cmds.polyCube(width=roof_width, 
            height=roof_height, 
            depth=roof_length,
            name="roof_#"
        )[0]
  cmds.move(
      (position[0], position[1] / 2.0, position[2], roof
  )
    except Exception as error:
      cmds.warning("Failed to create roof: {}".format(error))
      return None

    return wall
                     

if __name__ == "__main__":
    cmds.file(new=True, force=True)

    create_body
    create_porch
    create_roof
    create_chimney
    create_window
    create_door

    # Test error handling
    print("\n--- Error handling tests ---")
    create_body(body_width=-1, body_height=-1, body_length=-1) # should warn, use defaults

    cmds.viewFit(allObjects=True)
    print("house_geometry self-test complete!")

      
                 

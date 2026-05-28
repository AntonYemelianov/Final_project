import maya.cmds as cmds

DEBUG = True


def create_floor(floor_width=5.0, floor_thickness=0.5, floor_length=5.0,
                 position=(0, 0 ,0):
    """Create a rectangular floor

    Args:
        floor_width (float):     Floor width. Default 5.
        floor_thickness (float): Floor thickness. Default 0.5.
        floor_length (float):    Floor length. Default 5.
        position (tuple):  (x, y, z) center of the floor base.

    Returns:
        Str: Name of the floor transform node or none if failure.
    """
if DEBUG:
    print("[DEBUG] create_floor: fw={}, ft{}, fl={}, pos={}".format(
      floor_width, floor_thickness, floor_length, position))

if floor_width < 1.0:
    cmds.warning("invalid floor width {} -- using default 5".format(floor_width))
    floor_width=5
if floor_thickness < 0.1:
    cmds.warning("invalid floor thickness {} -- using default 0.5".format(floor_thickness))
    floor_thickness=0.
if floor_length < 1.0:
    cmds.warning("invalid floor length {} -- using default 5".format(floor_length))
    floor_length=5

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
      cmds.warning("Failed to create floor: {}".format(error))
      return none

return floor


def create_wall(wall_length=5.0, wall_height=3.0, wall_thickness=0.2,
                 position=(0, 0 ,0):
    """Create a  rectangular wall

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
      wall_length, wall_height, wall_thickness, position))

if wall_length < 1:
    cmds.warning("invalid wall length {} -- using default 5".format(wall_length))
    wall_length=10
if wall_height < 0.1:
    cmds.warning("invalid wall height {} -- using default 0.5".format(wall_height))
    wall_height=0.5
if wall_thickness < 1:
    cmds.warning("invalid wall thickness {} -- using default 5".format(wall_thickness))
    wall_thickness=10

    try:
        wall = cmds.polyCube(width=wall_length, 
                          height=wall_height,
                          depth=wall_thickness,
                          name="wall_#"
        )[0]
        cmds.move(
            (position[0], position[1] + wall_height/ 2.0, position[2], wall
        )
    except Exception as error:

def create_roof():
  """Creates a rectangular or pyramidal roof(random)"""

    #Define available roof shapes
    roof_shapes = ["cube", "pyramid"]
    #Make a random choice 
    roof_choice = random.choice(roof_shapes)
    # if-else function deciding which shape to create based on the random choice
    if roof_choice == "cube":
    else:
                 

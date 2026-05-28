import maya.cmds as cmds

DEBUG = True


def create_floor(floor_width=5, floor_thickness=0.5, floor_length=5,
                 position=(0, 0 ,0):
    """Create a floor

    Args:
        floor_width (float):    Floor width. Default 5.
        floor_thickness (float): Floor thickness. Default 0.5.
        floor_length (float):   Floor length. Default 5.
        position (tuple):  (x, y, z) center of the floor base.

    Returns:
        Str: Name of the floor transform node or none if failure.
    """
if DEBUG:
    print("[DEBUG] create_floor: fl={}, fh{}, fd={}, pos={}".format(
      floor_width, floor_thickness, floor_length, position))

if floor_width < 1:
    cmds.warning("invalid floor width {} -- using default 5".format(floor_width))
    width=10
if floor_thickness < 0.1:
    cmds.warning("invalid floor thickness {} -- using default 0.5".format(floor_thickness))
    width=0.5
if floor_length < 1:
    cmds.warning("invalid floor length {} -- using default 5".format(floor_length))
    width=10

    try:
        floor = cmds.polyCube(width=floor_width, 
                          height=floor_thickness,
                          depth=floor_length,
                          name="floor_#"
        )[0]
        cmds.move(
            (position[0], position[1] / 2.0, position[2], wall
        )
    except Exception as error:
      cmds.warning("Failed to create floor: {}".format(error))
      return none

return floor

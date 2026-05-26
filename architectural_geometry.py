import maya.cmds as cmds

DEBUG = True


def create_floor(floor_width=(random.uniform(0.1, 50)),
                 floor_thickness=(random.uniform(0.1, 50)), 
                 floor_length=(random.uniform(0.1, 50)),
                 position=(0, 0 ,0):
    """Create a floor

    Args:
        length (float):    Floor length. Random value between 0.1 and 50.
        thickness (float): Floor thickness. Random value between 0.1 and 50.
        width (float):     Floor width. Random value between 0.1 and 50.
        position (tuple):  (x, y, z) center of the floor base.

    Returns:
        Str: Name of the floor transform node or none if failure.
    """

    try:
        floor = cmds.polyCube(width=floor_width, 
                          height=floor_thickness,
                          depth=floor_length,
                          name="floor_#"
        )[0]
        cmds.move(
            (position[0], position[1] / 2.0, position[2], wall
        )

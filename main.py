"""
main.py -- House Generator (DIGM Final)
=======================================
Author: Anton Yemelianov

Assembles a house from configuration data using the builders dispatcher pattern.
"""

import maya.cmds as cmds
import architectural_geomentry as geo

HOUSE CONFIG = [
    #main body
    {"type":"body", "body_width": 8, "body_height": , "body_length": 12,
     "position": (0, 0 ,0)},
    #porch
    {"


#Confirguration Data
BUILDRES = {
"body":   geo.create_body,
"porch":    geo.create_porch,
"roof":    geo.create_roof,
"window":  geo.create_window,
"door":    geo.create_door,
"porch":   geo.create_porch,
"chimney": geo.create_chimney,
}

TYPE_MATERIAL = {
"floor": "floor",
"wall": "wall",
"roof": "roof",
"porch": "porch",
"chimney": "chimney"


#Dispatcher

#Driver
def build_house(config=None):
    """Build a house from confiuration data.

    Args:
       config (list): List of conifg dicts. Defaults to HOUSE_CONFIG.

    Returns:
        list: Names of all created Maya nodes.
    """
    if config is None:
        config = HOUSE_CONFIG

    cmds.file(new=True, force=True)

    shaders = {}
    for key, (name, color) in MATERIALS.items():
        shaders[key] = mat.create_material(name,color)

    ground = cmds.polyPlane( width=50, height=50, sx=1, sy=1, name="ground_#"
                           )[0]
    results = [ground]
#Main
if __name__ == "__main__":
    build_house()

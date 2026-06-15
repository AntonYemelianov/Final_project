"""
main.py -- House Generator (DIGM Final)
=======================================
Author: Anton Yemelianov

Assembles a house from configuration data using the builders dispatcher pattern.
"""

import maya.cmds as cmds
import architectural_geomentry as geo

HOUSE_CONFIG = [
    #main body
    {"type": "body", "body_width": 8, "body_length": 12,
     "position": (0, 0 ,0)},
    #porch
    {"type": "porch", "porch_width": 3, "porch_length

MATERIAL_PALETTE = [
"body":   ("white_concrete",  (1.0, 1.0, 1.0)),
"door":   ("wooden_door",     (0.58, 0.29, 0.0)),
"window": ("glass",           (0.4, 0.7, 1.0)),
"roof":   ("red_tiles",       (1.0, 0.0, 0.0)),
]

#Confirguration Data
BUILDRES = {
"body":    geo.create_body,
"porch":   geo.create_porch,
"roof":    geo.create_roof,
"window":  geo.create_window,
"door":    geo.create_door,
"porch":   geo.create_porch,
"chimney": geo.create_chimney,
}

TYPE_MATERIAL = {
"body": "body",
"door": "door",
"roof": "roof",
"porch": "porch",
"chimney": "chimney"

#---------------------------------------------------------------------------
#Dispatcher
#---------------------------------------------------------------------------
def create_element(data):
    """Dispatch one config entry to the correct builder function.

    Looks up data["type"] in BUILDERS and calls the matching function
    with the remaining keys as ** keyword arguments.

    Args:
        data (dict): One entry from HOUSE_CONFIG. Must have a "type" key.

    Returns:
        str or None: The created Maya node name, or None if failed.
    """
    element_type = data.get("type")

    #Check if the entry has a type:
    if not element_type:
        cmds.warning("Config entry missing "type" key -- skipping.")
        return None
        
    #Check if there is a builder for this type
    builder = BUILDERS.get(element_type)
    if not builder:
        cmds.warning("Unknown type '{}' -- skipping.".format(element_type))
        return None

    #Strip "type" before ** unpacking -- it's not a function parameter
    params = {k: v for k, v in data.items() if k != "type"}

    try:
        return builder(**params)
    except TypeError as error:
        cmds.warning("Bad params for '{}': {}".format(element_type, error))
        return None
        
    
# ---------------------------------------------------------------------------
#Driver
# ---------------------------------------------------------------------------
    
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
    
    # Materials
    shaders = {}
    for key, (name, color) in MATERIALS.items():
        shaders[key] = mat.create_material(name,color)
        
    # Ground plane
    ground = cmds.polyPlane( width=50,
                            height=50,
                            sx=1,
                            sy=1,
                            name="ground_#"
    )[0]
    
    results = [ground]

    #Process entry in the config
    for entry in config:
        obj = create_element(entry)
        if obj:
            # Auto assign material based on type
            mat_key = TYPE_MATERIALS.get(entry.get("type"))
            if mat_key and mat_key in shaders:
                mat.assign_material(obj, shaders[mat_key])
            results.append(obj)

        cmds.viewFit(allObjects=True)
        print("=== House Built ===")
        print("  {} elements from {} config entries.".format(
            len(results), len(config)))

        return results

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    build_house()

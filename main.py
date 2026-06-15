"""
main.py -- House Generator (DIGM Final)
===========================================================================
DIGM 131 Final | Author: Anton Yemelianov

Assembles a house from configuration data 
using the BUILDERS dispatcher pattern.
"""
import os
import sys
import maya.cmds as cmds

try:
    _THIS_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    _THIS_DIR = cmds.workspace(query=True, rootDirectory=True

if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)
                               
import house_materials as mat
import architectural_geomentry as geo

# ---------------------------------------------------------------------------
# Configuration Data
# ---------------------------------------------------------------------------
# Each dict is a "recipe" for one house element.
# "type" tells the dispatcher which function to call.
# The rest are parameters for that function.
# Add a new element = add one dict. No code changes needed.

HOUSE_CONFIG = [
    # Main body
    {"type": "body", "body_width": 8, "body_length": 12,
     "position": (0, 0 ,0)},
    
    # Porch
    {"type": "porch", "porch_width": 3, "porch_length": 1,
     "position": (0, 0, 0)},
    
    # Pouble door made out of two regular ones
    {"type": "door",
     "position": (-0.25, 0, 0)},
    {"type": "door",
     "position": (0.25, 0, 0)},

    # Windows
    {"type": "window", 
     "position": (0, 4.25, 0)},
    {"type": "window", 
     "position": (0, 5.25, 0)},
    {"type": "window", 
     "position": (0, 6.25, 0)},
    {"type": "window", 
     "position": (0, 4.25, 0)},
    {"type": "window", 
     "position": (0, 5.25, 0)},
    {"type": "window", 
     "position": (0, 6.25, 0)},

    # Roof
    {"type": "roof"
     "position": (0, 0, 0)},
]
    
MATERIAL_PALETTE = {
    "body":   ("white_concrete",  (1.0, 1.0, 1.0)),
    "porch":  ("white_concrete",  (1.0, 1.0, 1.0)),
    "door":   ("wooden_door",     (0.58, 0.29, 0.0)),
    "window": ("glass",           (0.4, 0.7, 1.0)),
    "roof":   ("red_tiles",       (1.0, 0.0, 0.0)),
}

# Mapping element type names to the functions that build them.
# Functions are values -- you can store them in a dict and call them by key.
BUILDRES = {
    "body":    geo.create_body,
    "porch":   geo.create_porch,
    "roof":    geo.create_roof,
    "window":  geo.create_window,
    "door":    geo.create_door,
    "porch":   geo.create_porch,
    "chimney": geo.create_chimney,
}

# Mapping element types to materials keys for auto-assignment
TYPE_MATERIAL = {
    "body":    "body",
    "door":    "door",
    "window":  "window"
    "roof":    "roof",
    "porch":   "porch",
    "chimney": "chimney"
}


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

    # Error handling test
    print("\n--- Error handling tests ---")
    create_element({"type": "body", "heigt": 2})     # Typo in key
    create_element({"height": 2})                    # Missing type
    create_element({"type": "lantern", "height": 2}) # Unknown type
    create_element({"type": "body", "heigt": -2})    # Invalid value
    print("--- All tests passed (warnings, not crashes) ---")

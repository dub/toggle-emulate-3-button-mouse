bl_info = {
    "name": "Toggle Emulate 3 Button Mouse",
    "blender": (3, 0, 0),
    "category": "3D View",
}

import bpy
from bpy.types import Operator


class TOGGLE_EMULATE_3_BUTTON_MOUSE_OT_operator(Operator):
    bl_idname = "wm.toggle_emulate_3_button_mouse"
    bl_label = "Toggle Emulate 3 Button Mouse"
    
    def execute(self, context):
        # Get the current state of the "Emulate 3 Button Mouse" setting
        prefs = context.preferences
        input_prefs = prefs.inputs
        
        # Toggle the preference
        input_prefs.use_mouse_emulate_3_button = not input_prefs.use_mouse_emulate_3_button
        
        # Get the new state and report it
        new_state = input_prefs.use_mouse_emulate_3_button
        self.report({'INFO'}, f"Emulate 3 Button Mouse: {'ON' if new_state else 'OFF'}")
        
        return {'FINISHED'}

def register():
    # Register the operator
    bpy.utils.register_class(TOGGLE_EMULATE_3_BUTTON_MOUSE_OT_operator)
    
    # Set the hotkey (Shift + Ctrl + Alt + M)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="Window", space_type='EMPTY')
        kmi = km.keymap_items.new(TOGGLE_EMULATE_3_BUTTON_MOUSE_OT_operator.bl_idname, 'M', 'PRESS', ctrl=True, shift=True, alt=True)

def unregister():
    # Unregister the operator
    bpy.utils.unregister_class(TOGGLE_EMULATE_3_BUTTON_MOUSE_OT_operator)
    
    # Remove the hotkey
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps['Window']
        for kmi in km.keymap_items:
            if kmi.idname == TOGGLE_EMULATE_3_BUTTON_MOUSE_OT_operator.bl_idname:
                km.keymap_items.remove(kmi)
                break

if __name__ == "__main__":
    register()

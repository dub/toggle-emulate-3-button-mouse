import bpy
from bpy.types import Operator

bl_info = {
    "name": "Toggle Emulate 3 Button Mouse",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Shift+Ctrl+Alt+M",
    "description": "Toggles the 'Emulate 3 Button Mouse' preference",
    "category": "User Interface",
}

class EMULATE_OT_toggle_three_button_mouse(Operator):
    bl_idname = "emulate.toggle_three_button_mouse"
    bl_label = "Toggle Emulate 3 Button Mouse"
    bl_description = "Toggle the 'Emulate 3 Button Mouse' preference"

    def execute(self, context):
        # Access user preferences
        preferences = context.preferences
        input_prefs = preferences.inputs

        # Toggle the preference
        input_prefs.use_mouse_emulate_3_button = not input_prefs.use_mouse_emulate_3_button

        # Prepare status message
        status = "ON" if input_prefs.use_mouse_emulate_3_button else "OFF"
        self.report({'INFO'}, f"Emulate 3 Button Mouse: {status}")

        return {'FINISHED'}

addon_keymaps = []

def register():
    bpy.utils.register_class(EMULATE_OT_toggle_three_button_mouse)

    # Add the keymap
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="Window", space_type='EMPTY')
        kmi = km.keymap_items.new(
            EMULATE_OT_toggle_three_button_mouse.bl_idname,
            type='M',
            value='PRESS',
            shift=True,
            ctrl=True,
            alt=True
        )
        addon_keymaps.append((km, kmi))

def unregister():
    # Remove the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    bpy.utils.unregister_class(EMULATE_OT_toggle_three_button_mouse)

if __name__ == "__main__":
    register()
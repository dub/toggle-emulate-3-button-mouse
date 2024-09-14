import bpy
import rna_keymap_ui
from bpy.types import Operator, AddonPreferences

bl_info = {
    "name": "Toggle Emulate 3 Button Mouse",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Shift+Ctrl+Alt+M",
    "description": "Toggles the 'Emulate 3 Button Mouse' preference",
    "category": "User Interface",
}

addon_keymaps = []

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
    

class EmulatePreference(AddonPreferences):
    bl_idname = __name__

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        box = row.box()
        box.label(text="Keymap")
        col = box.column()

        wm = bpy.context.window_manager
        kc = wm.keyconfigs.user
        old_km_name = ""
        get_kmi_1 = []
        for km_add, kmi_add in addon_keymaps:
            for km_con in kc.keymaps:
                if km_add.name == km_con.name:
                    km = km_con
                    break
            for kmi_con in km.keymap_items:
                if kmi_add.idname == kmi_con.idname:
                    if kmi_add.name == kmi_con.name:
                        get_kmi_1.append((km,kmi_con))

        get_kmi_1 = sorted(set(get_kmi_1), key=get_kmi_1.index)

        for km, kmi in get_kmi_1:
            if not km.name == old_km_name:
                col.label(text=str(km.name), icon="DOT")
            col.context_pointer_set("keymap", km)
            rna_keymap_ui.draw_kmi([],kc, km, kmi, col, 0)
            col.separator()
            old_km_name = km.name
            

def register():
    bpy.utils.register_class(EMULATE_OT_toggle_three_button_mouse)
    bpy.utils.register_class(EmulatePreference)

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
    bpy.utils.unregister_class(EmulatePreference)

if __name__ == "__main__":
    register()
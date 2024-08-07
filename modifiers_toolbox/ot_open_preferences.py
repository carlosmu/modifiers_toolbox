import bpy # type: ignore

class MTB_OT_open_preferences(bpy.types.Operator):
    """Open Addon Preferences"""
    bl_idname = "modifierstoolbox.open_preferences"
    bl_label = "Preferences"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        if (context.area.ui_type == 'PROPERTIES'):
            return True

    def execute(self, context):
        bpy.ops.screen.userpref_show('INVOKE_DEFAULT')
        if bpy.app.version < (4, 2, 0):
            bpy.context.preferences.active_section = 'ADDONS'
            bpy.data.window_managers["WinMan"].addon_search = "Modifiers Toolbox"
        else:
            bpy.context.preferences.active_section = 'EXTENSIONS'
            bpy.data.window_managers["WinMan"].extension_search = "Modifiers Toolbox"

        return{'FINISHED'}

##############################################
# REGISTER/UNREGISTER
##############################################
def register():
    bpy.utils.register_class(MTB_OT_open_preferences)


def unregister():
    bpy.utils.unregister_class(MTB_OT_open_preferences)
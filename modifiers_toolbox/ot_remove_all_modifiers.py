import bpy # type: ignore
class MTB_OT_remove_all_modifiers(bpy.types.Operator):
    """Remove all modifiers of selected objects"""
    bl_idname = "modifierstoolbox.remove_all_modifiers"
    bl_label = "Remove all modifiers in selected objects"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if (context.area.ui_type == 'PROPERTIES'):
            return True

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)
    
    def execute(self, context):
        objects = context.selected_objects
        if len(objects) > 0:
            for ob in objects:
                modifiers = get_modifiers(ob)
                if len(modifiers) > 0:
                    for mod in modifiers:
                        modifiers.remove(mod)
                else:
                    pass
                    
            self.report({"INFO"}, "All modifiers was removed")
        else:
            self.report({"WARNING"}, "Selected objects are needed")

        return{'FINISHED'}

def get_modifiers(object):
    if object.type == 'GPENCIL':
        return object.grease_pencil_modifiers
    return object.modifiers

##############################################
# REGISTER/UNREGISTER
##############################################
def register():
    bpy.utils.register_class(MTB_OT_remove_all_modifiers)


def unregister():
    bpy.utils.unregister_class(MTB_OT_remove_all_modifiers)
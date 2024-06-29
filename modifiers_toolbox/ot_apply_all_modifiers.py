import bpy # type: ignore

class MTB_OT_apply_all_modifiers(bpy.types.Operator):
    """Apply all modifiers of selected objects"""
    bl_idname = "modifierstoolbox.apply_all_modifiers"
    bl_label = "Apply all modifiers in selected objects"
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
            failed_list = []
            failures = False
            for ob in objects:
                try:
                    with bpy.context.temp_override(object=ob):
                        modifiers = get_modifiers(ob)
                        if len(modifiers) > 0:
                            for mod in modifiers:
                                bpy.ops.object.modifier_apply(modifier=mod.name)
                        else:
                            pass
                except:
                    failed_list.append(ob.name)                
                    failures = True    
            if failures:
                if len(failed_list) < 5:
                    self.report({"WARNING"}, f"Failed on following objects: {failed_list}")
                else:
                    self.report({"WARNING"}, f"Failed on several objects")
            else:
                self.report({"INFO"}, "All modifiers was applied")
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
    bpy.utils.register_class(MTB_OT_apply_all_modifiers)


def unregister():
    bpy.utils.unregister_class(MTB_OT_apply_all_modifiers)
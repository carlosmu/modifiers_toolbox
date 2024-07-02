import bpy # type: ignore
# from bpy.props import EnumProperty

class MTB_OT_display_toggles(bpy.types.Operator):
    """Toggle display for all modifiers. Assigned modifiers are needed."""
    bl_idname = "modifierstoolbox.display_toggles"
    bl_label = "Toggle display for all modifiers"
    bl_options = {'REGISTER', 'UNDO'}
    enum_items = (
        ('SHOW_EXPANDED', '', '', 'MOD_MIRROR', 0),
        ('SHOW_VIEWPORT', '', '', 'RECOVER_LAST', 1),
        ('SHOW_RENDER', '', '', 'RECOVER_LAST', 2),
    )

    action: bpy.props.EnumProperty(items=enum_items) # type: ignore

    @classmethod
    def poll(cls, context):
        if (context.area.ui_type == 'PROPERTIES'):
            return True

    def execute(self, context):
        active = context.active_object
        modifiers = get_modifiers(active)

        if len(modifiers) > 0:
            if self.action == 'SHOW_EXPANDED':        
                bool_value = False if modifiers[0].show_expanded == True else True
                for mod in modifiers:            
                    mod.show_expanded = bool_value

            elif self.action == 'SHOW_VIEWPORT':
                bool_value = False if modifiers[0].show_viewport == True else True
                for mod in modifiers:            
                    mod.show_viewport = bool_value
            
            else:
                bool_value = False if modifiers[0].show_render == True else True
                for mod in modifiers:            
                    mod.show_render = bool_value
        else:
            self.report({"INFO"}, "Assigned modifiers are needed")

        return{'FINISHED'}

def get_modifiers(object):
    if object.type == 'GPENCIL':
        return object.grease_pencil_modifiers
    return object.modifiers

##############################################
# REGISTER/UNREGISTER
##############################################
def register():
    bpy.utils.register_class(MTB_OT_display_toggles)


def unregister():
    bpy.utils.unregister_class(MTB_OT_display_toggles)
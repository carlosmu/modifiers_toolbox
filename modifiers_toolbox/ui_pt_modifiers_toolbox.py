import bpy # type: ignore
from . import ui_favourite_modifiers
from . import ui_add_modifier_menu
from . import ot_open_preferences

class MTB_PT_Modifiers_toolbox(bpy.types.Panel):
    bl_label = "Modifiers Toolbox"
    bl_idname = "MTB_PT_modifiers_toolbox"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "modifier"
    bl_options = {'HIDE_HEADER'}
 
    def draw(self,context):
        layout = self.layout
        row = layout.row(align=True)
        row.scale_y = 1.5
        row.menu(ui_add_modifier_menu.MTB_MT_Add_modifier_menu.bl_idname)
        row.menu(ui_favourite_modifiers.MTB_MT_Favourite_modifiers.bl_idname)
        row.operator(ot_open_preferences.MTB_OT_open_preferences.bl_idname, icon='PREFERENCES', text="")

##############################################
## Register/unregister classes and functions
##############################################
def register():
    bpy.utils.register_class(MTB_PT_Modifiers_toolbox)
        
def unregister():
    bpy.utils.unregister_class(MTB_PT_Modifiers_toolbox)
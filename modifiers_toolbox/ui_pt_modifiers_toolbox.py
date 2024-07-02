import bpy # type: ignore
from . import ui_favourite_modifiers
from . import ui_add_modifier_menu
from . import ot_open_preferences
from bl_ui.properties_data_modifier import DATA_PT_modifiers # type: ignore
original_draw = DATA_PT_modifiers.draw


class MTB_PT_Modifiers_toolbox(bpy.types.Panel):
    bl_label = "Modifiers Toolbox"
    bl_idname = "MTB_PT_modifiers_toolbox"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "modifier"
    bl_options = {'HIDE_HEADER'}
 
    
    @classmethod
    def poll(cls, context):
        if context.object.type in {'MESH', 'CURVE', 'FONT', 'SURFACE', 'LATTICE', 'VOLUME'}:
            return True

    def draw(self,context):
        layout = self.layout
        prefs = bpy.context.preferences.addons[__package__].preferences
        ob_type = context.object.type

        if not prefs.hide_button:
            layout.operator("wm.call_menu", text="Add Modifier", icon='ADD').name = "OBJECT_MT_modifier_add"
        
        row = layout.row()
        box = row.box()
        row = box.row(align=True)
        box.scale_y, box.scale_x = 1.4, 1.2
        # row.operator(ot_open_preferences.MTB_OT_open_preferences.bl_idname, icon='PREFERENCES', emboss=True, text="")
        # row.separator()
        if prefs.hide_button:
            row.operator("wm.call_menu", text="", icon='ADD').name = "OBJECT_MT_modifier_add"
            # row.separator()
        row.menu(ui_add_modifier_menu.MTB_MT_Add_modifier_menu.bl_idname, text="Modifiers", icon='MODIFIER_DATA')
        if ob_type in ob_type in {'MESH'}:
            if prefs.compact_ui:
                row.menu(ui_favourite_modifiers.MTB_MT_Favourite_modifiers.bl_idname,text="", icon='BOOKMARKS')
            else:
                row.separator()
                row.menu(ui_favourite_modifiers.MTB_MT_Favourite_modifiers.bl_idname, text="Favourites", icon='BOOKMARKS')
        # row.separator()
        row.operator(ot_open_preferences.MTB_OT_open_preferences.bl_idname, icon='PREFERENCES', emboss=True, text="")
        
        row = box.row(align=True)
        if prefs.compact_ui:
            box.scale_y, box.scale_x = 1.0, 1.0
        row.operator("modifierstoolbox.apply_all_modifiers", icon='CHECKMARK', text="Apply All", emboss=True)
        if not prefs.compact_ui:
            row.separator()
        row.operator("modifierstoolbox.remove_all_modifiers", icon='X', text="Remove All", emboss=True)
        row.separator()
        if len(context.active_object.modifiers) > 0:
            modifiers = context.active_object.modifiers
            row.operator("modifierstoolbox.display_toggles", icon='RESTRICT_VIEW_OFF', emboss=True, text="", depress = True if modifiers[0].show_viewport == True else False).action = 'SHOW_VIEWPORT'
            row.operator("modifierstoolbox.display_toggles", icon='RESTRICT_RENDER_OFF', emboss=True, text="", depress = True if modifiers[0].show_render == True else False).action = 'SHOW_RENDER'
            row.operator("modifierstoolbox.display_toggles", icon='FULLSCREEN_ENTER', emboss=True, text="", depress = True if modifiers[0].show_expanded == True else False).action = 'SHOW_EXPANDED'
        else:
            row.operator("modifierstoolbox.display_toggles", icon='RESTRICT_VIEW_OFF', emboss=True, text="").action = 'SHOW_VIEWPORT'
            row.operator("modifierstoolbox.display_toggles", icon='RESTRICT_RENDER_OFF', emboss=True, text="").action = 'SHOW_RENDER'
            row.operator("modifierstoolbox.display_toggles", icon='FULLSCREEN_ENTER', emboss=True, text="").action = 'SHOW_EXPANDED'
        # box.separator()

        layout.template_modifiers()

def empty_draw(self, content):
    pass

##############################################
## Register/unregister classes and functions
##############################################
def register():
    bpy.utils.register_class(MTB_PT_Modifiers_toolbox)
    bpy.types.DATA_PT_modifiers.draw = empty_draw
        
def unregister():
    bpy.utils.unregister_class(MTB_PT_Modifiers_toolbox)
    bpy.types.DATA_PT_modifiers.draw = original_draw
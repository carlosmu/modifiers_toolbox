import bpy # type: ignore

##################
# MENU
##################
class MTB_MT_Add_modifier_menu(bpy.types.Menu):
    bl_label = "All Modifiers list"
    bl_idname = "OBJECT_MT_Add_modifier_menu"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        ob_type = context.object.type

        if ob_type in {'MESH', 'CURVE', 'FONT', 'SURFACE', 'LATTICE'}:
            col = row.column()
            col.label(text="Edit")
            col.separator()
            col.menu_contents("OBJECT_MT_modifier_add_edit")

        if ob_type in {'MESH', 'CURVE', 'FONT', 'SURFACE', 'VOLUME'}:
            col = row.column()
            col.label(text="Generate")
            col.separator()
            col.menu_contents("OBJECT_MT_modifier_add_generate")
            col.operator("object.modifier_add", icon="GEOMETRY_NODES", text="Geometry Nodes").type='NODES'
        
        if ob_type in {'MESH', 'CURVE', 'FONT', 'SURFACE', 'LATTICE', 'VOLUME'}:
            col = row.column()
            col.label(text="Deform")
            col.separator()
            col.menu_contents("OBJECT_MT_modifier_add_deform")
        
        if ob_type in {'MESH', 'CURVE', 'FONT', 'SURFACE', 'LATTICE'}:
            col = row.column()
            col.label(text="Physics")
            col.separator()
            col.menu_contents("OBJECT_MT_modifier_add_physics")

##################
# DRAW BUTTON
##################
def draw_item(self, context):
    layout = self.layout
    layout.menu(MTB_MT_Add_modifier_menu.bl_idname)

##################
# REGISTER
##################
def register():
    bpy.utils.register_class(MTB_MT_Add_modifier_menu)
    # bpy.types.DATA_PT_modifiers.append(draw_item)
    # bpy.types.OBJECT_MT_modifier_add.prepend(draw_item)

def unregister():
    bpy.utils.unregister_class(MTB_MT_Add_modifier_menu)
    # bpy.types.DATA_PT_modifiers.remove(draw_item)
    # bpy.types.OBJECT_MT_modifier_add.remove(draw_item)
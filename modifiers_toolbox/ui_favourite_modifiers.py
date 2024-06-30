import bpy # type: ignore

##################
# MENU
##################
class MTB_MT_Favourite_modifiers(bpy.types.Menu):
    bl_label = "Favourite Modifiers"
    bl_idname = "OBJECT_MT_Favourite_modifiers"

    def draw(self, context):
        layout = self.layout
        ob_type = context.object.type
        # {'MESH', 'CURVE', 'FONT', 'SURFACE', 'LATTICE', 'VOLUME'}

        prefs = context.preferences.addons[__package__].preferences
        if prefs.data_transfer:
            layout.operator("object.modifier_add", text="Data Transfer", icon="MOD_DATA_TRANSFER").type='DATA_TRANSFER'
        if prefs.mesh_cache:
            layout.operator("object.modifier_add", text="Mesh Cache", icon="MOD_MESHDEFORM").type='MESH_CACHE'
        if prefs.mesh_sequence_cache:
            layout.operator("object.modifier_add", text="Mesh Sequence Cache", icon="MOD_MESHDEFORM").type='MESH_SEQUENCE_CACHE'
        if prefs.normal_edit:
            layout.operator("object.modifier_add", text="Normal Edit", icon="MOD_NORMALEDIT").type='NORMAL_EDIT'
        if prefs.weighted_normal:
            layout.operator("object.modifier_add", text="Weighted Normal", icon="MOD_NORMALEDIT").type='WEIGHTED_NORMAL'
        if prefs.uv_project:
            layout.operator("object.modifier_add", text="UV Project", icon="MOD_UVPROJECT").type='UV_PROJECT'
        if prefs.uv_warp:
            layout.operator("object.modifier_add", text="UV Warp", icon="MOD_UVPROJECT").type='UV_WARP'
        if prefs.vertex_weight_edit:
            layout.operator("object.modifier_add", text="Vertex Weight Edit", icon="MOD_VERTEX_WEIGHT").type='VERTEX_WEIGHT_EDIT'
        if prefs.vertex_weight_mix:
            layout.operator("object.modifier_add", text="Vertex Weight Mix", icon="MOD_VERTEX_WEIGHT").type='VERTEX_WEIGHT_MIX'
        if prefs.vertex_weight_proximity:
            layout.operator("object.modifier_add", text="Vertex Weight Proximity", icon="MOD_VERTEX_WEIGHT").type='VERTEX_WEIGHT_PROXIMITY'
        ###
        if prefs.array and ob_type in {'MESH', 'CURVE', 'FONT', 'SURFACE'}: # Use this for future versions, to show the favourites in diferent object types
            layout.operator("object.modifier_add", text="Array", icon="MOD_ARRAY").type='ARRAY'
        if prefs.bevel:
            layout.operator("object.modifier_add", text="Bevel", icon="MOD_BEVEL").type='BEVEL'
        if prefs.boolean:
            layout.operator("object.modifier_add", text="Boolean", icon="MOD_BOOLEAN").type='BOOLEAN'
        if prefs.build:
            layout.operator("object.modifier_add", text="Build", icon="MOD_BUILD").type='BUILD'
        if prefs.decimate:
            layout.operator("object.modifier_add", text="Decimate", icon="MOD_DECIM").type='DECIMATE'
        if prefs.edge_split:
            layout.operator("object.modifier_add", text="Edge Split", icon="MOD_EDGESPLIT").type='EDGE_SPLIT'
        if prefs.mask:
            layout.operator("object.modifier_add", text="Mask", icon="MOD_MASK").type='MASK'
        if prefs.mirror:
            layout.operator("object.modifier_add", text="Mirror", icon="MOD_MIRROR").type='MIRROR'
        if prefs.multiresolution:
            layout.operator("object.modifier_add", text="Multiresolution", icon="MOD_MULTIRES").type='MULTIRES'
        if prefs.remesh:
            layout.operator("object.modifier_add", text="Remesh", icon="MOD_REMESH").type='REMESH'
        if prefs.screw:
            layout.operator("object.modifier_add", text="Screw", icon="MOD_SCREW").type='SCREW'
        if prefs.skin:
            layout.operator("object.modifier_add", text="Skin", icon="MOD_SKIN").type='SKIN'
        if prefs.solidify:
            layout.operator("object.modifier_add", text="Solidify", icon="MOD_SOLIDIFY").type='SOLIDIFY'
        if prefs.subdivision_surface:
            layout.operator("object.modifier_add", text="Subdivision Surface", icon="MOD_SUBSURF").type='SUBSURF'
        if prefs.triangulate:
            layout.operator("object.modifier_add", text="Triangulate", icon="MOD_TRIANGULATE").type='TRIANGULATE'
        if prefs.volume_to_mesh:
            layout.operator("object.modifier_add", text="Volume to Mesh", icon="OUTLINER_DATA_VOLUME").type='VOLUME_TO_MESH'
        if prefs.weld:
            layout.operator("object.modifier_add", text="Weld", icon="AUTOMERGE_ON").type='WELD'
        if prefs.wireframe:
            layout.operator("object.modifier_add", text="Wireframe", icon="MOD_WIREFRAME").type='WIREFRAME'
        if prefs.geometry_nodes:
            layout.operator("object.modifier_add", text="Geometry Nodes", icon="GEOMETRY_NODES").type='NODES'
        ###
        if prefs.armature:
            layout.operator("object.modifier_add", text="Armature", icon="MOD_ARMATURE").type='ARMATURE'
        if prefs.cast:
            layout.operator("object.modifier_add", text="Cast", icon="MOD_CAST").type='CAST'
        if prefs.curve:
            layout.operator("object.modifier_add", text="Curve", icon="MOD_CURVE").type='CURVE'
        if prefs.displace:
            layout.operator("object.modifier_add", text="Displace", icon="MOD_DISPLACE").type='DISPLACE'
        if prefs.hook:
            layout.operator("object.modifier_add", text="Hook", icon="HOOK").type='HOOK'
        if prefs.laplacian_deform:
            layout.operator("object.modifier_add", text="Laplacian Deform", icon="MOD_MESHDEFORM").type='LAPLACIANDEFORM'
        if prefs.lattice:
            layout.operator("object.modifier_add", text="Lattice", icon="MOD_LATTICE").type='LATTICE'
        if prefs.mesh_deform:
            layout.operator("object.modifier_add", text="Mesh Deform", icon="MOD_MESHDEFORM").type='MESH_DEFORM'
        if prefs.shrinkwrap:
            layout.operator("object.modifier_add", text="Shrinkwrap", icon="MOD_SHRINKWRAP").type='SHRINKWRAP'
        if prefs.simple_deform:
            layout.operator("object.modifier_add", text="Simple Deform", icon="MOD_SIMPLEDEFORM").type='SIMPLE_DEFORM'
        if prefs.smooth:
            layout.operator("object.modifier_add", text="Smooth", icon="MOD_SMOOTH").type='SMOOTH'
        if prefs.smooth_corrective:
            layout.operator("object.modifier_add", text="Smooth Corrective", icon="MOD_SMOOTH").type='CORRECTIVE_SMOOTH'
        if prefs.smooth_laplacian:
            layout.operator("object.modifier_add", text="Smooth Laplacian", icon="MOD_SMOOTH").type='LAPLACIANSMOOTH'
        if prefs.surface_deform:
            layout.operator("object.modifier_add", text="Surface Deform", icon="MOD_MESHDEFORM").type='SURFACE_DEFORM'
        if prefs.warp:
            layout.operator("object.modifier_add", text="Warp", icon="MOD_WARP").type='WARP'
        if prefs.wave:
            layout.operator("object.modifier_add", text="Wave", icon="MOD_WAVE").type='WAVE'
        ###
        if prefs.cloth:
            layout.operator("object.modifier_add", text="Cloth", icon="MOD_CLOTH").type='CLOTH'
        if prefs.collision:
            layout.operator("object.modifier_add", text="Collision", icon="MOD_PHYSICS").type='COLLISION'
        if prefs.dynamic_paint:
            layout.operator("object.modifier_add", text="Dynamic Paint", icon="MOD_DYNAMICPAINT").type='DYNAMIC_PAINT'
        if prefs.explode:
            layout.operator("object.modifier_add", text="Explode", icon="MOD_EXPLODE").type='EXPLODE'
        if prefs.fluid:
            layout.operator("object.modifier_add", text="Fluid", icon="MOD_FLUIDSIM").type='FLUID'
        if prefs.ocean:
            layout.operator("object.modifier_add", text="Ocean", icon="MOD_OCEAN").type='OCEAN'
        if prefs.particle_instance:
            layout.operator("object.modifier_add", text="Particle Instance", icon="MOD_PARTICLE_INSTANCE").type='PARTICLE_INSTANCE'
        if prefs.particle_system:
            layout.operator("object.modifier_add", text="particle System", icon="MOD_PARTICLES").type='PARTICLE_SYSTEM'
        if prefs.soft_body:
            layout.operator("object.modifier_add", text="Soft Body", icon="MOD_SOFT").type='SOFT_BODY'
        else:
            pass

##################
# DRAW BUTTON
##################
# def draw_item(self, context):
#     layout = self.layout
#     layout.menu(MTB_MT_Favourite_modifiers.bl_idname)

##################
# REGISTER
##################
def register():
    bpy.utils.register_class(MTB_MT_Favourite_modifiers)

def unregister():
    bpy.utils.unregister_class(MTB_MT_Favourite_modifiers)
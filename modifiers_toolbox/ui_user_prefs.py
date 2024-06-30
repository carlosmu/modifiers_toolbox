import bpy # type: ignore

##############################################
#    USER PREFERENCES 
##############################################

class MTB_Preferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    hide_button : bpy.props.BoolProperty(name= "Embed original menu on addon toolbox", default =True) # type: ignore
    ##################
    # Keymap props
    # keymap_letters = [('A', 'A', '', '', 0),
    #                   ('B', 'B', '', '', 1),
    #                   ('C', 'C', '', '', 2),
    #                   ('D', 'D', '', '', 3),
    #                   ('E', 'E', '', '', 4),
    #                   ('F', 'F', '', '', 5),
    #                   ('G', 'G', '', '', 6),
    #                   ('H', 'H', '', '', 7),
    #                   ('I', 'I', '', '', 8),
    #                   ('J', 'J', '', '', 9),
    #                   ('K', 'K', '', '', 10),
    #                   ('L', 'L', '', '', 11),
    #                   ('M', 'M', '', '', 12),
    #                     ]
    # keymap_letter : bpy.props.EnumProperty(name = "Key", items = keymap_letters, default = 'M') # type: ignore
    # keymap_ctrl : bpy.props.BoolProperty(name = "CTRL", default = False) # type: ignore
    # keymap_shift : bpy.props.BoolProperty(name = "SHIFT", default = False) # type: ignore
    # keymap_alt : bpy.props.BoolProperty(name = "ALT", default = True) # type: ignore
    
    # Edit Modifiers
    data_transfer : bpy.props.BoolProperty(name = "DATA_TRANSFER", default = False) # type: ignore
    mesh_cache : bpy.props.BoolProperty(name = "MESH_CACHE", default = False) # type: ignore
    mesh_sequence_cache : bpy.props.BoolProperty(name = "MESH_SEQUENCE_CACHE", default = False) # type: ignore
    normal_edit : bpy.props.BoolProperty(name = "NORMAL_EDIT", default = False) # type: ignore
    weighted_normal : bpy.props.BoolProperty(name = "WEIGHTED_NORMAL", default = False) # type: ignore
    uv_project : bpy.props.BoolProperty(name = "UV_PROJECT", default = False) # type: ignore
    uv_warp : bpy.props.BoolProperty(name = "UV_WARP", default = False) # type: ignore
    vertex_weight_edit : bpy.props.BoolProperty(name = "VERTEX_WEIGHT_EDIT", default = False) # type: ignore
    vertex_weight_mix : bpy.props.BoolProperty(name = "VERTEX_WEIGHT_MIX", default = False) # type: ignore
    vertex_weight_proximity : bpy.props.BoolProperty(name = "VERTEX_WEIGHT_PROXIMITY", default = False) # type: ignore
    
    # Generate Modifiers
    array : bpy.props.BoolProperty(name = "ARRAY", default = True) # type: ignore
    bevel : bpy.props.BoolProperty(name = "BEVEL", default = False) # type: ignore
    boolean : bpy.props.BoolProperty(name = "BOOLEAN", default = True) # type: ignore
    build : bpy.props.BoolProperty(name = "BUILD", default = False) # type: ignore
    decimate : bpy.props.BoolProperty(name = "DECIMATE", default = True) # type: ignore
    edge_split : bpy.props.BoolProperty(name = "EDGE_SPLIT", default = False) # type: ignore
    mask : bpy.props.BoolProperty(name = "MASK", default = False) # type: ignore
    mirror : bpy.props.BoolProperty(name = "MIRROR", default = True) # type: ignore
    multiresolution : bpy.props.BoolProperty(name = "MULTIRES", default = False) # type: ignore
    remesh : bpy.props.BoolProperty(name = "REMESH", default = False) # type: ignore
    screw : bpy.props.BoolProperty(name = "SCREW", default = False) # type: ignore
    skin : bpy.props.BoolProperty(name = "SKIN", default = False) # type: ignore
    solidify : bpy.props.BoolProperty(name = "SOLIDIFY", default = True) # type: ignore
    subdivision_surface : bpy.props.BoolProperty(name = "SUBSURF", default = True) # type: ignore
    triangulate : bpy.props.BoolProperty(name = "TRIANGULATE", default = False) # type: ignore
    volume_to_mesh : bpy.props.BoolProperty(name = "VOLUME_TO_MESH", default = False) # type: ignore
    weld : bpy.props.BoolProperty(name = "WELD", default = False) # type: ignore
    wireframe : bpy.props.BoolProperty(name = "WIREFRAME", default = False) # type: ignore
    geometry_nodes : bpy.props.BoolProperty(name = "NODES", default = True) # type: ignore

    # Deform Modifiers
    armature : bpy.props.BoolProperty(name = "ARMATURE", default = True) # type: ignore
    cast : bpy.props.BoolProperty(name = "CAST", default = False) # type: ignore
    curve : bpy.props.BoolProperty(name = "CURVE", default = False) # type: ignore
    displace : bpy.props.BoolProperty(name = "DISPLACE", default = False) # type: ignore
    hook : bpy.props.BoolProperty(name = "HOOK", default = False) # type: ignore
    laplacian_deform : bpy.props.BoolProperty(name = "LAPLACIANDEFORM", default = False) # type: ignore
    lattice : bpy.props.BoolProperty(name = "LATTICE", default = True) # type: ignore
    mesh_deform : bpy.props.BoolProperty(name = "MESH_DEFORM", default = False) # type: ignore
    shrinkwrap : bpy.props.BoolProperty(name = "SHRINKWRAP", default = True) # type: ignore
    simple_deform : bpy.props.BoolProperty(name = "SIMPLE_DEFORM", default = False) # type: ignore
    smooth : bpy.props.BoolProperty(name = "SMOOTH", default = False) # type: ignore
    smooth_corrective : bpy.props.BoolProperty(name = "CORRECTIVE_SMOOTH", default = False) # type: ignore
    smooth_laplacian : bpy.props.BoolProperty(name = "LAPLACIANSMOOTH", default = False) # type: ignore
    surface_deform : bpy.props.BoolProperty(name = "SURFACE_DEFORM", default = False) # type: ignore
    warp : bpy.props.BoolProperty(name = "WARP", default = False) # type: ignore
    wave : bpy.props.BoolProperty(name = "WAVE", default = False) # type: ignore
    
    # Physics Modifiers
    cloth : bpy.props.BoolProperty(name = "CLOTH", default = False) # type: ignore
    collision : bpy.props.BoolProperty(name = "COLLISION", default = False) # type: ignore
    dynamic_paint : bpy.props.BoolProperty(name = "DYNAMIC_PAINT", default = False) # type: ignore
    explode : bpy.props.BoolProperty(name = "EXPLODE", default = False) # type: ignore
    fluid : bpy.props.BoolProperty(name = "FLUID", default = False) # type: ignore
    ocean : bpy.props.BoolProperty(name = "OCEAN", default = False) # type: ignore
    particle_instance : bpy.props.BoolProperty(name = "PARTICLE_INSTANCE", default = False) # type: ignore
    particle_system : bpy.props.BoolProperty(name = "PARTICLE_SYSTEM", default = False) # type: ignore
    soft_body : bpy.props.BoolProperty(name = "SOFT_BODY", default = False) # type: ignore

    
    ###################
    # UI          
    def draw(self, context):
        layout = self.layout 

        box = layout.box()
        box.label(text="Behaviour:", icon='OPTIONS')
        box.prop(self, "hide_button")
        box.separator()

        # box = layout.box()
        # box.label(text="Shortcut for favourite modifiers menu:", icon='HAND')
        # row = box.row()
        # row.scale_x = 0.3
        # row.prop(self, "keymap_letter")
        # col = row.column()
        # col.prop(self, "keymap_alt", toggle = False)
        # col.prop(self, "keymap_ctrl", toggle = False)
        # col.prop(self, "keymap_shift", toggle = False)
        # box.separator()
        
        box = layout.box()
        box.label(text="Favourite modifiers (for mesh objects only):", icon='BOOKMARKS')
        
        row = box.row()

        col = row.column()
        col.label(text="Edit")
        col.separator()
        col.prop(self, "data_transfer", text="Data Transfer")
        col.prop(self, "mesh_cache", text="Mesh Cache")
        col.prop(self, "mesh_sequence_cache", text="Mesh Sequence Cache")
        col.prop(self, "normal_edit", text="Normal Edit")
        col.prop(self, "weighted_normal", text="Weighted Normal")
        col.prop(self, "uv_project", text="UV Project")
        col.prop(self, "uv_warp", text="UV Warp")
        col.prop(self, "vertex_weight_edit", text="Vertex Weight Edit")
        col.prop(self, "vertex_weight_mix", text="Vertex Weight Mix")
        col.prop(self, "vertex_weight_proximity", text="Vertex Weight Proximity")

        col = row.column()
        col.label(text="Generate")
        col.separator()
        col.prop(self, "array", text="Array")
        col.prop(self, "bevel", text="Bevel")
        col.prop(self, "boolean", text="Boolean")
        col.prop(self, "build", text="Build")
        col.prop(self, "decimate", text="Decimate")
        col.prop(self, "edge_split", text="Edge Split")
        col.prop(self, "mask", text="Mask")
        col.prop(self, "mirror", text="Mirror")
        col.prop(self, "multiresolution", text="Multiresolution")
        col.prop(self, "remesh", text="Remesh")
        col.prop(self, "screw", text="Screw")
        col.prop(self, "skin", text="Skin")
        col.prop(self, "solidify", text="Solidify")
        col.prop(self, "subdivision_surface", text="Subdivision Surface")
        col.prop(self, "triangulate", text="Triangulate")
        col.prop(self, "volume_to_mesh", text="Volume to Mesh")
        col.prop(self, "weld", text="Weld")
        col.prop(self, "wireframe", text="Wireframe")
        col.prop(self, "geometry_nodes", text="Geometry Nodes")

        col = row.column()
        col.label(text="Deform")
        col.separator()
        col.prop(self, "armature", text="Armature")
        col.prop(self, "cast", text="Cast")
        col.prop(self, "curve", text="Curve")
        col.prop(self, "displace", text="Displace")
        col.prop(self, "hook", text="Hook")
        col.prop(self, "laplacian_deform", text="Laplacian Deform")
        col.prop(self, "lattice", text="Lattice")
        col.prop(self, "mesh_deform", text="Mesh Deform")
        col.prop(self, "shrinkwrap", text="Shrinkwrap")
        col.prop(self, "simple_deform", text="Simple Deform")
        col.prop(self, "smooth", text="Smooth")
        col.prop(self, "smooth_corrective", text="Smooth Corrective")
        col.prop(self, "smooth_laplacian", text="Smooth Laplacian")
        col.prop(self, "surface_deform", text="Surface Deform")
        col.prop(self, "warp", text="Warp")
        col.prop(self, "wave", text="Wave")

        col = row.column()
        col.label(text="Physics")
        col.separator()
        col.prop(self, "cloth", text="Cloth")
        col.prop(self, "collision", text="Collision")
        col.prop(self, "dynamic_paint", text="Dynamic Paint")
        col.prop(self, "explode", text="Explode")
        col.prop(self, "fluid", text="Fluid")
        col.prop(self, "ocean", text="Ocean")
        col.prop(self, "particle_instance", text="Particle Instance")
        col.prop(self, "particle_system", text="Particle System")
        col.prop(self, "soft_body", text="Soft Body")

        box.separator()

        layout.separator()

####################################
# REGISTER/UNREGISTER
####################################
def register():
    bpy.utils.register_class(MTB_Preferences) 
        
def unregister():
    bpy.utils.unregister_class(MTB_Preferences)
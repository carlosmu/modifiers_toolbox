import bpy

addon_keymaps = []

def register():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Window', space_type='EMPTY')
        kmi = km.keymap_items.new("wm.call_menu", type = 'M', value = 'PRESS', ctrl= False, alt = True)
        kmi.properties.name = "OBJECT_MT_Favourite_modifiers"
        addon_keymaps.append((km, kmi))  
        
def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
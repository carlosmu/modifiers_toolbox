# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

####################################
# IMPORT MODULES
####################################

# from . import ot_modifiers_toolbox
from . import ui_add_modifier_menu
from . import ui_favourite_modifiers
from . import ui_pt_modifiers_toolbox
from . import ui_user_prefs
from . import ui_keymap
from . import ot_open_preferences
from . import ot_remove_all_modifiers
from . import ot_apply_all_modifiers
from . import ot_display_toggles

bl_info = {
    "name": "Modifiers Toolbox",
    "author": "Carlos Mu <carlos.damian.munoz@gmail.com>",
    "blender": (3, 2, 0),
    "version": (1, 1, 0),
    "category": "Interface",
    "location": "Modifiers Properties",
    "description": "Modifier tools to improve your workflow",
    "warning": "",
    "doc_url": "https://blendermarket.com/products/modifiers-toolbox",
    "tracker_url": "https://blendermarket.com/creators/carlosmu",
}

####################################
# REGISTER/UNREGISTER
####################################
def register():
    ui_add_modifier_menu.register()
    ui_favourite_modifiers.register()
    ui_pt_modifiers_toolbox.register()
    ot_open_preferences.register()
    ot_remove_all_modifiers.register()
    ot_apply_all_modifiers.register()
    ot_display_toggles.register()
    ui_user_prefs.register()
    ui_keymap.register()

def unregister():
    ui_add_modifier_menu.unregister()
    ui_favourite_modifiers.unregister()
    ui_pt_modifiers_toolbox.unregister()
    ot_open_preferences.unregister()
    ot_remove_all_modifiers.unregister()
    ot_apply_all_modifiers.unregister()
    ot_display_toggles.unregister()
    ui_user_prefs.unregister()
    ui_keymap.unregister()
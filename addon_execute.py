# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/Ozbend_Engraving_Internal
#
# Add-on execution script
#
# console command to install (win): "c:/Program Files/blender-2.79b-windows64/blender.exe" -b d:/scene.blend -P d:/addon_execute.py -- -sx 300 -sy 600 -s 0.5 -sa 10 -n NewName -p d:/dest1
# console command to install (nix): blender -b /tmp/scene.blend -P /tmp/addon_execute.py -- -sx 300 -sy 600 -s 0.5 -sa 10 -n NewName -p /tmp/dest1

import bpy

bpy.ops.engravinginternal.start()

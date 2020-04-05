import xbmcaddon
import xbmcgui
import subprocess
import os

ADDON = xbmcaddon.Addon(id='script.module.parsec')
ADDON_ID = ADDON.getAddonInfo('id')
peer_id = ADDON.getSetting("peer_id")
peer_id = 'peer_id=' + peer_id

# Check if parsec is installed
parsec_installed = True
try:
        os.system('parsecd ' + peer_id)
except:
        xbmcgui.Dialog().ok('ERROR', 'Parsec is not installed on this device.\nPlease visit: https://parsecgaming.com/downloads/')
        print('Parsec is not installed on this device.\nPlease visit: https://parsecgaming.com/downloads/')
    
    
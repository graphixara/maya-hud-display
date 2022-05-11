"""
Add Headsup Display to the maya viewport
"""

import maya.cmds as cmds
 
cmds.headsUpDisplay( 'HUDObjectPosition', rem=True )
 
    
def objectPosition(*args):
    """Add Camera object translate Position to HUD """

    try:

        positionValue = cmds.getAttr('renderCam01camera01:steadycam_startPivot_ctrl.ty')
        return positionValue

    except:
        return 0.0

cmds.headsUpDisplay( 'HUDObjectPosition', section=8, block=0, blockSize='medium', label='Camera Height', labelFontSize='large', dfs='large', attachToRefresh=1, command=objectPosition )
 
print('HUD Updated')


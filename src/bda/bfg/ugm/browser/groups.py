from bda.bfg.tile import (
    tile,
    Tile,
)
from bda.bfg.ugm.model.groups import Groups

@tile('leftcolumn', 'templates/left_column.pt', interface=Groups,
      permission='login')
class GroupsLeftColumn(Tile):
    
    add_label = u"Add Group"

@tile('rightcolumn', 'templates/right_column.pt', interface=Groups,
      permission='login')
class GroupsRightColumn(Tile):
    pass
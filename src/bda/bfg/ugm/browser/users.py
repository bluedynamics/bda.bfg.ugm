from bda.bfg.tile import (
    tile,
    Tile,
)
from bda.bfg.ugm.model.users import Users

@tile('leftcolumn', 'templates/left_column.pt', interface=Users,
      permission='login')
class UsersLeftColumn(Tile):
    
    add_label = u"Add User"

@tile('rightcolumn', 'templates/right_column.pt', interface=Users,
      permission='login')
class UsersRightColumn(Tile):
    pass
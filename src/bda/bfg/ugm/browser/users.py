from bda.bfg.tile import tile
from bda.bfg.app.browser.layout import ProtectedContentTile
from bda.bfg.ugm.model.users import Users

@tile('leftcolumn', 'templates/column.pt', interface=Users,
      permission='login', strict=False)
class UsersLeftColumn(ProtectedContentTile):
    pass

@tile('rightcolumn', 'templates/column.pt', interface=Users,
      permission='login', strict=False)
class UsersRightColumn(ProtectedContentTile):
    pass
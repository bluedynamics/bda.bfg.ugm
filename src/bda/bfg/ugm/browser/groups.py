from bda.bfg.tile import tile
from bda.bfg.app.browser.layout import ProtectedContentTile
from bda.bfg.ugm.model.groups import Groups

@tile('leftcolumn', 'templates/column.pt', interface=Groups,
      permission='login', strict=False)
class GroupsLeftColumn(ProtectedContentTile):
    pass

@tile('rightcolumn', 'templates/column.pt', interface=Groups,
      permission='login', strict=False)
class GroupsRightColumn(ProtectedContentTile):
    pass
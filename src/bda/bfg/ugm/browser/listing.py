from bda.bfg.tile import (
    tile,
    Tile,
)
from bda.bfg.ugm.model.users import Users
from bda.bfg.ugm.model.groups import Groups

class ColumnListing(Tile):
    pass

@tile('columnlisting', 'templates/column_listing.pt',
      interface=Users, permission='login')
class UserColumnListing(ColumnListing):
    pass

@tile('columnlisting', 'templates/column_listing.pt',
      interface=Groups, permission='login')
class GroupsColumnListing(ColumnListing):
    pass
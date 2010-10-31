from bda.bfg.tile import (
    tile,
    Tile,
)
from bda.bfg.ugm.model.users import Users
from bda.bfg.ugm.model.groups import Groups

class ColumnListing(Tile):
    
    @property
    def items(self):
        # XXX: nothing senceful yet, dummy code for CSS
        ret = list()
        for i in range(1000):
            ret.append({
                'left': 'item %i' % i,
                'right': 'whatever %i' % i,
            })
        return ret

@tile('columnlisting', 'templates/column_listing.pt',
      interface=Users, permission='login')
class UserColumnListing(ColumnListing):
    pass

@tile('columnlisting', 'templates/column_listing.pt',
      interface=Groups, permission='login')
class GroupsColumnListing(ColumnListing):
    pass
from bda.bfg.tile import (
    tile,
    Tile,
    registerTile,
    render_tile,
)
from bda.bfg.app.browser.layout import ProtectedContentTile
from bda.bfg.ugm.model.root import Ugm
from bda.bfg.ugm.model.users import Users
from bda.bfg.ugm.model.groups import Groups

###############################################################################
# Content tiles for Root, Users and Groups, rendering left and right column
###############################################################################

registerTile('content',
             'bda.bfg.ugm:browser/templates/columns.pt',
             interface=Ugm,
             class_=ProtectedContentTile,
             permission='login')

registerTile('content',
             'bda.bfg.ugm:browser/templates/columns.pt',
             interface=Users,
             class_=ProtectedContentTile,
             permission='login',
             strict=False)

registerTile('content',
             'bda.bfg.ugm:browser/templates/columns.pt',
             interface=Groups,
             class_=ProtectedContentTile,
             permission='login',)

###############################################################################
# Columns for Root. They proxy columns for Users as default.
###############################################################################

class RootColumn(Tile):
    
    def _render(self, name):
        return render_tile(self.model['users'], self.request, name)

@tile('leftcolumn', interface=Ugm, permission='login')
class RootLeftColumn(RootColumn):
    
    def render(self):
        return self._render('leftcolumn')

@tile('rightcolumn', interface=Ugm, permission='login')
class RootRightColumn(RootColumn):
    
    def render(self):
        return self._render('rightcolumn')
from bda.bfg.tile import (
    tile,
    registerTile,
    render_tile,
)
from bda.bfg.app.browser.layout import ProtectedContentTile
from bda.bfg.ugm.model.root import Root
from bda.bfg.ugm.model.users import Users
from bda.bfg.ugm.model.groups import Groups

###############################################################################
# Content tiles for Root, Users and Groups, rendering left and right column
###############################################################################

registerTile('content',
             'bda.bfg.ugm:browser/templates/columns.pt',
             interface=Root,
             class_=ProtectedContentTile,
             permission='login',
             strict=False)

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
             permission='login',
             strict=False)

###############################################################################
# Columns for Root. They proxy columns for Users as default.
###############################################################################

class RootColumn(ProtectedContentTile):
    
    def _render(self, name):
        return render_tile(self.model['users'], self.request, name)

@tile('leftcolumn', interface=Root, permission='login', strict=False)
class RootLeftColumn(RootColumn):
    
    def render(self):
        return self._render('leftcolumn')

@tile('rightcolumn', interface=Root, permission='login', strict=False)
class RootRightColumn(RootColumn):
    
    def render(self):
        return self._render('rightcolumn')
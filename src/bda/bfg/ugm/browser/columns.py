from bda.bfg.tile import (
    tile,
    Tile,
    registerTile,
    render_tile,
)
from bda.bfg.app.browser.layout import ProtectedContentTile

registerTile('content',
             'bda.bfg.ugm:browser/templates/columns.pt',
             class_=ProtectedContentTile,
             permission='login',
             strict=False)

class Column(Tile):
    """Abstract column.
    """
    
    def _render(self, model, name):
        return render_tile(model, self.request, name)
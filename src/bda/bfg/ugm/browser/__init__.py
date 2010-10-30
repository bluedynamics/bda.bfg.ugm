from repoze.bfg.view import static
from bda.bfg.tile import registerTile
from bda.bfg.app.browser.layout import ProtectedContentTile
from bda.bfg.ugm.model.root import Root

from bda.bfg.app import browser
browser.MAIN_TEMPLATE = 'bda.bfg.ugm.browser:templates/main.pt'
browser.ADDITIONAL_CSS.append('bda.bfg.ugm.static/styles.css')

static_view = static('static')

registerTile('content',
             'bda.bfg.ugm:browser/templates/root.pt',
             interface=Root,
             class_=ProtectedContentTile,
             permission='login',
             strict=False)
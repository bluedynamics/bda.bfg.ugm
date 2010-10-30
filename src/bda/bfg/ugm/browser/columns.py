from bda.bfg.tile import registerTile
from bda.bfg.app.browser.layout import ProtectedContentTile
from bda.bfg.ugm.model.root import Root
from bda.bfg.ugm.model.users import Users
from bda.bfg.ugm.model.groups import Groups

###############################################################################
# content tiles for Users and Groups, rendering left and right column
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
# left and right columns for root. they proxy columns for users
###############################################################################

# XXX: Class style tiles

registerTile('leftcolumn',
             'bda.bfg.ugm:browser/templates/column.pt',
             interface=Root,
             class_=ProtectedContentTile,
             permission='login',
             strict=False)

registerTile('rightcolumn',
             'bda.bfg.ugm:browser/templates/column.pt',
             interface=Root,
             class_=ProtectedContentTile,
             permission='login',
             strict=False)

###############################################################################
# left and right columns for users
###############################################################################

# XXX: Class style tiles

registerTile('leftcolumn',
             'bda.bfg.ugm:browser/templates/column.pt',
             interface=Users,
             class_=ProtectedContentTile,
             permission='login',
             strict=False)

registerTile('rightcolumn',
             'bda.bfg.ugm:browser/templates/column.pt',
             interface=Users,
             class_=ProtectedContentTile,
             permission='login',
             strict=False)

###############################################################################
# left and right columns for groups
###############################################################################

# XXX: Class style tiles

registerTile('leftcolumn',
             'bda.bfg.ugm:browser/templates/column.pt',
             interface=Groups,
             class_=ProtectedContentTile,
             permission='login',
             strict=False)

registerTile('rightcolumn',
             'bda.bfg.ugm:browser/templates/column.pt',
             interface=Groups,
             class_=ProtectedContentTile,
             permission='login',
             strict=False)
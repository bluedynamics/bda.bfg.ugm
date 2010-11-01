from bda.bfg.tile import Tile

class ColumnListing(Tile):
    """Abstract column listing.
    """
    
    @property
    def items(self):
        """Return list of dicts like:
        
        {
            'target': u'http://example.com/foo',
            'left': u'Left column content',
            'right': u'middle column content',
            'actions': [
                {
                    'XXX': 'XXX',
                }
            ],
        }
        """
        raise NotImplementedError(u"Abstract ``ColumnListing`` does not "
                                  u"implement ``items`` property")
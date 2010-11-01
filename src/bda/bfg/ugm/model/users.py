from bda.bfg.app.model import (
    BaseNode,
    Properties,
    BaseMetadata,
)
from bda.bfg.ugm.model.user import User

class Users(BaseNode):
    """Users Node.
    """
    
    @property
    def metadata(self):
        metadata = BaseMetadata()
        metadata.title = "Users"
        metadata.description = "Container for Users"
        return metadata
    
    def __iter__(self):
        yield 'foo'
    
    iterkeys = __iter__
    
    def __getitem__(self, name):
        try:
            return BaseNode.__getitem__(self, name)
        except KeyError:
            if not name in self.iterkeys():
                raise KeyError(name)
            # XXX: User(ldapNode, name, self)
            user = User(BaseNode(), name, self)
            self[name] = user
            return user
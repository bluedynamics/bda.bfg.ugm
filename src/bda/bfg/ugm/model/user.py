from zope.interface import implements
from repoze.bfg.security import (
    Everyone,
    Allow,
    Deny,
    ALL_PERMISSIONS,
)
from bda.bfg.app.model import (
    AdapterNode,
    Properties,
    BaseMetadata,
)
from bda.bfg.ugm.model.interfaces import IUser

class User(AdapterNode):
    
    implements(IUser)
    
    __acl__ = [
        (Allow, 'group:authenticated', 'view'),
        (Allow, 'group:authenticated', 'edit'),
        (Allow, Everyone, 'login'),
        (Deny, Everyone, ALL_PERMISSIONS),
    ]
    
    @property
    def properties(self):
        props = Properties()
        props.editable = True
        return props
    
    @property
    def metadata(self):
        metadata = BaseMetadata()
        metadata.title = "User"
        metadata.description = "User"
        return metadata
    
    def __call__(self):
        self.model()
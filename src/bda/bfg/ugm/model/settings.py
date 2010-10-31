import os
from repoze.bfg.security import (
    Everyone,
    Allow,
    Deny,
    ALL_PERMISSIONS,
)
from bda.bfg.app.model import (
    BaseNode,
    Properties,
    ConfigProperties,
    BaseMetadata,
)
from bda.bfg.ugm.model.utils import APP_PATH

class Settings(BaseNode):
    __acl__ = [
        (Allow, 'group:manager', 'view'),
        (Allow, Everyone, 'login'),
        (Deny, Everyone, ALL_PERMISSIONS),
    ]
    
    def __init__(self, name=None):
        BaseNode.__init__(self, name)
        path = os.path.join(APP_PATH, 'etc', 'ldap.cfg')
        self._config = ConfigProperties(path)
    
    def __call__(self):
        self.attrs()
    
    @property
    def attrs(self):
        return self._config
    
    @property
    def metadata(self):
        metadata = BaseMetadata()
        metadata.title = "LDAP Settings"
        metadata.description = "LDAP Connection Settings"
        return metadata
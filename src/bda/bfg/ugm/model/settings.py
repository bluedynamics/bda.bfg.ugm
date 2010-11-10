import os
from zope.interface import implements
from bda.ldap import LDAPProps
from bda.ldap.base import testLDAPConnectivity
from bda.ldap.users import LDAPUsersConfig
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
from bda.bfg.ugm.model.interfaces import ISettings
from bda.bfg.ugm.model.utils import APP_PATH

class Settings(BaseNode):
    
    implements(ISettings)
    
    __acl__ = [
        (Allow, 'group:manager', 'view'),  
        (Allow, 'group:manager', 'edit'),
        (Allow, Everyone, 'login'),
        (Deny, Everyone, ALL_PERMISSIONS),
    ]
    
    def __init__(self, name=None, _app_path=None):
        """``_app_path`` defines an alternative path for app root and is
        for testing purposes only
        """
        BaseNode.__init__(self, name)
        path = os.path.join(_app_path or APP_PATH, 'etc', 'ldap.cfg')
        self._config = ConfigProperties(path)
        self.invalidate()
    
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
    
    def invalidate(self):
        self._ldap_props = None
        self._ldap_ucfg = None
    
    @property
    def ldap_connectivity(self):
        config = self._config
        return testLDAPConnectivity(config.server, int(config.port))
    
    @property
    def ldap_props(self):
        if self._ldap_props is None:
            config = self._config
            self._ldap_props = LDAPProps(server=config.server,
                                         port=int(config.port),
                                         user=config.user,
                                         password=config.password)
        return self._ldap_props

    @property
    def ldap_ucfg(self):
        if self._ldap_ucfg is None:
            config = self._config
            # XXX: extend settings: uri, attrmap, scope, queryfilter
            self._ldap_ucfg = LDAPUsersConfig(baseDN=config.users_dn,
                                              attrmap={
                                                  'id': 'uid',
                                                  'login': 'uid',
                                                  'cn': 'cn',
                                                  'sn': 'sn',
                                                  'mail': 'mail',
                                              })
        return self._ldap_ucfg
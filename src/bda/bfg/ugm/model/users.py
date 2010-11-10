from zope.interface import implements
from bda.bfg.app.model import (
    BaseNode,
    Properties,
    BaseMetadata,
)
from bda.ldap import LDAPProps
from bda.ldap.users import LDAPUsers
from bda.ldap.users import LDAPUsersConfig
from bda.bfg.ugm.model.interfaces import IUsers
from bda.bfg.ugm.model.user import User

class Users(BaseNode):
    
    implements(IUsers)
    
    def __init__(self, props=None, ucfg=None):
        super(Users, self).__init__()
        self._ldap_props = props
        self._ldap_ucfg = ucfg
        self._ldap_users = None

    @property
    def metadata(self):
        metadata = BaseMetadata()
        metadata.title = "Users"
        metadata.description = "Container for Users"
        return metadata

    @property
    def ldap_props(self):
        if self._ldap_props is None:
            config = self.__parent__['settings']._config
            self._ldap_props = LDAPProps(server=config.server,
                                         port=int(config.port),
                                         user=config.user,
                                         password=config.password)
        return self._ldap_props

    @property
    def ldap_ucfg(self):
        if self._ldap_ucfg is None:
            config = self.__parent__['settings']._config
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
    
    @property
    def ldap_users(self):
        if self._ldap_users is None:
            self._ldap_users = LDAPUsers(self.ldap_props, self.ldap_ucfg)
        return self._ldap_users

    def invalidate(self):
        self._ldap_props = None
        self._ldap_ucfg = None
        self._ldap_users = None

    def __iter__(self):
        return self.ldap_users.__iter__()
    
    iterkeys = __iter__
    
    def __getitem__(self, name):
        try:
            return BaseNode.__getitem__(self, name)
        except KeyError:
            if not name in self.iterkeys():
                raise KeyError(name)
            user = User(self.ldap_users[name], name, self)
            self[name] = user
            return user

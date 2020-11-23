import ldap
import logging
from openerp import tools
from openerp.osv import osv
from openerp import SUPERUSER_ID
from ldap.filter import filter_format


_logger = logging.getLogger(__name__)


class CompanyLDAP(osv.osv):
    _inherit = "res.company.ldap"

    def connect(self, conf):
        """
        Connect to an LDAP server specified by an ldap
        configuration dictionary.
        :param dict conf: LDAP configuration
        :return: an LDAP object
        """
        prefix = (
            ""
            if conf["ldap_server"].startswith("ldap://")
            or conf["ldap_server"].startswith("ldaps://")
            else "ldap://"
        )
        uri = "%s%s:%d" % (prefix, conf["ldap_server"], conf["ldap_server_port"])

        connection = ldap.initialize(uri)
        if conf["ldap_tls"]:
            connection.start_tls_s()
        return connection

    def authenticate(self, conf, login, password):
        """
        Authenticate a user against the specified LDAP server.
        In order to prevent an unintended 'unauthenticated authentication',
        which is an anonymous bind with a valid dn and a blank password,
        check for empty passwords explicitely (:rfc:`4513#section-6.3.1`)

        :param dict conf: LDAP configuration
        :param login: username
        :param password: Password for the LDAP user
        :return: LDAP entry of authenticated user or False
        :rtype: dictionary of attributes
        """

        if not password:
            return False

        entry = False
        filter = filter_format(
            conf["ldap_filter"],
            [login] * conf["ldap_filter"].count("%s"),
        )
        try:
            results = self.query(conf, filter.encode("utf-8"))

            # Get rid of (None, attrs) for searchResultReference replies
            results = [i for i in results if i[0]]
            if results and len(results) == 1:
                dn = results[0][0]
                conn = self.connect(conf)
                conn.simple_bind_s(dn, password.encode("utf-8"))
                conn.unbind()
                entry = results[0]
        except ldap.INVALID_CREDENTIALS:
            return False
        except ldap.LDAPError as e:
            _logger.error("An LDAP exception occurred: %s", e)
        return entry

    def get_or_create_user(self, cr, uid, conf, login, ldap_entry, context=None):
        """
        Retrieve an active resource of model res_users with the specified
        login. Create the user if it is not initially found.
        :param dict conf: LDAP configuration
        :param login: the user's login
        :param tuple ldap_entry: single LDAP result (dn, attrs)
        :return: res_users id
        :rtype: int
        """

        user_id = False
        login = tools.ustr(login.lower().strip())
        cr.execute("SELECT u.id, u.active FROM res_users u JOIN res_partner p ON u.partner_id = p.id WHERE lower(u.login)=%s OR lower(p.email)=%s", (login, login))
        res = cr.fetchone()
        if res:
            if res[1]:
                user_id = res[0]
        elif conf["create_user"]:
            _logger.debug('Creating new Odoo user "%s" from LDAP' % login)
            user_obj = self.pool["res.users"]
            values = self.map_ldap_attributes(cr, uid, conf, login, ldap_entry)
            if conf["user"]:
                values["active"] = True
                user_id = user_obj.copy(cr, SUPERUSER_ID, conf["user"], default=values)
            else:
                user_id = user_obj.create(cr, SUPERUSER_ID, values)
        return user_id

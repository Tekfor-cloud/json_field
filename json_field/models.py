from odoo import models, api
from odoo.tools import Query
from . import expression


class JsonModels(models.AbstractModel):
    """Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class user(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).
    """

    _auto = True  # automatically create database backend
    _register = False  # not visible in ORM registry, meant to be
    # python-inherited only
    _abstract = False  # not abstract
    _transient = False  # not transient

    @api.model
    def _where_calc(self, domain, active_test=True):
        """Computes the WHERE clause needed to implement an OpenERP domain.
        :param domain: the domain to compute
        :type domain: list
        :param active_test: whether the default filtering of records with ``active``
                            field set to ``False`` should be applied.
        :return: the query expressing the given domain as provided in domain
        :rtype: osv.query.Query
        """
        # if the object has an active field ('active', 'x_active'), filter out all
        # inactive records unless they were explicitely asked for
        if (
            self._active_name
            and active_test
            and self._context.get("active_test", True)
        ):
            # the item[0] trick below works for domain items and '&'/'|'/'!'
            # operators too
            if not any(item[0] == self._active_name for item in domain):
                domain = [(self._active_name, "=", 1)] + domain

        if domain:
            return expression.JsonExpression(domain, self).query
        else:
            return Query(self.env.cr, self._table, self._table_query)

class MssqlRouter:

    route_app_labels = {'mssql',}

    def db_for_read(self, model, **hints):
        return 'mssql'

    def db_for_write(self, model, **hints):
        return 'mssql'

    def allow_relation(self, obj1, obj2, **hints):
        if (
        obj1._meta.app_label in self.route_app_labels or
        obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return True
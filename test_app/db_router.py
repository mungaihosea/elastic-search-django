
class NonRelRouter:
    """
    route non-relational models to mongodb
    """
    def __init__(self):
        self.non_rel_databases = ["Company", "Category", "SearchModel", "BlogPost"]


    def db_for_read(self, model, **hints):
        if model.__name__ in self.non_rel_databases:
            print(model.__name__)
            return 'nonrel'
        return 'default'

    def db_for_write(self, model, **hints):
        if model.__name__ in self.non_rel_databases:
            print(model.__name__)
            return 'nonrel'
        return 'default'

    def allow_migration(self, db, app_label, model_name=None, **hints):
        if model.__name__ in self.non_rel_databases:
            return False
        # if db == 'nonrel':
        #     return False
        return True

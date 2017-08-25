from .q import TemplateQuery


class PeopleReadQuery(TemplateQuery):

    def get_query_string(self):
        return 'SELECT * FROM PEOPLE'


class CompanyReadQuery(TemplateQuery):

    def get_query_string(self):
        return 'SELECT * FROM COMPANY'

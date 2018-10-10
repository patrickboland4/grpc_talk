import pdb

from arango import ArangoClient


class ArangoHelper():
    
    def __init__(self):
        #
        # initialize arango client
        #
        self.client = ArangoClient(protocol='http', host='localhost', port=8529)
        sys_db = self.client.db('_system', username='root',)
        
        #
        # create db if does not exist
        # 

        if not sys_db.has_database('users'):
            sys_db.create_database('users')

        self.db = self.client.db('users', username='root', password='passwd')

        #
        # create collection if does not exist
        #

        if not self.db.has_collection('user_profiles'):
            self.db.create_collection('user_profiles')

        self.collection = self.db.collection('user_profiles')


    def create_user_profile(self, property_dict):
        first = property_dict.get('first')
        last = property_dict.get('last')
        term = property_dict.get('term')

        first_last_term = "{}{}{}".format(first, last, term)

        property_dict["_key"] = first_last_term

        try:
            self.db.insert_document('user_profiles', property_dict)
            return "OK"
        except:
            return "Failed"


    def get_user_profile(self, key):
        return self.collection.get(key)
        

    def get_all_profiles(self):
        # Execute an AQL query and iterate through the result cursor.
        cursor = self.db.aql.execute('FOR doc IN user_profiles RETURN doc')
        names = [document for document in cursor]
        return names



def run():
    
    # Add a hash index to the collection.
    #students.add_hash_index(fields=['name'], unique=True)

    helper = ArangoHelper()

    helper.create_user_profile({'first': 'jane', 
        'last': 'doe', 'term': 'Fall2018', 
        'profile': 'I love python'})
    helper.create_user_profile({'first': 'john', 
        'last': 'smith', 'term': 'Fall2018',
        'profile': 'python is the greatest'})
    
    print(helper.get_user_profile('janedoeFall2018'))
    print(helper.get_user_profile('johnsmithFall2018'))

    print(helper.get_all_profiles())



if __name__ == '__main__':
    run()

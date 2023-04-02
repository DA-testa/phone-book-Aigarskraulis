class Contact:
    def __init__(self, number, name):
        self.number = number
        self.name = name

class Query:
    def __init__(self, query):
        self.type, self.number, *self.name = query

    def execute(self, contacts):
        if self.type == 'add':
            contacts[self.number] = Contact(self.number, ''.join(self.name))
        elif self.type == 'del':
            contacts.pop(self.number, None)
        else: # self.type == 'find'
            contact = contacts.get(self.number, None)
            return contact.name if contact is not None else 'not found'

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep dictionary of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    for query in queries:
        response = query.execute(contacts)
        if response is not None:
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

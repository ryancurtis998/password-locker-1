class user:
    '''
    class will contain all user authentication details
    '''
    def _init_(self, name, password):
        '''
        this will create a new authentication for each instance of a user
        '''

        self.name = name
        self.password = password

class BookManagerException(Exception):
    pass

class ValidationException(BookManagerException):
    def __init__(self, msgs):
        """
        #:param msgs: lista de mesaje de eroare
        #:type msgs: msgs
        """
        self.__err_msgs = msgs

    def getMessages(self):
        return self.__err_msgs

    def __str__(self):
        return 'Validation Exception: ' + str(self.__err_msgs)

class RepositoryException(BookManagerException):
    def __init__(self, msg):
        self.__msg = msg

    def getMessage(self):
        return self.__msg

    def __str__(self):
        return 'Repository Exception: ' + str(self.__msg)

class DuplicateIDException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "ID duplicat.")

class Inchiriere_ReturnareAlreadyAssignedException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Inchiriere_Returnare existent deja pentru carte si client dat.")

class BookNotFoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self,"Cartea nu a fost gasita.")

class Inchiriere_ReturnareNotFoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Inchiriere_Returnare nu a fost gasita.")

class ClientNotFoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Clientul nu a fost gasit.")

class NotEnoughInchiriere_ReturnaresException(BookManagerException):
    def __init__(self):
        pass

class CorruptedFileException(BookManagerException):
    def __init__(self):
        pass






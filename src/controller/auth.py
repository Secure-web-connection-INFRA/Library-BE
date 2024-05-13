from abc import ABC, abstractmethod

class AuthService(ABC):

    @abstractmethod
    def validateAuth(self):
        """Abstract method to validate authentication."""
        pass

    @abstractmethod    
    def login(self):
        """Abstract method to handle login."""
        pass

    @abstractmethod
    def signUp(self):
        """Abstract method to handle sign up."""
        pass

    @abstractmethod
    def resetPassword(self):
        """Abstract method to handle password reset."""
        pass

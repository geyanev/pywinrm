import re


class WinRMWebServiceError(Exception):
    """Generic WinRM SOAP Error"""
    pass


class WinRMAuthorizationError(Exception):
    """Authorization Error"""
    pass


class WinRMWSManFault(Exception):
    """A Fault returned in the SOAP response. The XML node is a WSManFault"""
    pass


class WinRMTransportError(Exception):
    """"Transport-level error"""
    code = 500

    def __init__(self, transport, message, full_message=None):
        self.transport = transport
        self.message = message
	self.full_message = full_message

    def __str__(self):
        return '{0} {1}. {2} {3}'.format(self.code, re.sub(
            'Error$', '', self.__class__.__name__), self.message, self.full_message)

    def __repr__(self):
        return "{0}(code={1}, transport='{2}', message='{3}', full_message='{4}')".format(
            self.__class__.__name__, self.code, self.transport, self.message, self.full_message)


class UnauthorizedError(WinRMTransportError):
    """Raise if the user is not authorized"""
    code = 401


class TimeoutError(WinRMTransportError):
    pass

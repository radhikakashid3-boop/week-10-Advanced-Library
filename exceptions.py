
class LibraryError(Exception):
    """Base exception for the library."""


class ValidationError(LibraryError):
    """Raised when validation fails."""


class SerializationError(LibraryError):
    """Raised when serialization fails."""


class ConfigurationError(LibraryError):
    """Raised when configuration is invalid."""

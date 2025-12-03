import importlib.metadata

__title__: str = "abpi-python"
__version__: str = "0.1.0"
__openapi_doc_version__: str = "0.1.0"
__gen_version__: str = "0.1.0"
__user_agent__: str = ""

try:
    if __package__ is not None:
        __version__ = importlib.metadata.version(__package__)
except importlib.metadata.PackageNotFoundError:
    pass

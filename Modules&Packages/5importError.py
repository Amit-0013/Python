##Write code that attempts to import a non-existent module and gracefully handles the import error by printing an error message.

try:
    import any 
except ImportError as e:
    print("Module does not exist ",e)
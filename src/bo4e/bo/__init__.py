# src/bo4e/bo/__init__.py
import importlib
import pkgutil

# Iterate through all the modules in the current package
package = __name__
for _, modname, _ in pkgutil.iter_modules(__path__, package + "."):
    # Import the module
    module = importlib.import_module(modname)
    # Iterate through the attributes of the module
    for attribute_name in dir(module):
        # Get the attribute
        attribute = getattr(module, attribute_name)
        # Check if the attribute is a class and it's defined in this module (not imported)
        if isinstance(attribute, type) and attribute.__module__ == module.__name__:
            # Add the class to the namespace of this module
            globals()[attribute_name] = attribute

# Now you can directly import any class from the bo package
# from bo4e.bo import Vertrag, Ansprechpartner, etc.

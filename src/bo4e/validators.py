"""
Contains validators for BO s and COM s classes.
"""

# pylint: disable=unused-argument
def check_list_length_at_least_one(instance, attribute, value):
    """
    Check that minimal list length is at least one.
    """
    if len(value) < 1:
        raise ValueError(f"List {attribute.name} must not be empty.")

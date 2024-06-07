============
Fundamentals
============

The BO4E data model is constructed around three main parts: Business Objects, Components, and Enumerations.

**Business Objects** and **Components** are the primary building blocks of the data model.
They inherit from a main Business Object and a main Component respectively.
These main objects contain meta data fields such as `_id`, `_typ`, and `_version` that are common to all Business Objects and Components.

**Enumerations** are used to represent a set of named values in the data model, providing a way to enforce specific values for a field.

This structure allows for a high degree of flexibility and extensibility, enabling the data model to adapt to the evolving needs of the German energy market.

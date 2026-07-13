======================
Technical restrictions
======================

There are some technical restrictions throughout the BO4E data models which are important if you want to use it.
There are several reasons for these but mostly due to compatibility reasons as we want to design the data model
such that it can be implemented in most programming languages.

* The data model is generally not object oriented. The reference implementation (BO4E-Python) uses inheritance
  to save some code but the generated JSON schemas do not contain any information about inheritance as it is not
  supported by the official JSON schema structure. As a result, the following constraints apply:

  * You can only differentiate BOs and COMs by using the enums `BoTyp` and `ComTyp`. They are not directly
    referenced from the data model but are rolled out to support developers if they need to differentiate the
    types.
  * There will be some redundancy in terms of field definitions.

* In general, BOs won't be referenced by COMs but it's not prohibited. In fact, there are some cases in which a COM
  references a BO. Keep that in mind when designing a package structure e.g. to prevent circular import errors.
* There are no circular references **except for** self references. A model can reference itself in the same class.
  This means, when drawing a reference graph of BO4E there will be no loops except for "tiny" loops corresponding
  to self references. E.g. `BO Rechnung` can have a field `teilrechnungen` of type `list[BO Rechnung]`.
  But it cannot reference another model which references back to `BO Rechnung`.

  * As a result, we cannot directly support `n x m`-relationships as they would require a back-reference.
    If you're designing a database structure you have to manually add these relationship tables where needed.

* We won't use a `Union`-type which is represented in JSON schemas as `anyOf` except for a nullable type. I.e.
  the type can never be a union of two or more types which are not `null`.

================================
BO4E Data Model Release Workflow
================================

Welcome to the BO4E Data Model release process!
This guide provides a straightforward explanation of how we release new versions of our data model, making it easier for you to integrate and use them in your preferred programming language.

Step-by-Step Guide
==================

1. Python Package Implementation
--------------------------------
   * **Starting Point:** The journey begins with the implementation of the `BO4E data model as a Python package <https://github.com/bo4e/BO4E-python/>`_.

2. Release and Schema Generation
--------------------------------
   * **Automatic Generation:** Upon releasing a new version of this Python package, a GitHub action automatically triggers.
   * **JSON Schemas Creation:** This action generates JSON schemas, which are essential blueprints of the data model.
   * **Storage:** These schemas are then stored in a dedicated repository, known as the `BO4E-Schemas Repository <https://github.com/bo4e/BO4E-Schemas>`_.

3. Optional Customization (BO4E-Schema-Tool)
--------------------------------------------
   * **Flexibility in Data Fields:** Initially, the JSON schemas contain only optional fields.
   * **Setting Required Fields:** If you need to designate certain fields as mandatory, you can use the `BO4E-Schema-Tool Repository <https://github.com/bo4e/BO4E-Schema-Tool>`_.
   * **Tool Functionality:** This repository houses a command-line interface (CLI) tool that assists in updating the JSON schema files to define required fields.

4. Code Generation (BO4E-Python-Generator)
------------------------------------------
   * **Finalizing JSON Schemas:** Once you have the final version of the JSON schema files, it's time to generate code.
   * **Pydantic Classes Creation:** Utilize tools like the `BO4E-Python-Generator <https://github.com/bo4e/BO4E-Python-Generator>`_, another CLI tool, to create Pydantic classes from the JSON schemas.

5. Ready to Use
---------------
   * **Integration:** With these steps complete, the BO4E data model is now ready for use in your favorite programming language.
   * **Seamless Application:** Implement the data model seamlessly in your projects and enjoy the efficiency it brings to your workflow.

.. note::
   This workflow ensures that the BO4E data model remains flexible, adaptable, and easy to integrate into various programming environments.

Visualization of the release workflow
=====================================

.. image:: /_static/bo4e-release-workflow.png

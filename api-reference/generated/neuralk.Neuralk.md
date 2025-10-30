# Neuralk

### *class* Neuralk(user_id, password, timeout=15)

Main class for interacting with the Neuralk AI platform.

This class serves as the primary interface for the Neuralk SDK, providing access to
various services through specialized handlers. It manages authentication and provides
access to analysis, project, and user management functionality.

* **Variables:**
  * **analysis** (*AnalysisHandler*) – Handler for analysis operations
  * **projects** (*ProjectHandler*) – Handler for project management operations
  * **users** (*UserHandler*) – Handler for user management operations
  * **project_files** (*ProjectFileHandler*) – Handler for project file management operations
  * **organization** (*OrganizationHandler*) – Handler for organization management operations
* **Parameters:**
  * **user_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The user ID for authentication
  * **password** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The password for authentication
  * **timeout** ([*int*](https://docs.python.org/3/library/functions.html#int) *,* *optional*) – Request timeout in seconds. Defaults to 15 s.

<!-- !! processed by numpydoc !! -->

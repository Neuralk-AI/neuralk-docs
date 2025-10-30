# Neuralk.projects.add_user

#### Neuralk.projects.add_user(project, user_email, role='member')

Add a user to a project by project ID with a specific role.

* **Parameters:**
  * **project** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|**Project*) – The project to add the user to or its ID .
  * **user_email** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The email of the user to add
  * **role** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The role to assign to the user. Default is “member”.
  * **roles** (*Available*)
  * **"owner"** ( *-*)
  * **"contributor"** ( *-*)
  * **"member"** ( *-*)
* **Raises:**
  **NeuralkException** – If adding the user fails
* **Return type:**
  None

<!-- !! processed by numpydoc !! -->

# Neuralk.projects.get_active_analyses

#### Neuralk.projects.get_active_analyses(project)

Retrieve the list of pending or in progress analyses for a project.

* **Parameters:**
  * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The ID of the project or its hash_id
  * **project** (*Project* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str))
* **Returns:**
  The list of pending analysis
* **Return type:**
  [list](https://docs.python.org/3/library/stdtypes.html#list)[Analysis]
* **Raises:**
  **NeuralkException** – If the project retrieval fails

<!-- !! processed by numpydoc !! -->

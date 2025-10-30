# Neuralk.project_files.create

#### Neuralk.project_files.create(project, name, file_path)

Create a new project file and upload it to object storage.

* **Parameters:**
  * **project** (*Project*) – The project to which the file belongs.
  * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The name of the file.
  * **file_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The path to the file.
* **Returns:**
  The created project file object.
* **Return type:**
  ProjectFile
* **Raises:**
  **NeuralkException** – If the file upload fails.

<!-- !! processed by numpydoc !! -->

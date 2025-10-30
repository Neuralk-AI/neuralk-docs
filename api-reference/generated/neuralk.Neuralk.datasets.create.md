# Neuralk.datasets.create

#### Neuralk.datasets.create(project, name, file_path)

Create a new dataset and upload its file to object storage.

* **Parameters:**
  * **project** (*Project*) – The project to which the dataset belongs or its hash_id.
  * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The name of the dataset.
  * **file_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The path to the dataset file.
* **Returns:**
  The created dataset object.
* **Return type:**
  Dataset
* **Raises:**
  **NeuralkException** – If the dataset creation or upload fails.

<!-- !! processed by numpydoc !! -->

# Neuralk.datasets.create_from_url

#### Neuralk.datasets.create_from_url(project, name, file_name, file_url, file_format)

Create a new dataset from a distant url

* **Parameters:**
  * **project** (*Project*) – The project to which the dataset belongs or its hash_id.
  * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The name of the dataset.
  * **file_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The name of the uploaded file.
  * **file_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The url of the uploaded file.
  * **file_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The format of the uploaded file.
* **Returns:**
  The created dataset object.
* **Return type:**
  Dataset
* **Raises:**
  **NeuralkException** – If the dataset creation or upload fails.

<!-- !! processed by numpydoc !! -->

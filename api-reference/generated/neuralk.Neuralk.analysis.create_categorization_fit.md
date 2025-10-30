# Neuralk.analysis.create_categorization_fit

#### Neuralk.analysis.create_categorization_fit(dataset, name, taxonomy_file=None, target_columns=None, id_columns=None, categorizer_feature_cols=None)

Create a new categorization fit analysis.

* **Parameters:**
  * **dataset** (*Dataset*) – The dataset to use for the analysis.
  * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The name of the analysis.
  * **target_columns** ([*list*](https://docs.python.org/3/library/stdtypes.html#list) *[*[*str*](https://docs.python.org/3/library/stdtypes.html#str) *]* *,* *optional*) – The target column name.
  * **id_columns** ([*list*](https://docs.python.org/3/library/stdtypes.html#list) *[*[*str*](https://docs.python.org/3/library/stdtypes.html#str) *]* *,* *optional*) – List of ID column names.
  * **categorizer_feature_cols** ([*list*](https://docs.python.org/3/library/stdtypes.html#list) *[*[*str*](https://docs.python.org/3/library/stdtypes.html#str) *]* *,* *optional*) – List of categorizer feature columns.
  * **taxonomy_file** (*ProjectFile* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str))
* **Returns:**
  The created analysis object.
* **Return type:**
  Analysis
* **Raises:**
  **NeuralkException** – If the analysis creation fails.

<!-- !! processed by numpydoc !! -->

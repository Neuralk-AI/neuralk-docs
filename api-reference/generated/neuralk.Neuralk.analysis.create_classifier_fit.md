# Neuralk.analysis.create_classifier_fit

#### Neuralk.analysis.create_classifier_fit(dataset, name, target_column, id_columns=None, feature_column_name_list=None, fast_nicl_mode=False)

Create a new classifier fit analysis.

* **Parameters:**
  * **dataset** (*Dataset*) – The dataset to use for the analysis.
  * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The name of the analysis.
  * **target_column** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The target column name.
  * **id_columns** ([*list*](https://docs.python.org/3/library/stdtypes.html#list) *[*[*str*](https://docs.python.org/3/library/stdtypes.html#str) *]* *,* *optional*) – List of ID column names.
  * **feature_column_name_list** ([*list*](https://docs.python.org/3/library/stdtypes.html#list) *[*[*str*](https://docs.python.org/3/library/stdtypes.html#str) *]* *,* *optional*) – List of feature column names.
  * **fast_nicl_mode** ([*bool*](https://docs.python.org/3/library/functions.html#bool))
* **Returns:**
  The created analysis object.
* **Return type:**
  Analysis
* **Raises:**
  **NeuralkException** – If the analysis creation fails.

<!-- !! processed by numpydoc !! -->

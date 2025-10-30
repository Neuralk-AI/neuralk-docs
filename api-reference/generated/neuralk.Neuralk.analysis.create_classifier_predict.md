# Neuralk.analysis.create_classifier_predict

#### Neuralk.analysis.create_classifier_predict(dataset, name, classifier_fit_analysis, fast_nicl_mode=False)

Create a new classifier predict analysis from a fit analysis.

* **Parameters:**
  * **dataset** (*Dataset*) – The dataset to use for prediction.
  * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The name of the prediction analysis.
  * **classifier_fit_analysis** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Analysis*) – The fit analysis object or its id.
  * **fast_nicl_mode** ([*bool*](https://docs.python.org/3/library/functions.html#bool))
* **Returns:**
  The created prediction analysis object.
* **Return type:**
  Analysis
* **Raises:**
  **NeuralkException** – If the analysis creation fails.

<!-- !! processed by numpydoc !! -->

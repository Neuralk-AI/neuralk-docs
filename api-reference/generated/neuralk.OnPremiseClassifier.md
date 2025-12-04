# OnPremiseClassifier

### *class* OnPremiseClassifier(, host, dataset_name='dataset', model='nicl-small', timeout_s=900, metadata=None, user=None, api_version=None, default_headers=None)

Sklearn-style estimator proxying fit/predict calls to an on-premise NICL server.

This classifier connects to a local or self-hosted NICL (Neural In-Context Learning)
server and provides a scikit-learn compatible interface for classification tasks.
It’s designed for users who have deployed NICL on their own infrastructure.

* **Parameters:**
  * **host** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Base URL of the NICL server (e.g., “[http://localhost:8000](http://localhost:8000)”).
    This is a required parameter.
  * **dataset_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *,* *default="dataset"*) – Name identifier for the dataset used in API requests.
  * **model** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *,* *default="nicl-small"*) – Model identifier/path to use for inference (e.g., “nicl-small”, “nicl-large”).
  * **timeout_s** ([*int*](https://docs.python.org/3/library/functions.html#int) *,* *default=900*) – Request timeout in seconds for API calls.
  * **metadata** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict) *,* *optional*) – Optional metadata dictionary to include with requests.
  * **user** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *,* *optional*) – Optional user identifier for request tracking.
  * **api_version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *,* *optional*) – Optional API version string to send as ‘Nicl-Version’ header.
  * **default_headers** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict) *,* *optional*) – Optional default headers to include with every request (e.g., authentication).
* **Variables:**
  * **classes** (*ndarray* *of* *shape* *(**n_classes* *,* *)*) – The unique class labels found during fit.
  * **X_train** (*ndarray* *of* *shape* *(**n_samples* *,* *n_features* *)*) – Training data stored during fit.
  * **y_train** (*ndarray* *of* *shape* *(**n_samples* *,* *)*) – Training labels stored during fit.
  * **last_response** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict) *,* *optional*) – The last response received from the remote server (set after predict/predict_proba).

### Examples

```pycon
>>> from neuralk import OnPremiseClassifier
>>> import numpy as np
>>>
>>> # Initialize the classifier with your NICL server URL
>>> clf = OnPremiseClassifier(
...     host="http://localhost:8000",
...     model="nicl-small",
...     timeout_s=300
... )
>>>
>>> # Generate some training data
>>> X_train = np.random.randn(100, 10).astype(np.float32)
>>> y_train = np.random.randint(0, 2, 100).astype(np.int64)
>>>
>>> # Fit the classifier (stores training data)
>>> clf.fit(X_train, y_train)
>>>
>>> # Make predictions
>>> X_test = np.random.randn(10, 10).astype(np.float32)
>>> predictions = clf.predict(X_test)
>>> probabilities = clf.predict_proba(X_test)
```

### Notes

- The classifier requires numeric input data (numpy arrays with float32 dtype).
- Training labels must be integers (int64 dtype).
- The fit method only stores the training data; actual model training happens
  on the remote server during predict/predict_proba calls.
- For advanced use cases, consider using the low-level helpers in
  `neuralk.model.classify` directly.

<!-- !! processed by numpydoc !! -->

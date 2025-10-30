# Neuralk.datasets.wait_until_complete

#### Neuralk.datasets.wait_until_complete(dataset, refresh_time=1.0, timeout=None, verbose=False)

Wait for analysis until it is finished.

* **Parameters:**
  * **analysis** (*Analysis* *or* [*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the analysis to wait for, or its ID.
  * **refresh_time** ([*float*](https://docs.python.org/3/library/functions.html#float)) – time (in seconds) between status checks.
  * **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float) *,* *optional*) – maximum time to wait in seconds.
  * **verbose** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – whether to display status messages.
  * **dataset** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Dataset*)
* **Returns:**
  the final analysis object.
* **Return type:**
  Analysis

<!-- !! processed by numpydoc !! -->

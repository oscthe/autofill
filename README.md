# autofill


<p align="center">
  <img src="missing_values.png" />
</p>

autofill is a simple module for analyzing and imputing missing values in a pandas dataframe. 

For a specific column, autofill will split the data, fit the imputing techniques and evaluate its fit on a random test-sample.
Sample data used in the example below is available [here](https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot).

### Installation

```bash
pip install autofill
```

### Example usage
```python
import pandas as pd
from autofill.engine import AutoFill

df = pd.read_csv("melb_data.csv")
auto_fill = AutoFill()
auto_fill.missing_analysis(df)

```


### Running tests

To run the unit tests, simply:

```bash
python -m pytest
```

# naïve-irt-1pl  
Naïve IRT: A Speed-Optimized and Accurate Alternative to the Rasch Model  

This is a Python program for estimating Item Response Theory (IRT) parameters for a Rasch model (1PL). For synthetic IRT data generation, the [GIRTH](https://eribean.github.io/girth/) package can be used. Additionally, the program's structure and parameters are compatible with the [GIRTH](https://eribean.github.io/girth/) package.  
Below is a description of the available function. For more details, visit the [GIRTH homepage](https://eribean.github.io/girth/).  

# Usage

To run Naïve IRT with unidimensional models (1PL).

### Complete Data

```python
import numpy as np
from girth.synthetic import create_synthetic_irt_dichotomous
from naive_irt import naive_irt_1pl

# Create Synthetic Data
difficulty = np.linspace(-2.5, 2.5, 10)
discrimination = np.random.rand(10) + 0.5
theta = np.random.randn(500)

syn_data = create_synthetic_irt_dichotomous(difficulty, discrimination, theta)

# Solve for parameters
estimates = naive_irt_1pl(syn_data)

# Unpack estimates
ability_estimates = estimates['Ability']
difficulty_estimates = estimates['Difficulty']
```

### Missing Data

Missing data is supported using with the `tag_missing_data` function of `GIRTH` package.

```python
from girth import tag_missing_data
from naive_irt import naive_irt_1pl

# import data (you supply this function)
my_data = import_data(filename)

# Assume its dichotomous data with True -> 1 and False -> 0
tagged_data = tag_missing_data(my_data, [0, 1])

# Run Estimation
results = naive_irt_1pl(tagged_data)
```

# Support

## Installation

From Source

```sh
pip install . -t $PYTHONPATH --upgrade
```
# Contact

Please contact me with any questions or feature requests. Thank you!

Juan Ramón Rico
juanramonrico@ua.es

Miguel Arevalillo
miguel.arevalillo@uv.es

# License

MIT License

Copyright (c) 2025 Juan Ramón Rico and Miguel Arevallillo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

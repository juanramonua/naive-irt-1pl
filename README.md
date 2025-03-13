# Naïve IRT (1PL)

Naïve IRT: A Speed-Optimized and Accurate Alternative to the Rasch Model  

This is a Python program for estimating Item Response Theory (IRT) parameters for a Rasch model (1PL). For synthetic IRT data generation, the [GIRTH](https://eribean.github.io/girth/) package can be used. Additionally, the program's structure and parameters are compatible with the [GIRTH](https://eribean.github.io/girth/) package. 

# Proposed method

### Step 1: Computation of Item Facility and Item Difficulty
For each tesxt item $i$:

1. Compute *Item Facility* ($F_i$):

   $F_i = \frac{\text{number of correct responses to item } i}{\text{total responses to item } i}$
  
   This represents the proportion of test-takers who answered item $i$ correctly.

2. Compute \textit{Item Difficulty} ($D_i$) as:

   $D_i = 1 - F_i$
  
   This transformation ensures that items with higher facility (easier items) receive lower difficulty scores and items with lower facility (harder items) receive higher difficulty scores.

### Step 2: Computation of Test-Taker Ability

For each test-taker $j$:

1. Sum the **difficulties of correctly answered items**:

   $S_{\text{correct}, j} = \sum_{i \in C_j} D_i,$
   
   where $C_j$ is the set of items correctly answered by subject $j$.

3. Sum the **facilities of incorrectly answered items**:

   $S_{\text{incorrect}, j} = \sum_{i \in I_j} F_i$

   where $I_j$ is the set of items incorrectly answered by subject $j$.

4. Compute **Subject Ability** ($A_j$) as:

   $A_j = \frac{S_{\text{correct}, j}}{S_{\text{correct}, j} + S_{\text{incorrect}, j}}$

   In our practical implementations, any potential undefined $ 0/0 $ division when computing $A_j$ is addressed by assigning a default value of 0.5, ensuring computational stability.

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

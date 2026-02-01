# improper-payments-dgp

[![](https://github.com/wkingc/improper-payments-dgp-py-package/actions/workflows/python-package.yml/badge.svg)](https://github.com/wkingc/improper-payments-dgp-py-package/actions/workflows/python-package.yml)

[![](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

A Python package to simulate data for improper payments.

## Installation

```bash
pip install improper-payments-dgp
```

## Quick Start

```python
from improper_payments_dgp import improper_payments_dgp

# Generate 100,000 payments with maximum payment amount of $1,000, mean 
# payment amount of $100, and a standard devation of 1/2 the payment 
# amount (e.g., coefficient of variation equal to 0.5).  The percentage 
# of each payment that is improper is between 40% and 60% of the 
# payment amount, and the probability that each payment is improper is 10%.

pop_data = improper_payments_dgp(
    mean_target=100, 
    cv_target=1/2, 
    A=0, 
    B=1000, 
    b=(0.4, 0.6), 
    p_improper=0.1, 
    size=100000, 
    random_state=123
)

print(f"The mean payment amount is ${pop_data.X.mean():.2f} with a total payment amount of ${pop_data.X.sum():,.2f}.")

print(f"The coefficient of variation for payment amount is {pop_data.X.var()**0.5/pop_data.X.mean():.2%}.")

print(f"The minimum and maximum percentages of improper payments are {pop_data.B.min():.2%} and {pop_data.B.max():.2%}, respectively.")

print(f"The probability of an improper payment is {pop_data.Z.mean():.2%}.")

print(f"The mean improper payment amount (conditional on being improper) is ${pop_data.Y[pop_data.Y > 0].mean():.2f}.")

print(f"The total improper payment amount is ${pop_data.Y.sum():,.2f}.")
```

The generated dataset includes:

- **Payment amounts** (X): Following a truncated gamma distribution
- **Improper percentages** (B): Uniform distribution of what portion is improper
- **Improper indicators** (Z): Binary indicators of whether payment is improper
- **Improper amounts** (Y): Calculated as X × B × Z

## API Reference

### `improper_payments_dgp(mean_target, cv_target, A, B, b, p_improper, size=1, random_state=None)`

Generate simulated data for improper payments.

**Parameters:**

- `mean_target` (int or float): Target mean payment amount
- `cv_target` (float): Target coefficient of variation for payment amounts
- `A` (int or float): Minimum payment amount
- `B` (int or float): Maximum payment amount  
- `b` (int, float, or tuple): Bounds for uniform distribution of improper percentages (0 ≤ b ≤ 1)
- `p_improper` (float): Probability that a given payment is improper
- `size` (int): Number of payments to generate
- `random_state` (int, optional): Random seed for reproducibility

**Returns:**

- `pandas.DataFrame`: DataFrame with columns:
  - `X`: Payment amounts (truncated gamma distribution)
  - `B`: Improper payment percentages (uniform distribution)
  - `Z`: Improper payment indicators (binomial distribution)
  - `Y`: Improper payment amounts (X × B × Z)

## Requirements

- Python ≥ 3.9
- truncated-gamma-rvs
- scipy
- pandas

## Development

```bash
git clone https://github.com/wkingc/improper-payments-dgp-py-package.git
cd improper-payments-dgp-py-package
pip install -e ".[dev]"
python -m pytest
```

## License

MIT License. See [LICENSE](LICENSE) for details.

## Documentation

For a complete usage guide, see <https://www.kingcopeland.com/improper-payments-dgp-py/>.

## Citation

If you use this package in your research, please consider citing it:

```bibtex
@software{copeland2026ipaymentsdgp,
    author = {Wade K. Copeland},
    title = {{improper-payments-dgp: A Python package to simulate data for improper payments}},
    url = {https://pypi.org/project/improper-payments-dgp/},
    version = {0.1.7},
    year = {2026}
}
```
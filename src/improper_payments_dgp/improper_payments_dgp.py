from truncated_gamma_rvs import truncgamma_rvs
from scipy.stats import uniform, binom
import pandas as pd

def improper_payments_dgp(mean_target, cv_target, A, B, b, p_improper, size, random_state = None):
    """This function generates simulated data for improper payments.
    
    Args:
        mean_target (int or float): The target mean payment amount.
        cv_target (float): The target coefficient of variation (e.g., CV[X] = SD[X]/mean[X]) for the payment amount.
        A (int or float): The minimum payment amount.
        B (int or float): The maximum payment amount.
        b (int, float, or tuple): Bounds of the uniform distribution (0 <= b <= 1) for the percentage of each payment that is improper.
        p_improper (float): Probability that a given payment is improper.
        size (int): The number of payments to generate.
        random_state (int): The seed for random number generation to create reproducible results.
        
    Returns:
        A Pandas DataFrame with the following:
            X: Random variate(s) of a truncated gamma distribution for the payment amount.
            B: Random variate(s) of a uniform distribution for the percent of the payment that is improper.
            Z: Random variate(s) of a binomial distribution that indicate if a payment is improper.
            Y: Random variate(s) for the improper payment amount.
        
    Example:
        >>> pop_data = improper_payment_rvs(mean_target = 100, cv_target = 1/2, A = 0, B = 1000, b = (0.4, 0.6), p_improper = 0.1, size = 100000, random_state = 123)
        >>> print(f"The mean payment amount is ${pop_data.X.mean():.2f} with a total payment amount of ${pop_data.X.sum():,.2f}.\nThe coefficient of variation for payment amounts is {pop_data.X.var()**0.5/pop_data.X.mean():.2%}.\nThe minimum and maximum percentages of improper payments are {pop_data.B.min():.2%} and {pop_data.B.max():.2%}, respectively.\nThe probability of an improper payment is {pop_data.Z.mean():.2%}.\nThe mean improper payment amount (conditional on being improper) is ${pop_data.Y[pop_data.Y > 0].mean():.2f} with a total improper payment amount of ${pop_data.Y.sum():,.2f}.")
    """
    b = b if type(b) is tuple else (b, b)
    
    X = truncgamma_rvs(mean_target = mean_target, cv_target = cv_target, A = A, B = B, size = size, random_state = random_state)
    B = uniform.rvs(size = size, loc = b[0], scale = b[1] - b[0], random_state = random_state)
    Z = binom.rvs(size = size, n = 1, p = p_improper, random_state = random_state)
    Y = X*B*Z
    
    pop_data = pd.DataFrame({
        "X": X,
        "B": B,
        "Z": Z,
        "Y": Y})
    
    return pop_data
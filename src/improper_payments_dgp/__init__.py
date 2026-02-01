"""
Improper Payments Data Generating Process Package

A Python package to simulate data for improper payments.
"""

from .improper_payments_dgp import improper_payments_dgp

__version__ = "0.1.6"
__author__ = "Wade K. Copeland"
__email__ = "wade@kingcopeland.com"

# This controls what gets imported with "from improper_payments_dgp import *"
__all__ = ["improper_payments_dgp"]
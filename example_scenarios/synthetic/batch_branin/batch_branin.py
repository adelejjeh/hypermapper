#!/usr/bin/python
import math

import os
import sys
import warnings
from collections import OrderedDict

# ensure backward compatibility
from hypermapper import optimizer  # noqa


def branin_function(X):
    """
    Compute the branin function.
    :param X: dictionary containing the input points.
    :return: the value of the branin function
    """
    values = []
    for idx in range(len(X["x1"])):
        x1 = X["x1"][idx]
        x2 = X["x2"][idx]
        a = 1.0
        b = 5.1 / (4.0 * math.pi * math.pi)
        c = 5.0 / math.pi
        r = 6.0
        s = 10.0
        t = 1.0 / (8.0 * math.pi)

        y_value = (
            a * (x2 - b * x1 * x1 + c * x1 - r) ** 2 + s * (1 - t) * math.cos(x1) + s
        )
        values.append(y_value)

    return values


def main():
    parameters_file = (
        "example_scenarios/synthetic/batch_branin/batch_branin_scenario.json"
    )
    optimizer.optimize(parameters_file, branin_function)
    print("End of Branin.")


if __name__ == "__main__":
    main()

import pandas as pd
import numpy as np
from julia import Main
import sys

print(Main.eval('[x^2 for x in 0:4]'))

print("Hello World")
print(sys.version_info)
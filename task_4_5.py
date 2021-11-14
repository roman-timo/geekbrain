# 5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.

import sys
from utils import currency_rates

print(list(map(currency_rates, sys.argv[1:])))
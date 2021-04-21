from collections import OrderedDict
import numpy as np
import pandas as pd

import sys
sys.path.append("../../../")
from utests import project_test, generate_random_tickers, generate_random_dates, assert_output


@project_test
def test_calculate_arithmetic_rate_of_return(fn):
    tickers = generate_random_tickers(5)
    dates = generate_random_dates(6)

    fn_inputs = {
        'close': pd.DataFrame(
            [
                [21.050810483942833, 17.013843810658827, 10.984503755486879, 11.248093428369392, 12.961712733997235],
                [15.63570258751384, 14.69054309070934, 11.353027688995159, 475.74195118202061, 11.959640427803022],
                [482.34539247360806, 35.202580592515041, 3516.5416782257166, 66.405314327318209, 13.503960481087077],
                [10.918933017418304, 17.9086438675435, 24.801265417692324, 12.488954191854916, 10.52435923388642],
                [10.675971965144655, 12.749401436636365, 11.805257579935713, 21.539039489843024, 19.99766036804861],
                [11.545495378369814, 23.981468434099405, 24.974763062186504, 36.031962102997689, 14.304332320024963]],
            dates, tickers)
    }
    fn_correct_outputs = OrderedDict([
        (
            'arithmetic_returns',
            pd.Series([4.77892789, 0.22689225, 51.39616553, 6.83675173, 0.07443370],tickers)
        
        )])

    assert_output(fn, fn_inputs, fn_correct_outputs)

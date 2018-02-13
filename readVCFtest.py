import pandas as pd
import io
import os
import allel

# from sklearn import tree
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split

import CONSTS


def read_vcf():
    path = "data/sample.vcf"
    with open(path, 'r') as f:
        lines = [l for l in f if not l.startswith('##')]
    return pd.read_table(
        io.StringIO(str.join(os.linesep, lines)),
        dtype={'#CHROM': str, 'POS': int, 'ID': str, 'REF': str, 'ALT': str,
               'QUAL': str, 'FILTER': str, 'INFO': str}
    ).rename(columns={'#CHROM': 'CHROM'})


if __name__ == '__main__':
    p = read_vcf()

    for key in p.keys():
        for h_idx in CONSTS.HEALTHY_IDX:
            if str(h_idx) in key:
                p[key].append("1")
            #else:
                # p[key]['healthy'] = 0

    # print(str(p))



    print(str(test))

import pandas as pd
import numpy as np
from inspect import signature

def contain_relation(df1, df2, keys=None):
    sig = signature(contain_relation)
    if not isinstance(df1, pd.DataFrame):
        raise TypeError('{} must be DataFrame'.format(sig.parameters['df1'].name))
    if not isinstance(df2, pd.DataFrame):
        raise TypeError('{} must be DataFrame'.format(sig.parameters['df2'].name))

    if df1.empty:
        raise ValueError('{} can not be empty'.format(sig.parameters['df1'].name))
    if df2.empty:
        raise ValueError('{} can not be empty'.format(sig.parameters['df2'].name))

    if keys == None:
        common_df_cols = set(df1.columns)-(set(df1.columns)-set(df2.columns))
        keys = list(common_df_cols)
    else:
        # TODO:check if keys in df1,df2
        pass
    #TODO: check two df's value-type same
    df1_g = df1.groupby([keys])
    df1_num_of_keys = set(df1_g.groups.keys())
    df2_g = df2.groupby([keys])
    df2_num_of_keys = set(df2_g.groups.keys())
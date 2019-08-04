# coding: utf-8

import pandas as pd
import numpy as np

df = pd.read_csv("train.csv")
dfs_info = pd.read_csv("songs.csv")
dfu_info = pd.read_csv("members.csv")

# Filter positive and freq
dfp = df.loc[df.target > 0]
fl = dfp.song_id.value_counts()
fl = fl[fl > 5]
dfp = dfp.loc[dfp.song_id.isin(fl.index)]

dfi = dfp[['song_id']]
dfi = dfi.drop_duplicates()
dfi = pd.merge(dfi, dfs_info, how='left', on=['song_id'])
dfi = dfi.reset_index()
dfi = dfi.reset_index()

dfu = pd.merge(dfp, dfu_info, how='left', on='msno')
dfu = pd.merge(dfu, dfi[['level_0','song_id']], how='left', on='song_id')


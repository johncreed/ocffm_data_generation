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

dset = {}
dfu['his'] = np.nan
dfu.his = dfu.his.apply(str)
for i, row in dfu.iterrows():
    user_id = row['msno']
    song_id = str(row['level_0'])
    if user_id in dset:
        dfu.set_value(i, 'his', '|'.join(dset[user_id][-50:]))
        dset[user_id].append(song_id)
    else:
        dset[user_id] = [song_id]
    if i % 100000 == 0:
        print(i)

dfi.to_csv("top_song.csv", index = False)
dfu.to_csv("listener.csv", index = False)

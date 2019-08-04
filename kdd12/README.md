# Preprocess

1. filter.py
Input: training.csv 
Output: ad.filter.csv, user.filter.csv

# Create item (ad) file

2. ad.py
Input: ad.filter.csv
Output: ad.gby.csv, AdID.map

3. ad_ffm.py / ad_fm.py / ad_mf.py
Input: ad.gby.csv
Output: ad.ffm / ad.fm / ad.mf


# Create user file

4. user.py
Input: user.filter.csv, AdID.map
Output: user.gby.csv

5. shuffle the user.gby.csv
Input: user.gby.csv
Output: user.gby.csv.shuf

6. user_ffm_shuf.py
Input: user.gby.csv.shuf
Output: user.shuf.ffm

7. split.py user.shuf.ffm to 8:1:1
Input: user.shuf.ffm
Output: user.shuf.tr.ffm user.shuf.va.ffm user.shuf.te.ffm

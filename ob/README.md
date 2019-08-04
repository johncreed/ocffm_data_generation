# Data preprocess 

1. filter.py

* Input: clicks_train.csv, cv_events.csv, promote_content.csv
* Output: click_filter.csv, events_filter.csv, ad_filter.csv
* Purpose: Filter by number of clicks count

2. add_filter.py

* Input: ad_filter.csv, events_filter.csv, click_filter.csv, document_meta.csv
* Output: events_filter_label.csv, ad_filter.csv

3. split.sh

* Input: events_filter_label.csv
* Output: events_filter_label.{tr,va,te}.csv

```
for ext in tr va te
do
    mv events_filter_label.$ext.csv ob.$ext.csv
done
for ext in va te
do
    head -n1 ob.tr.csv > lala
    cat ob.$ext.csv >> lala
    mv lala ob.$ext.csv
done
```

4. Convert ob.{tr,va,te}.csv to data format

* context_ffm.py, context_fm.py, context_mf.py
* Input: ob.{tr,va,te}.csv 
* Output: ob.{tr,va,te}.{ffm,fm,mf}

5. Convert ad_filter.csv to data format

* item_ffm.py, item_fm.py, item_mf.py
* Input: ad_filter.csv 
* Output: item.{ffm,fm,mf}

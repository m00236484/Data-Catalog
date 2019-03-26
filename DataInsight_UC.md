## Introduction
The objective of this use case is to help Datainsight fellows to get a centrlize plateform to find their dataset, 
the fellow will be able to seach for a specfic datasets on the data catlog or he cn search for this dataset on other datasources 
that the Data-Catalog has access on.

## Functionality

# Catalog
1. Search for dataset (by name, category, text) internally in data-catalog
2. Search for dataset (by name, category, text) externally in pre-defind sources such as US Open Data, AWS public data, etc.
3. Request and add a new dataset if this dataset not available in the catalog and user have the valid information to bring this dataset in.
4. Tracking The changes on the datasets.

# Extracting
1. Extract defined datasets from the sources system to S3 as default.
2. Scheduling jobs extract datas in daily, weekly, or in realtime if ablicable.
3. Dataset conversion to transfer the dataset from file format to database format or might to streaming this datasets to streaming topic or channel.
4. Notify subscribed fellows when changes happened on datasets.

# Profiling
1. Profiling the extracted datasets.
2. If dataset has been changed and fresh data downloaded then data-catalog will provide statstic to compare between different version of same dataset.        
3. Show simlity between datasets if similar datasets have been downloaded from different source.



## Dataset Sources
1. US Open data.
2. AWS Public Data.
3. Kagal.

  
# Data-Catalog
Introduction:

When it comes to widely availablity  of data sources it comes to Data Catalog, Data catalog takes care of each single data source, it should answers the below question
1- Where are the data sources at?
2- How could you reach to this data sources?
3- How to keep the stackholder aligned with changes on these datasources?
4- What action should be taken when there is a change on a data source?
5- What the impcat of that change on other dependant data source?



Tech Stack:
1- Python
2- Apach Flask
3- Postgrece
4- Spark
5- Kafka
6- APIs


![image] https://raw.githubusercontent.com/m00236484/Data-Catalog/master/Datacatalog.jpg

Business Value:

Use Case:
As fellow in Insight Data Engineer Program one of challanges that data-enginers and data-sintests facing is geting a setable and reliable dataset and based on that this use case as part of the Data catalog roadmap it will help Insightdata fellows to have an plateform that opens to sources of datasets such as AWS Public Dataset, US Governmet Open DataSets, and etc.

In this use case I aim to catalog these data sets ara available on previouse sources and avilabilty to:
1- Extract the available datasets into Datacatalog S3.
2- Sunc periodicly with the datasets sources to capture whatever changes and does:
    a- create a new dataset if there is a new dataset on the source
    b- add a new version if existing dataset has been updated and linage between the master and versions.
    c- notifiy subscribed fellows if there change on a dataset.  
3- Allow the fellows to search for a specfic a dataset by name or category.
4- Allow the fellows to add a new dataset if it's not exist in the Datacatalog.

Engineering Chalanges:
1- since the datasets live across different sources
    a- each source has it's own chracterstic and customization.
    b- each dataset has different formats and extension (CSV, JSON,and etc).
2- Size: most of dataset are very huage  (hundred of GB, terabyte) which requered a better utlization for resources during  moving it from source to Datacatalog.        
    


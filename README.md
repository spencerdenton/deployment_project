# <u>Mini-project IV</u>

### [Assignment](assignment.md)

## <u>Table of Contents</u>
- [Notebooks]
    - [Main Notebook](/notebooks/instructions.ipynb)
- [Data]
    - [CSV of Banking Data](/data/data.csv)   
- [Presentation PDF](/images/Deployment_Project_Presentation.pdf)
- [Output](/src/)
    - [API script](/src/app.py)
    - [Model](/src/xgb_classifier.pkl)

## <u>Project/Goals</u>
To predict loan approvals using machine learning models developed with pipelines and deployed to the cloud. 

## <u>Hypothesis</u>
I hypothesise that applicants will be more likely to be approved for loans that have credit history, higher incomes, co-applicant's, are applyiong for loans of lower values and are buying properties in a more urban area.  

## <u>EDA</u>
I discovered there were some missing values, most of the applicants are male and the loan amounts seem quite low given current property values. It seems most of this data may have been taken from a single location so it might not be that diverse. 

## <u>Process</u>

- For the EDA I explored the data using a variety of data visualizations and statistices.
- I then cleaned the data replacing missing values with averages (mode for catgorical and median for numeric columns) and ropped rows mkissong credit history info as that would be critical to determining loan eligibility.
- I also scaled the numeric data with log transformations to deal with the distribution and outliers. 
- Following this I built both an XGBoost and Random Forrest Model and ran grid search to to determine the best model and parameters. 
- I then built a pipeline to combine a lot of my previous steps in to a single pipeline.
- Saved model to a Pickle file. 
- I then built an API using Flask and deployed it to the cloud via AWS. 

## <u>Results/Demo</u>
Model seemed to perform well. Had a higher than 80% accuracy and other metrics were also postive. Seemed to have a higher false postive, than false negatives which also seems to make sense as it would be better to reject a qualified applicant than approve someone who might default on a loan. 

## <u>Challanges</u> 
- Issues getting everything into a working pipeline. A lot of steps worked individually, but when combined seemed to generate some errors, that required debugging. 
- AWS. Lost the location of my key pair, so took some time to connect to the server while I relocated it. 
- Time. We only had one day to complete this project so was a lot to do in a short amount of time. 

## <u>Future Goals</u>
- Run again with more data. Dataset was quite small. Would prefer to have more data to build the model on to improve accuracy of models.
- Edit code to make it more efficent.
- Look at doing a similar but more complex project. Seems like there is a lot of potential for predictive ML modelling within the finance industry. 
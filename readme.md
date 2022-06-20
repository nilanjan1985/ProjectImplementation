# ML Tech Task
Truecaller 2021/2022

## 1. Overview

This task is concerned with applying machine learning to data about advertisement impressions of Truecaller users. 
**The aim of the project is to automatically select which type of ad to show to a user in order to maximise the
click-through-rate (defined in section 2.1)**. 
There are two parts to this exercise: 
the first part is about completing missing code snippets, 
the second is about reviewing the approach taken here.

## 2. Details about this project

The project and project files provided here form an "end-to-end" machine learning experiment, from data preparation
to model training and model assessment. 
We have removed some code pieces which are highlighted with `# TODO:`. 
When the missing pieces are completed, the project should run as described in the setup section below.

### 2.1 Setup
We recommend starting in a new virtual environment. The code has been tested on Python 3.7 and 3.8. 
To install dependencies run this command:

`python -m pip install -e <path-to-project-folder>`

To run the pipeline, we recommend navigating to the `/src` folder and running 

`python -m ml_tech_task`

Optional parameters:

`--tune_hyper_parameters`
= Boolean flag to toggle between using a grid search and preset model values

Note that this will not run successfully because code-fragments are missing!

### 2.1 The data
The data provided here is a single day's snapshot of user behaviour. 
The user identifier is labelled 'user_id' and the date of the snapshot is labelled 'ds'. 
In addition there is also other information about the user: 
* prince_range: the price range of the device the app is installed on 
* gender: gender of the user
* age_group: age group of the suer
* region: geographic region of the user based on IP
* country: country location of the user based on IP
* \<KPI\>\_\<ad-type\>\_\<time-period\>: user behaviour:
  * KPI = 
    * n_imps: number of impressions (number of times an ad type has been shown)
    * n_clicks: number of clicks (number of times an ad type has been clicked on)
    * ctr: click-through-rate (=n_clicks/n_imps)
  * Ad-type = 
    * total: all ads shown (sum of all types)
    * unknown: we do not have a label for this ad type
    * others: the type of ad which was shown (e.g. 'gaming')
    * **Note that not all types are included in this data set for simplicity reasons.**
      You may assume we are showing only the ad types detailed here to the user and scale "total" accordingly. 
      Alternatively you may pursue a different approach as you see fit. 
  * time-period = 
    * 1d: sum/average over the last day
    * 1w: sum/average over the last week
    * 1m: sum/average over the last month
    * 3m: sum/average over the last three months 
    * (it is the sum of n_imps & n_clicks, but the average for ctr)

## 3. The tasks
We anticipate that completion of all the tasks should take 4-7h.

### 3.1 Task 1

1. Fix the code by completing all the missing pieces highlighted with `# TODO:` 
   (They are only in the two nodes.py files). 
   The code should run as described in section 2.1 without errors.
2. Do you think this model is performing well? Why/ why not?
3. Submit a zip file containing the `src/ml_tech_task` folder alongside a brief discussion document (500 words or fewer) 
   on the model performance. 

#### Rules
* Do not change the pipeline defined in pipeline.py
* Avoid violating the type-hints, unless you have a very convincing reason to do so.
* Modifying other functions should not be necessary, but you might change them if you find they are limiting your 
  solution, so don't shy away from modifications. 
* You are free to create other functions or classes if you feel that is beneficial (but this is not expected).

#### Tips 
* This task is not about improving model performance. Do not spend time on optimising hyper parameters.
* What are the features and what are the targets?   
* This task is about creating a data-specific approach to ML while maintaining a generalisable framework.  
* You will need to gain a good understanding of the data. 
* Feel free do exploratory data analysis in notebooks; however we will not be considering any notebooks in the 
  assessment of this exercise.

### 3.2 Task 2 

The product owner of the project has been away since project kick-off and only knows about goals 
(maximising click-through-rate) and underlying data we have at hand. 
They reached out to you asking for your input on the project.
Write a technical note, advising the product owner about our **usage of data**. 
Cover the question from two viewpoints:
1. Explain and critique the current status of the project given the overall structure and primary data source as 
   provided here:
   focus on the overall approach currently taken in the data-engineering section, 
   specifically in the `transform_features` function.
2. Comment on future scope for this project. 
   We only included a single day's data here, but since the project started we have created a pipeline which
   generates updated information for every day.
   Outline your vision for making the most of our data. 

Please submit this technical note as a separate document. 
   
#### Rules
* The document should be approx. 600 words.

#### Tips
* The product owner understands the field but does not have a technical background.
* This document might be passed to upper management, so it is important that the key information is quickly accessible.

# freshflow

## Overview
This repository contains a train.py file which takes input and returns model
Currently the data file is not added to git repo for security purpose

## Versions
* python==3.9
* prophet==1.1.2

### Part1: analysis
* Currently the data from data.csv file is analysed 
* There are only 3 items in the data whose sales data is available from '2021-04-03' till '2022-02-09'
* There are some duplicates which are dropped 
* the revenue columns is filled with 0 when empty
* Its noticed items - 80028349, 80028349 common patterns and seasonality but the item 80101923 doesnt have patterns
in sales except the spikes and the order quantity for this items has  been very high initially 
* 
### Part2: Modeling-1
* As part of modelling the data i have made certain assumptions that the model needs to predict salesquantity per day 
in future
* I divided the data for training till '2021-12-31' and the rest for testing
* I trained a Fb prophet model which runs individually on each items and emits the forecast in a dataframe

### Part2.1: Model results
* model is able to capture the  forecast of item1, item3 - 80028349, 80028349 due to the patterns linearity & sesonality 
 in data
* for item 80101923 is not able to capture the patterns as there no proper historical patterns 
* MAE - is around 9.3, 7.4, 4.4 for the items 80028349,80101923, 80028349 respectively


### Part3: Modeling-2
* As part of modelling the data i have made certain assumptions that the model needs to predict salesquantity per day 
in future
* In this iteration the cut off for training data for training till '2022-01-01' and the rest for testing
* I trained a Fb prophet model which runs individually on each items and emits the forecast in a dataframe

### Part3.1: Model results
* In this iteration item2 is able to better then experimnent-1 when no data available and now is able to predict a 
straight line of average sales



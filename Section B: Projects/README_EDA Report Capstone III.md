## Exploratory Data Analysis on Supermarket_sales Data Set: Capstone III


### INTRODUCTION

This dataset; ‘Supermarket Sales’ is available on Kaggle contains transactional data of three supermarkets.
It consists of 1000 records and 17 attributes (see Table 1). 

#### Table 1 Summary of Attributes
| Attribute                | Description                                                                                                          |
|--------------------------|----------------------------------------------------------------------------------------------------------------------|
| Invoice id               | Computer generated sales slip invoice identification number                                                       |
| Branch                   | 3 branches are available identified by A, B and C                                                                    |
| City                     | Location of supercenters                                                                                             |
| Customer type            | Type of customers, recorded by Members for customers using member card and Normal for without member card.          |
| Gender                   | Gender type of customer                                                                                              |
| Product line             | General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel |
| Unit price               | Price of each product in $                                                                                            |
| Quantity                 | Number of products purchased by customer                                                                             |
| Tax 5%                   | 5% tax fee for customer buying                                                                                       |
| Total                    | Total price including tax                                                                                            |
| Date                     | Date of purchase (Record available from January 2019 to March 2019)                                                  |
| Time                     | Purchase time (10am to 9pm)                                                                                           |
| Payment                  | Payment used by customer for purchase (3 methods are available – Cash, Credit card and Ewallet)                      |
| COGS                     | Cost of goods sold                                                                                                   |
| Gross margin percentage  | Gross margin percentage                                                                                              |
| Gross income             | Gross income                                                                                                         |
| Rating                   | Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)                         |

### DATA CLEANING

Here is a short summary of the methods and visualisations done during data cleaning:
1.	Importing packages: Packages for data cleaning and visualization were imported, such as pandas, seaborn, and matplotlib.pyplot.
2.	Reading supermarket_sales.csv: The dataset was read into a pandas DataFrame using the read_csv() function.
3.	Data previewing: head() function was used to preview the first few rows. 
4.	Understanding the data:  info() function was used to obtain a summary of the dataset.
5.	Exploring Numeric Data: The describe() function was used to obtain descriptive statistics of the numeric data in the dataset.
6.	Exploring the Invoice ID and gross margin percentage columns: The nunique() function was used to check the number of unique values for 'Invoice ID'
    and 'gross margin percentage' columns.
7.	Dropping columns: The drop() function was used to drop the 'Invoice ID' and 'gross margin percentage' columns since they were not useful for further analysis.
8.	Changing Date and Time Datatypes: The to_datetime() function was used to change the 'Date' and 'Time' columns' datatype to datetime.
9.	Separating Numerical and Categorical Data: The DataFrame was separated into two dataframes, one for numerical data and another for categorical data.
10.	Visualizing Numeric Data: Histograms were used to visualize the distribution of each numeric column in the dataset.
11.	Visualizing Categorical Data: Bar plots were used to visualize the distribution of each categorical column in the dataset.
12.	Dropping the Branch column: The drop() function was used to drop the 'Branch' column since it was not useful for further analysis; the information from 
    the ‘City’ column was more informative than the information from ‘Branch’ which did not add more to the dataset. 
13.	Checking for duplicates: The duplicated() and sum() functions together to check if there is any rows of duplicated data of which there wasn’t any. 

### MISSING DATA

The ‘Supermarket Sales’ dataset did not have any missing data and therefore did not require imputation or dropping of columns due to missing data.

### DATA STORIES AND VISUALISATIONS
 
Before exploring the comparative visualizations and stories, here are the histograms (numerical) and countplots (categorical) for 
all 13 variables kept in the dataset.

#### Numerical variables – Histograms:

First, we have the count of the different transaction totals. The distribution of the graph indicates that the number of transactions mostly 
decreases as the total of the transaction decreases. 

![image](https://user-images.githubusercontent.com/127414934/233711204-a75df5ef-1448-4143-91cf-a11b2deff96f.png)

For the tax, which is 5% for all transactions; cogs, and gross income, the graph distribution looks the same. This is due to the fact that the 
tax (5%) and gross margin percentage (4.76%) are the same for all instances. This essentially means that for upcoming comparative visualizations between
other numerical or categorical variables, we can focus on only one of these columns relating to income.   

![image](https://user-images.githubusercontent.com/127414934/233711557-60db50de-5360-40bd-ae3a-03709aec5180.png)

![image](https://user-images.githubusercontent.com/127414934/233711429-4f6615e7-0554-40cf-8fa7-00f8bd90af14.png)

![image](https://user-images.githubusercontent.com/127414934/233711591-cbb1ca35-a00a-4489-9f80-b36fee8aefe3.png)

The rating scores are between 4 and 10. The scores that are given most frequently appear to be between 6 and 7, and the lowest scores most frequently given are 
between 5 and 6.

![image](https://user-images.githubusercontent.com/127414934/233711714-e313a6ba-a2b6-4d47-ab53-b88436255c36.png)

The quantity score per invoice appears to be from 1 up to 10 items, with 10 being the most frequent count and 7 the least frequent.

![image](https://user-images.githubusercontent.com/127414934/233711797-4bb77f55-3547-4e5d-8cfa-b315a4c493fd.png)

The price of units varies from around $10 to just under $100. The distribution of counts/frequency across the price range is displayed in the graph.

![image](https://user-images.githubusercontent.com/127414934/233711953-99bf0f99-9d6a-43cf-aeec-9549d7d26d98.png)

#### Categorical variables – Countplots:

![image](https://user-images.githubusercontent.com/127414934/233712587-7a93250c-a446-4698-b8b6-717f5c51b931.png)

| Payment        | Count |
| -------------- | ----- |
| Ewallet        | 345   |
| Cash payment   | 344   |
| Credit card    | 311   |

![image](https://user-images.githubusercontent.com/127414934/233713006-54ccc6d2-3e6c-4cf0-b216-b96eba00bf82.png)

| Customer type | Count |
| ------------- | ----- |
| Member        | 501   |
| Normal        | 499   |

![image](https://user-images.githubusercontent.com/127414934/233713094-6e7960dd-85ef-46b6-aefd-964727f9b3fe.png)

| Gender | Count |
| ------ | ----- |
| Male   | 499   |
| Female | 501   |

![image](https://user-images.githubusercontent.com/127414934/233713160-c8e6abd6-b04a-4d52-af66-004cb297d218.png)

| City       | Count |
| ---------- | ----- |
| Yangon     | 340   |
| Mandalay   | 332   |
| Naypyitaw  | 328   |

![image](https://user-images.githubusercontent.com/127414934/233713224-2db45aca-90da-40cd-a05d-6cc2432cc877.png)

| Product line            | Count |
| ----------------------- | ----- |
| Fashion accessories     | 178   |
| Food and beverages      | 174   |
| Electronic accessories  | 170   |
| Sports and travel       | 166   |
| Home and lifestyle      | 160   |
| Health and beauty       | 152   |

Above, we have five countplots and the respective value counts for the 5 remaining numerical variables in which the distribution across 
the categorical data can be clearly examined.

#### Comparative visualizations

#### 1.	Explore numerical variables - Correlation Heatmap:

![image](https://user-images.githubusercontent.com/127414934/233713525-3a836f16-5437-4b78-bd3c-294fca4e095e.png)

The highest correlation (=0.71) is between the quantity sold and the gross income (in turn, thus also the total, cogs, and tax 5%). A high quantity of 
items sold is positively correlated with a high gross income. This is very logical as more items purchased (i.e., a higher quality will equal a higher total 
and, in turn, a higher profit/gross income). Similarly, the second-highest positive correlation is between unit price and gross income (=0.63), which again
makes sense as more expensive items will naturally lead to more expensive invoice totals and, in turn, higher gross incomes.

All the other numerical variables have correlations very close to 0, whether they are + values or – values. This means that these comparisons are not highly 
correlated at all. There is therefore not much of a relationship between the variables that meet at blue squares. For example, there is not much of a 
relationship between customer ratings and gross income.

#### 2.	Explore categorical variables - Product lines and City:


Using grouped bar plots, we can see the distribution of the numerical variables in relation to the city
(and branch A = Yangon, branch B = Naypyitaw, Branch C = Mandalay) and product lines.

![image](https://user-images.githubusercontent.com/127414934/233713793-8f279dc0-1eee-43cb-8645-497995103389.png)

![image](https://user-images.githubusercontent.com/127414934/233713840-9ce92f21-645f-4002-9e57-bb6738becf74.png)

![image](https://user-images.githubusercontent.com/127414934/233713881-209a6873-5b72-49ff-b899-6fdf58d3bf91.png)

![image](https://user-images.githubusercontent.com/127414934/233713915-9a05ea50-777e-4a1f-bbdf-53a08d440c97.png)

Above are the outputs for the averages of all categorical variables of the invoices based on the city of purchase and the product line it falls under.
In general, there are no apparent outliers (top or bottom) for either of the numerical variables in terms of the city or product line. However, the displayed 
graphs provide a good overview for all branches to compare their average income, quantities sold, customer ratings, and units per product line, but also to 
compare with the other branches.

*Similar averaged grouped barplots could be made for all categorical variables, such as payment method and gender, customer type and gender, or any 
other combination.

#### 3.	Exploring the main dependent variable – Sales:

Above is one graph looking at the average gross income per city and product line, but the sales aspect is arguably the most looked at or important
dependent variable.

Although the costs of goods sold differ per product, the gross margin percentage for all products in all lines and cities are the same. 
This eases the visualization and factors that have to be considered when exploring.

![image](https://user-images.githubusercontent.com/127414934/233714170-af55460a-744a-4734-b8fa-6a54b1c2a858.png)

The graph above is a boxplot of the gross income distribution over all product lines. From this, it is clear that the distribution of sales (gross income)
is quite similar across all product lines. There are outliers above the maximums for Sports and Travel, Food and Beverages, and Fashion Accessories. 

![image](https://user-images.githubusercontent.com/127414934/233714368-ebd2457f-10ba-4093-ac2a-28642f37503e.png)

For completion, above is also a barplot of the total gross income per product line, which similarly to the boxplot shows little difference between product lines.
Food and Beverages have the highest total gross income, while Health and Beauty have the lowest. 

![image](https://user-images.githubusercontent.com/127414934/233714469-df2180ee-d6fe-49d8-a461-a58afc14f430.png)

From this pie chart, we can see that the payment methods are close to equally responsible for the total amount of income the supermarkets generate.
Cash is responsible for the most income, with 34.7% of sales stemming from this payment method.

![image](https://user-images.githubusercontent.com/127414934/233714554-02df3b0f-4b7d-4e52-b9c7-85858db51eba.png)

This stacked barplot shows member customer vs normal customer total income split by female and male. From this, we can see that the member customers are 
responsible for slightly more of the gross income. Similarly, there are also slightly more female members compared to male members.

![image](https://user-images.githubusercontent.com/127414934/233714624-e47fa39e-b2d4-4252-8f30-e6f0243c0ded.png)

This lineplot shows the total gross income per day for the recorded period (01 Jan 2019 - 01 April 2019). This graph gives a general overview of the
gross income per day over the four-month period. We can deduce that the total income fluctuates between an estimated $50 and $350. We can also deduce 
that it fluctuates a lot and changes quite drastically between the $50 and $350 margin. Looking at the value counts, we can see the highest total gross income
in a day for the period was $355,907 on 2019-03-09. The lowest total gross income in a day for the period was $44,487.5 on 2019-02-13. 

#### Aspects to add/improve on: 

This EDA did not look at the time variable. A graph can be added to look at, for example, the average gross income per hour of the day. Similarly, this EDA looked
at gross income (to represent the sales/income of the supermarket) as the main dependent variable, but any of the other variables could also be focused on. 
Lastly, this EDA only looks at visual representations to comment on distributions of the data. No statistical testing or analysis was added in this EDA.


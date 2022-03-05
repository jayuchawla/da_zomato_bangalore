# da_zomato_bangalore
## Project Title
#### EDA on Zomato Restraunts in Bangalore

## Problem Statement
#### Studying Zomata dataset and unlocking patterns or trends to futher _define their KPIs_ (key performance indicators).

## Dataset
-   #### https://www.kaggle.com/himanshupoddar/zomato-bangalore-restaurants

## Understanding Data
-   Shape: (51717, 17)
-   Columns that can be ignored:
    -   url
    -   phone
-   multi-valued columns:
    -   rest_type 
    -   dish_liked
    -   cuisines
    -   reviews_list
    -   menu_item

## Cleaning Data
-   online_order and book_table have no null values and each value is a binary
-   rate column:
    -   all values don't follow same pattern (num.num/5), contain None, Nan, NEW, - too
    -   cleaned values are obtained by writing a custom utility (matches_pattern)
-   votes column:
    -   all values are integers
    -   no negative values
-   location column:
    -   all values are object type
    -   no invalid characters or strange values
    -   no dual names (for e.g. x yz and xyz are dual names)
-   rest_type column (unique values extracted to a list):
    -   multi-valued
    -   no dual names
-   dish_liked column (unique values extracted to a list):
    -   multi-valued
    -   dual names found (to be handled in feature engineering phase)
-   cuisines(unique values extracted to a list):
    -   multi-valued
    -   dual names found (to be handled in feature engineering phase)
-   approx_cost:
    -   replaced null by 0 (will use central tendency in fe phase)
    -   removed separators
-   menu_item:
    -   replaced '[]' by Not Provided
-   
# Gender classification task
## 1. Potential problems
**1.1 Small dataset**

Such small dataset might not represent the general population, for example, it is possible that the real target distribution is very different from the observed dataset (a ratio of men and women among our customers in fact is not 70/30).

**1.2 High-cardinality category features**

In case of a small dataset it could be a problem because some categories contain a tiny amount of related observations (frequency of category "Luxury cars" of the feature "Ad category" is 17 or binary variable Click has only 18 cases of value 1). It could bring a noise to the model in case of an absence of careful treatment of such cases.

Also on inference there is a high probability of getting a new category in test observation. It is important to take into account such cases.

**1.3 Presence of NaN feature values**

It would require a treatment of such values during model training and inference both, because some models don't handle it from the box.

## 2. Feature engineering
The main instument for finding the most important features would be a measuring classification metrics on a n-fold (n is 3 or 5) cross validaion. The metric would be an accuracy, because 70/30 class imbalance is not critical.

I would generate several features from the orginal features and measure metrics values on all possible subsets of feature sets (it's ok because the number of features at the moment is not huge, in other case one would consider such techniques as SHAP or permutation importance).

Let's look at original features and think if it possible to make it more informative and stable for the model:

**device_name**
It would be nice to extract a name of a device owner and a device using NLP techniques. Then one can use lists of male and female names in different countries and map a gender to the name, so we can create a binary feature "is_male_name". Also created feature "device_type" could be helpful.

**app_category**
Most observations belong to the most popular categories. For purposes of reducing noise I would try to combine all other categories to a created "Other" category (also NaN would be considered here).

**ad_category**
Here I would also try to combine unpopular categories. Because here we have more categories, we could combine it by groups, for example, categories Clothing, Beauty, Jewelry to group "Appearance", Beer and Wines, Restaurants to "Gastronomy" and so on.

**interaction_with_app**
It could be a useful feature. One can generate some statistics like "how much time the user spends using app from beauty category", "how much time user spends using apps in average"

**click**
This featury likely to be removed entirely because it mostly contains only one value (zero)

## 3. Model
I would like to try linear logistic regression at first, because dataset is small so I would rely also on an understanding of business domain, in that case it is quite helpful that linear mode is interpretable.

## Advantages
- interpretability
- fast training and inference

## Disadvantages
- can't handle nonlinear dependencies
- requires one-hot encoding of categorical features
- requires scaling continious feature values

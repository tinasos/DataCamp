#When you created your first decision tree the default arguments for max_depth and min_samples_split were set to None. This means that no limit on the depth of your tree was set. That's a good thing right? Not so fast. We are likely overfitting. This means that while your model describes the training data extremely well, it doesn't generalize to new data, which is frankly the point of prediction. Just look at the Kaggle submission results for the simple model based on Gender and the complex decision tree. Which one does better?

#Maybe we can improve the overfit model by making a less complex model? In DecisionTreeRegressor, the depth of our model is defined by two parameters: - the max_depth parameter determines when the splitting up of the decision tree stops. - the min_samples_split parameter monitors the amount of observations in a bucket. If a certain threshold is not reached (e.g minimum 10 passengers) no further splitting can be done.

#By limiting the complexity of your decision tree you will increase its generality and thus its usefulness for prediction!

#Instructions
#Include the Siblings/Spouses Aboard, Parents/Children Aboard, and Embarked features in a new set of features.
#Fit your second tree my_tree_two with the new features, and control for the model compelexity by toggling the max_depth and min_samples_split arguments.

# Create a new array with the added features: features_two
features_two = train[["Pclass","Age","Sex","Fare", "SibSp", "Parch", "Embarked"]].values

#Control overfitting by setting "max_depth" to 10 and "min_samples_split" to 5 : my_tree_two
max_depth = 10
min_samples_split = 5
my_tree_two = tree.DecisionTreeClassifier(max_depth = 10, min_samples_split = 5, random_state = 1)
my_tree_two = my_tree_two.fit(features_two, target)

#Print the score of the new decison tree
print(my_tree_two.score(features_two, target))

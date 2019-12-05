from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
import sklearn.model_selection
import sklearn.metrics


 using k-fold to fit the model
def Kfold_scores(x_train_data, y_train_data, kfoldnum , c_array):
    """
    using k-fold cross validation to fit the model
    kfoldnum - the number of k in cross validation
    c_array - is the learning rate (hpyer parameter)
    """
    fold = StratifiedKFold(kfoldnum, random_state=None, shuffle=False)  # define K-Fold

    results_table = pd.DataFrame(index = range(len(c_array),3), columns = ['C_parameter','Mean recall score', 'Mean precision score'])
    results_table['C_parameter'] = c_array

    # the k-fold will give 2 lists: train_indices = indices[0], test_indices = indices[1]
    j = 0
    for c_param in c_array:
        print('-------------------------------------------')
        print('C parameter: ', c_param)
        print('-------------------------------------------')
        print('')

        recall_accs = []
        precision_accs = []
        for iteration, indices in enumerate(fold.split(x_train_data, y_train_data),start=1):

            # Call the logistic regression model with a certain C parameter
            lr = LogisticRegression(C = c_param, penalty = 'l1')

            # Use the training data to fit the model. In this case, we use the portion of the fold to train the model
            # with indices[0]. We then predict on the portion assigned as the 'test cross validation' with indices[1]
            lr.fit(x_train_data.iloc[indices[0],:],y_train_data.iloc[indices[0]])

            # Predict values using the test indices in the training data
            y_pred_undersample = lr.predict(x_train_data.iloc[indices[1],:])

            # Calculate the recall score and append it to a list for recall scores representing the current c_parameter
            recall_acc = sklearn.metrics.recall_score(y_train_data.iloc[indices[1]],y_pred_undersample)
            recall_accs.append(recall_acc)
            
            precision_acc = sklearn.metrics.precision_score(y_train_data.iloc[indices[1]], y_pred_undersample)
            precision_accs.append(precision_acc)
            print("Iteration {}: recall score = {:.4f}, precision score = {:.4f}".format(iteration, recall_acc, precision_acc))

        # The mean value of those recall scores is the metric we want to save and get hold of.
        results_table.ix[j,'Mean recall score'] = np.mean(recall_accs)
        results_table.ix[j, 'Mean precision score'] = np.mean(precision_accs)
        j += 1
        print('')
        print('Mean recall score'.format(np.mean(recall_accs)))
        print('Mean precision score'.format(np.mean(precision_accs)))
        print('')

    best_c = results_table[results_table['Mean recall score'] == 
                               np.max(results_table['Mean recall score'])]['C_parameter']
    
    # Finally, we can check which C parameter is the best amongst the chosen.
    print('*********************************************************************************')
    print('Best model to choose from cross validation is with C parameter = ', best_c)
    print('*********************************************************************************')
    
    return (best_c)

# use function printing_Kfold_scores to find the best hyper-parameter
## notes: my computer can not afford such a big data, so I random sample data.
Kfold_scores(x_train_1.iloc[:100000], y_train_1.iloc[:100000], kfoldnum = 5, c_array = [0.01, 0.1, 1])
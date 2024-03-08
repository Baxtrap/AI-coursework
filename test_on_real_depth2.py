import pandas as pd

def apply_tree(row):
    if row['safety'] == 'high' and row['persons'] != '2':
        acceptability = 'acc'
    else:
        acceptability = 'unacc'
    row['acceptability'] = acceptability

    # row['acceptability'] = 'unacc'
def accuracy_check(correct_diagnosis, predicted_diagnosis):
    num_correct_diagnosis = 0
    for accept_correct,accept_predicted in zip(correct_diagnosis,predicted_diagnosis):
        if accept_correct == accept_predicted:
            num_correct_diagnosis += 1
    percentage_correct_diagnosis = (num_correct_diagnosis/len(predicted_diagnosis)) * 100
    print(num_correct_diagnosis,'/',len(correct_diagnosis))
    print(percentage_correct_diagnosis ,'%')

if __name__ == '__main__':
    data = pd.read_csv('training data.csv')
    correct_diagnosis = data['acceptability'].tolist()
    data.apply(apply_tree, axis=1,)
    predicted_diagnosis = data['acceptability'].tolist()
    accuracy_check(correct_diagnosis,predicted_diagnosis)
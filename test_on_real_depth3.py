import pandas as pd

def apply_tree(row):
    if row['safety'] == 'med':
        if row['persons'] == '4':
            if row['maint'] == 'vhigh':
                acceptability = 'unacc'
            else:
                acceptability = 'acc'
        elif row['persons'] == 'more':
            if row['buying'] == 'med' or row['buying'] == 'high':
                acceptability = 'unacc'
            else:
                acceptability = 'acc'
        else:
            acceptability = 'unacc'
    elif row['safety'] == 'high':
        if row['persons'] == '2':
            acceptability = 'unacc'
        else:
            if row['buying'] == 'low':
                acceptability = 'vgood'
            else:
                acceptability = 'acc'
    else:
        acceptability = 'unacc'
    row['acceptability'] = acceptability

def accuracy_check(correct_diagnosis, predicted_diagnosis):
    num_correct_diagnosis = 0
    for accept_correct,accept_predicted in zip(correct_diagnosis,predicted_diagnosis):
        if accept_correct == accept_predicted:
            num_correct_diagnosis += 1
    percentage_correct_diagnosis = (num_correct_diagnosis/len(predicted_diagnosis)) * 100
    print(num_correct_diagnosis,'/',len(correct_diagnosis))
    print(percentage_correct_diagnosis ,'%')

if __name__ == '__main__':
    data = pd.read_csv('real_deal.csv')
    correct_diagnosis = data['acceptability'].tolist()
    data.apply(apply_tree, axis=1,)
    predicted_diagnosis = data['acceptability'].tolist()
    accuracy_check(correct_diagnosis,predicted_diagnosis)


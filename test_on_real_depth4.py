import pandas as pd

def apply_tree(row):
    if row['safety'] == 'high':
        if row['persons'] == '2':
            criteria= 'unacc'
        elif row['persons'] == '4':
            if row['buying'] == 'high':
                if row['maint'] == 'vhigh':
                    criteria= 'unacc'
                else:
                    criteria= 'acc'
            elif row['buying'] == 'low':
                if row['maint'] == 'vhigh':
                    criteria= 'acc'
                else:
                    criteria= 'vgood'
            elif row['buying'] == 'med':
                if row['maint'] == 'high' or row['maint'] == 'vhigh':
                    criteria= 'unacc'
                else:
                    criteria= 'acc'
            elif row['buying'] == 'vhigh':
                if row['maint'] == 'low' or row['maint'] == 'med':
                    criteria= 'acc'
                else:
                    criteria= 'unacc'
        elif row['persons'] == 'more':
            if row['buying'] == 'high':
                if row['maint'] == 'vhigh':
                    criteria= 'unacc'
                else:
                    criteria= 'acc'
            elif row['buying'] == 'low':
                if row['maint'] == 'vhigh':
                    criteria= 'acc'
                else:
                    criteria= 'vgood'
            elif row['buying'] == 'med':
                if row['maint'] == 'low':
                    criteria= 'good'
                else:
                    criteria= 'acc'
            else:
                if row['maint'] == 'high' or row['maint'] == 'vhigh':
                    criteria= 'unacc'
                else:
                    criteria= 'acc'
    elif row['safety'] == 'low':
        criteria= 'unacc'
    elif row['safety'] == 'med':
        if row['persons'] == '2':
            criteria= 'unacc'
        elif row['persons'] == '4':
            if row['maint'] == 'high':
                if row['buying'] == 'vhigh':
                    criteria= 'unacc'
                else:
                    criteria= 'acc'
            elif row['maint'] == 'low':
                if row['buying'] == 'high':
                    criteria= 'unacc'
                elif row['buying'] == 'med':
                    criteria= 'good'
                else:
                    criteria= 'acc'
            elif row['maint'] == 'med':
                criteria= 'acc'
            else:
                criteria= 'unacc'
        elif row['persons'] == 'more':
            if row['buying'] == 'high':
                if row['doors'] == '2':
                    criteria= 'unacc'
                else:
                    criteria= 'acc'
            elif row['buying'] == 'low':
                if row['maint'] == 'high' or row['maint'] == 'vhigh':
                    criteria= 'acc'
                else:
                    criteria= 'good'
            elif row['buying'] == 'med':
                if row['lug_boot'] == 'small':
                    criteria= 'unacc'
                else:
                    criteria= 'acc'
            else:
                if row['maint'] == 'med':
                    criteria= 'acc'
                else:
                    criteria = 'unacc'
    row['acceptability'] = criteria


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
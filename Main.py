import math
import pandas as pd
from decision_tree import tree_pic

def calculate_proportions(dataframe, attribute):
    proportion = dataframe[attribute].value_counts(normalize=True).to_dict()
    return proportion

def calculate_entropy(dataframe):
    proportions = calculate_proportions(dataframe, 'acceptability')
    entropy = 0
    for proportion in proportions.values():
        entropy += proportion * math.log(proportion, 2)
    return -entropy

def determine_leaf(set):
    possible_leaves = set['acceptability'].value_counts().to_dict()
    return max(possible_leaves, key=possible_leaves.get)

def proportion_of_whole(group):
    return len(group)/len(data)

def find_best_candidate(set,entropy_before_test,attribute_names):
    best_candidate = {'attribute': attribute_names[0], 'IG': 0}
    for attribute in attribute_names:
        grouped_data = set.groupby(attribute)
        entropy_after_test = 0
        for key, group in grouped_data:
            entropy = calculate_entropy(group)
            proportion = proportion_of_whole(group)
            if entropy > 0:
                entropy_after_test += entropy * proportion
        IG = entropy_before_test - entropy_after_test
        if IG > best_candidate['IG']:
            best_candidate['attribute'] = attribute
            best_candidate['IG'] = IG
    return best_candidate


def ID3_algorythm(attribute_names, set, pathway, current_branch, depth, max_depth):
    entropy_before_test = calculate_entropy(set)
    if entropy_before_test < 0.1 or depth >= max_depth: # conditions to terminate branch
        parent_branch = current_branch
        leaf = determine_leaf(set)
        pathway = (parent_branch, leaf)
        return pathway
    if len(attribute_names) > 0:
        best_candidate = find_best_candidate(set,entropy_before_test, attribute_names)
        parent_branch = best_candidate['attribute']
        grouped_columns = set.groupby(best_candidate['attribute'])
        for key, group in grouped_columns:
            current_branch = key
            updated_attribute_names = attribute_names.copy()
            updated_attribute_names.remove(best_candidate['attribute'])
            subtree = ID3_algorythm(updated_attribute_names, group, {}, current_branch, depth + 1, max_depth)
            if isinstance(subtree, tuple):
                add = {subtree[0]: subtree[1]}
                if pathway == {}:
                    pathway[parent_branch] = {}
                    pathway[parent_branch].update(add)
                else:
                    pathway[parent_branch].update(add)
            else: #type is dict
                if pathway == {}:
                    pathway[parent_branch] = {}
                    pathway[parent_branch][current_branch] = subtree
                else:
                    pathway[parent_branch][current_branch] = subtree
        return pathway


if __name__ == '__main__':
    data = pd.read_csv('training data.csv')
    data_output = data[['acceptability']]
    data_input = data.drop('acceptability', axis=1)
    attribute_names = data_input.columns.tolist()
    pathway = {}
    max_depth = 3
    depth = 0
    decision_tree = ID3_algorythm(attribute_names, data, pathway, 'root', depth, max_depth)
    print(decision_tree)
    tree_pic(decision_tree)






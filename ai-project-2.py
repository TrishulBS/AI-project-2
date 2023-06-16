import numpy as np
import time

def forward_selection(data):
    current_set = []
    overall_precision_best = 0
    curr_feature_set = []
    
    
    i = 1
    while(i<len(data[0])):
        print("When examining the search tree at the", i, "th level")
        add_feature = None
        precision_highest = 0
        
        j=1
        while(j<len(data[0])):
            boo = False
            for ele in current_set:
                if ele == j:
                    boo=True
                    break
            if boo == False:
                print('Verifying the possiblity of adding the ', j, 'th feature')
                precision = calculate_accuracy(1, data, current_set.copy(), j)

                if precision > precision_highest:
                    precision_highest = precision
                    add_feature = j
            j+=1
        
        boo2 = False
        for ele in current_set:
            if ele == add_feature:
                boo2 = True
                break

        if boo2 == False:
            current_set.append(add_feature)

        boo3=False
        if precision_highest > overall_precision_best:
            overall_precision_best = max(overall_precision_best, precision_highest)
            boo3=True

        if boo3 == True:
            curr_feature_set = current_set.copy()

        print('We can add the feature', add_feature, 'to the current features resulting in an accuracy of', precision_highest)
        i+=1
    print('After considering all features, the resulting feature set is', curr_feature_set, 'which exhibits an accuarcy of ',overall_precision_best)

print('What dataset size do you want to use? Press 1 for small dataset or 2 for large dataset')
dataset = int(input())
print('what algorithm do you want to use? Press 1 for forward selection or 2 for backward elimination')
algorithm = int(input())

def backward_elimination(data):
    current_set = list(range(1, len(data[0])))
    overall_precision_best = 0
    curr_feature_set = []

    i = 1
    while(i<len(data[0])):
        print("When examining the search tree at the level", i)
        eliminate_feature = None
        precision_highest = 0


        j=1
        while(j<len(data[0])):
            boo = False
            for ele in current_set:
                if ele == j:
                    boo=True
                    break
            if boo == True:
                print('Verifying the possiblity of removing the ', j, 'th feature')
                precision = calculate_accuracy(2, data, current_set.copy(), j)

                if precision > precision_highest:
                    precision_highest = precision
                    eliminate_feature = j
            j+=1

        boo2 = False
        for ele in current_set:
            if ele == eliminate_feature:
                boo2 = True
                break

        if boo2 == True:
            current_set.remove(eliminate_feature)

        boo3=False
        if precision_highest > overall_precision_best:
            overall_precision_best = max(overall_precision_best, precision_highest)
            boo3=True

        if boo3 == True:
            curr_feature_set = current_set.copy()

        print('We can eliminate the feature', eliminate_feature, 'from the current features resulting in an accuracy: ', precision_highest)
        i+=1
    print('After considering all features, the resulting feature set is', curr_feature_set, 'which exhibits an accuarcy: ',overall_precision_best)

def calculate_distance(instance1, instance2, features):
    distance = 0
    
    for feature in features:
        distance += (instance1[feature] - instance2[feature])**2
    
    return distance**2

def calculate_accuracy(search_type, data, current_list, feature): 
    updated_list = list(current_list) 
    if search_type == 1: 
        updated_list.append(feature)
    else:
        updated_list.remove(feature)
        
    val = 0
    for i in range(len(data)):
        classify_label = data[i][0]
        dist_nn = float('inf')
        loc_nn = float('inf')

        for j in range(len(data)):
            if j != i:
                distance = calculate_distance(data[i], data[j], updated_list)
                boo=False
                if distance < dist_nn:
                    boo=True
                    dist_nn = distance
                if boo==True:
                    loc_nn = j
                    label_nn = data[loc_nn][0]

        if classify_label == label_nn:
            val += 1

    return val / len(data)
def get_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        data = [list(map(float, line.strip().split())) for line in lines]
        return np.array(data)


start = time.time()
if dataset == 1:
    data=get_data('CS170_small_Data__18.txt')
else:
    data=get_data('LargeData.txt')
    
if algorithm  == 1:
    forward_selection(data)
else:
    backward_elimination(data)
end = time.time()
print('Time taken was: {:.2f} seconds'.format(end-start))

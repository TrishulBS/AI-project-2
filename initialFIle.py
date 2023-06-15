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
                precision = cross_val_without_one_feature(1, data, current_set.copy(), j)

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
            curr_feature_set = current_set

        print('We can add the feature', add_feature, 'to the current features resulting in an accuracy of', precision_highest)
        i+=1
    print('After considering all features, the resulting feature set is', curr_feature_set, 'which exhibits an accuarcy of ',overall_precision_best)

print('What dataset size do you want to use? Press 1 for small dataset or 2 for large dataset')
dataset = int(input())
print('what algorithm do you want to use? Press 1 for forward selection or 2 for backward elimination')
algorithm = int(input())




start = time.time()
if dataset == 1:
    data=get_data('SmallData.txt')
else:
    data=get_data('LargeData.txt')
    
if algorithm  == 1:
    forward_selection(data)
else:
    backward_elimination(data)
end = time.time()
print('Time taken was: {:.2f} seconds'.format(end-start))

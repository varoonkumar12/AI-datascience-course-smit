Score_list=[40, 89, 90, 89, 23, 90, 50]
unique= list(set(Score_list))
unique.sort(reverse=True)
first_best=unique[0]
second_best=unique[1]
 
print("first best score is",first_best)
print("second best score is ",second_best)



def count_frequency(lst):
    freq_dict={}
    for item in lst:
        if item in freq_dict:
            freq_dict[item]+=1
        else:
            freq_dict[item]=1
    return freq_dict
sample_list=["apple","banana","apple","orange","banana","apple"]
print("frequency count:",count_frequency(sample_list))
            
    
    
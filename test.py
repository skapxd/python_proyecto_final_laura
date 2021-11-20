test_list = ['1','2','3','4','5','6','7','8','9',]


def string2ListEqualPart(string: str, equalPart: int) -> list:
    n=3
    customRange =  range(0, len(test_list), n)

    output=[test_list[i:i + n] for i in customRange]

    

    return 

string2ListEqualPart(test_list)
# # 
# from itertools import zip_longest
# test_list = ['1','2','3','4','5','6','7','8','9','10']


# def group_elements(n, iterable, padvalue='x'):
#     return zip_longest(*[iter(iterable)]*n, fillvalue=padvalue)

# print(group_elements(3,test_list).)
# # for output in group_elements(3,test_list):
# #     print(output)


# test_list = ['1','2','3','4','5','6','7','8','9','10']

# final_list= lambda test_list, x: [test_list[i:i+x] for i in range(0, len(test_list), x)]

# output=final_list(test_list, 3)

# print('The Final List is:', output)
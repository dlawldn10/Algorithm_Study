# #10/24
# #4659
# #7:11
# #7:52

# moeum = ['a', 'e', 'i', 'o', 'u']
# while True:
#     tmpstr = input()
#     if tmpstr == 'end':
#         break

#     mj_flag = ['moeum', 0, '']
#     moeum_cnt = 0
#     isAcceptable = True
#     for i in tmpstr:
#         # print(mj_flag)
#         if i in moeum:
#             moeum_cnt += 1

#             if mj_flag[2] == i:
#                 if mj_flag[2] != 'e' and mj_flag[2] != 'o':
#                     isAcceptable = False
#                     break

#             if mj_flag[0] == 'jaeum':
#                 mj_flag = ['moeum', 1, i]
#             else:
#                 mj_flag = ['moeum', mj_flag[1]+1, i]
#         else:
#             if mj_flag[2] == i:
#                 isAcceptable = False
#                 break

#             if mj_flag[0] == 'moeum':
#                 # print(mj_flag)
#                 mj_flag = ['jaeum', 1, i]
#             else:
#                 mj_flag = ['jaeum', mj_flag[1]+1, i]

            
#         if mj_flag[1] == 3:
#             isAcceptable = False
#             break

#     if moeum_cnt == 0:
#         isAcceptable = False
        
        
#     if isAcceptable:
#         print(f"<{tmpstr}> is acceptable.")
#     else:
#         # print(moeum_cnt, mj_flag, isAcceptable)
#         print(f"<{tmpstr}> is not acceptable.")


# 다른 풀이
# import re
# while 1:
#     s=input()
#     if s=='end':break
#     case1 = len(re.findall('[aeiou]',s)) != 0
#     case2 = len(re.findall('[aeiou]{3}|[^aeiou]{3}',s))==0
#     case3 = len(re.findall('([a-df-np-z])\\1',s))==0
#     if case1 and case2 and case3:
#         print(f'<{s}> is acceptable.')
#     else:
#         print(f'<{s}> is not acceptable.')





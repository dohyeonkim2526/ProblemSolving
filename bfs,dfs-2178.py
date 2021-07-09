# #1:이동가능, 0:불가능
# #(1,1)에서 출발
# import sys
# from collections import deque
# x,y=map(int, input().split())
# mat=[[0]*(y+1) for _ in range(x+1)]

# for i in range(x):
#     m=sys.stdin.readline()
#     for j in range(y):
#         mat[i+1][j+1]=int(m[j])

# def find(start,end,cnt):
#     while start!=x and end !=y:
#         if mat[start][end+1]==1:
#             if mat[start+1][end]==1:
#                 start+=1
#                 cnt+=1
#                 find(start,end,cnt)

#             elif mat[start][end+1]==1:
#                 end+=1
#                 cnt+=1
#                 find(start,end,cnt)

#         if mat[start+1][end]==1:
#             if mat[start+1][end]==1:
#                 start+=1
#                 cnt+=1
#                 find(start,end,cnt)

#             elif mat[start][end+1]==1:
#                 end+=1
#                 cnt+=1
#                 find(start,end,cnt)
#         ans.append(cnt)
# ans=[]
# find(1,1,0)
# print(ans)



# #deque.popleft()
# # def find(start):
# #     for i in range(1,y+1):
# #         if mat[i][start]==1:
# #             queue.append(i)

# # def find(start,cnt): 
# #     queue=deque([start]) 
    
# #     while queue:
# #         cnt+=1
# # #         start=queue.popleft()
# # #         check.append(start)
# # #         for i in range(1,x+1):
# # #             if mat[i][start]==1 and i not in check:
# # #                 queue.append(i)

# # def find(start,end,cnt):
    
# #     #반복문 조건
# #     while start!=4 and end!=6:
# #         cnt+=1
# #         if mat[start][end]==0:
# #             continue

# #         if mat[start+1][end]==1:
# #             start+=1
# #             find(start,end,cnt)
# #         else:
# #             end+=1
# #             find(start,end,cnt)
# #         if mat[start][end+1]:
# #             end+=1
# #             find(start,end,cnt)
# #         else:
# #             start+=1
# #             find(start,end,cnt)
# #     return cnt

# # find(1,1,0)

# # for m in mat:
# #     for _ in m:
# #         print(_, end=' ')
# #     print()
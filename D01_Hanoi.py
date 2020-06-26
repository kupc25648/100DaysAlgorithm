
'''
Hanoi Tower problem
 (N=3)
  [|]       |     |
 [ | ]      |     |
[  |  ]     |     |

Objective

     |     |       [|]
     |     |      [ | ]
     |     |     [  |  ]

Algorithm
1 [recursively] move N-1 disks from left to middle
2 move largest disk from left to right
3 [recursively] move N-1 disks from middle to right
'''


height = 3

def hanoi(height, left='left', right='right', middle='middle'):
    if height:
        hanoi(height-1,left,middle,right)
        print(height,left,'=>',right)
        hanoi(height-1,middle, right, left)

hanoi(height)

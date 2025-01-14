
debug = False

def print_game_config(G, generation=-1, debug=True):
    if not debug:
        return
    n = len(G)  
    for i in range(n): 
        print(*G[i], sep=', ')
    print(f"End of generation {generation}")

def create_empty_grid(n):
    # Create an empty grid G of size n * n
    G=[[0]*n for num in range(0,n)]
   
    return G

def update_grid_with_input(G, val):
    x, y=input().split()
    if x!='-' and y!='-':
        while 0<=int(x)<n and 0<=int(y)<n:
            G[int(x)][int(y)]=val
            x, y=input().split()
            if x=='-' and y=='-':
                break
    return G

def cal_neighbor_mean(x, y, G):
    # Calculate the mean value of neighbors for cell (x, y) in G
    conlist=[]
    if x+1<=n-1:
        conlist.append(G[x+1][y])
        if y-1>=0:
            conlist.append(G[x+1][y-1])
    if y+1<=n-1:
        conlist.append(G[x][y+1])
        if x-1>=0:
            conlist.append(G[x-1][y+1])
    if x+1<=n-1 and y+1<=n-1:
        conlist.append(G[x+1][y+1])
    if x-1>=0:
        conlist.append(G[x-1][y])
    if y-1>=0:
        conlist.append(G[x][y-1])
    if x-1>=0 and y-1>=0:
        conlist.append(G[x-1][y-1])
    sum1=0
    for num in conlist:
        sum1+=num
    mean=sum1/len(conlist)

   
    return mean

def update_game_config(G):
    # Update G to its next generation nextG
    nextG=[[0]*n for num in range(0,n)]
    for num1 in range(0,n):
        for num2 in range(0,n):
            mean=cal_neighbor_mean(num1, num2, G)
            nextG[num1][num2]=G[num1][num2]+round(mean/2)


    return nextG 


def input_game_config(n):
    # Input the game config
    G = create_empty_grid(n)
    print("Please input the locations of the angel cells: ")
    update_grid_with_input(G, 20)
    print("Please input the locations of the devil cells: ")
    update_grid_with_input(G, -20)
    return G


if __name__ =='__main__':
    n = int(input("Input the size of the grid: "))
    m = int(input("Input the number of generations: "))

    G = input_game_config(n)
    print_game_config(G, -1, debug=debug)
    for i in range(m):
        G = update_game_config(G)
        print_game_config(G, i, debug=debug)
    print(G)
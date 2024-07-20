if __name__ == '__main__':
    n=int(input())
    m=[]
    commands={}
    for i in range(n):
        commands[i]=input().split()
    for k,v in commands.items():
        if v[0] == 'insert':
            #print('peform ',v[0])
            id=int(v[1])
            val=int(v[2])

            m.insert(id,val)
        
        elif v[0] == 'print':
            #print('perform ',v[0])
            print(m)
        elif v[0] == 'remove':
            #print('peform ',v[0],'     ',v[1])
            val=int(v[1])
            if val in m:
                m.remove(val)    
        elif v[0] == 'append':
            #print('perform ',v[0])
            val=int(v[1])
            m.append(val)
        elif v[0] == 'sort':
            #print('perform ',v[0])
            m.sort() 
        elif v[0] == 'pop':
            #print('perform ',v[0])
            m.pop()
        elif v[0] == 'reverse':
            m.reverse()

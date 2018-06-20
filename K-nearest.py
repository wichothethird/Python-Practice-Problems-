from math import sqrt

def main():

    print(getKnearest())
    


def getKnearest():
    
    lista = [(-21,67),(1,2),(2,5),(-4,4),(-1,2),(7,3),(5,7)]
    center = (0,0)
    knearest = []
    answer = []
    
    counter = 0 
    while(counter!=len(lista)):
        
        dist = FindDistance(center,lista[counter])
        print(dist)
        knearest.append([dist,lista[counter],counter])
        counter=counter+1
    
    


    

    answer.append(min(knearest)[1])
    del knearest[min(knearest)[2]]
    answer.append(min(knearest)[1])
    
    return answer 
    



def FindDistance(center,point):
   
    x = ((point[0]-center[0])**2 + (point[1]-center[1])**2)
    
    distance =sqrt(x)
    return distance
    



if __name__=="__main__":
    main()

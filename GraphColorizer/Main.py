import csv                                                              #importing csv related library for reading,writing csvs
import random
from random import seed
from os.path import exists

if __name__=='__main__':
    
    path=input("Enter File Name OR Give Path: ")                       #asking user for path to csv file
    fileexists = exists(path)                                          #checking if path is valid or not
  
    while not fileexists:                                              #if invalid path
        path=input("Enter File Name OR Give Path: ")                   #asking again if path is invalid 
        fileexists = exists(path)                                      #checking if path is valid or not
      
    print("\nThe File Name OR Path Is "+path)                          #printing
    print("Reading File...")                                           #printing
    print("Processing...")                                             #printing
    print("Printing File Data...\n")                                   #printing
                               
    Edge=["0"]*15                                                      #variables/array declaration & initialization
    EdgeColors=[0]*15
    VertexColors=[0]*15
    Merged=["0"]*20
    Vertex= []*15
    VertexA=["0"]*15
    VertexB=["0"]*15

    with open(path) as csvfile:                                         #opening csv file
        csvread = csv.reader(csvfile, delimiter='"')                    #reading csv
        linecount = 0
        count=0  
        for row in csvread:                                             #iterating via each row
            if linecount == 0:                                          #if line=1, i.e., first row or header
                print(f' {" ".join(row)}')                              #printing csv headers
                linecount += 1                                          #incrementing line count
            else:
                print(f'    {row[0]}        {row[1]}       {row[3]}')   #printing rows
                Edge[count]=row[3]

                word = row[0]
                filter = ''.join([chr(i) for i in range(1, 32)])
                words=word.translate(str.maketrans('', '', filter))

                VertexA[count]=words
                VertexB[count]=row[1]
                count+=1                                                #incrementing
                linecount += 1                                          #incrementing

    Merged=VertexA+VertexB                                              #merging the VertexA & VertexB
    Vertex=list(dict.fromkeys(Merged))                                  #getting unique vertex'es

    for i in range(0, len(VertexA)): 
        VertexA[i]=VertexA[i][1:len(VertexA)]
        VertexB[i]=VertexB[i][1:len(VertexB)]

    with open('vertex-coloring.csv', 'w', newline='') as vertexfile:    #creating new csv file
        print("\nCreating 'vertex-coloring.csv'...")                    #printing
        print("Writing To 'vertex-coloring.csv'...")                    #printing
        vertexfields = ['vertex-id', 'vertex-color']                    #file headers
        vertexwriter = csv.writer(vertexfile)                           #writing to file
        vertexwriter.writerow(vertexfields)                             #writing headers to file
        seed(1)
        for i in range(0, len(Vertex)):                                 #looping through vertex'es
            VertexColors[i]=random.randint(0,3)
            vertexdata=[Vertex[i],VertexColors[i]]                      #edge file data
            vertexwriter.writerow(vertexdata)                           #writing to file
    vertexfile.close()                                                  #closing file
    print("Closing 'vertex-coloring.csv'...")                           #printing

    with open('edge-coloring.csv', 'w', newline='') as edgefile:        #creating new csv file
        print("\nCreating 'edge-coloring.csv'...")                      #printing
        print("Writing To 'edge-coloring.csv'...")                      #printing
        edgefields = ['edge-id', 'edge-color']                          #file headers
        edgewriter = csv.writer(edgefile)                               #writing to file
        edgewriter.writerow(edgefields)                                 #writing headers to file
        seed(1)
        for i in range(0, len(Edge)):                                   #looping through edge's
            EdgeColors[i]=random.randint(0,3)
            edgedata=[Edge[i],EdgeColors[i]]                            #edge file data
            edgewriter.writerow(edgedata)                               #writing to file
    edgefile.close()                                                    #closing file
    print("Closing 'edge-coloring.csv'...")                             #printing

    print("\nProgram Ended...")                                         #printing


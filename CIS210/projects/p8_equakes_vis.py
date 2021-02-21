'''
CIS 210 - World Wide Earthquake Watch

Author: Luke Vandecasteele

Credits: Class notes, my dad

This function analyzes date from earthquakes
across the globe, plots the date on a map, and
creates clusters based off latitude and longitude
coordinates.
'''

import math
import random
import turtle

breakpoint()

def readFile(filename,headerlines):
    '''
    (string,int) -> dictionary

    This function takes in a file
    name in the form of a string
    (filename) then reads the file
    and sorts the data into a dictionary.
    It also skips a number of lines
    (headerlines) for a header.

    >>> readFile('equake_test.csv',1)
    {1: [-178.4753, -33.6142], 2: [74.6387, 35.6305],
    3: [74.6175, 35.6024], 4: [56.5402, 27.3836], 5: [142.8263, 27.8431],
    6: [11.3306, -52.8602]}

    '''
    datafile = open(filename)
    datadict = {}
    key = 0

    for aline in range(headerlines):
        datafile.readline()

    for aline in datafile:
        items = aline.split(',')
        key += 1
        lat = float(items[1])
        lon = float(items[2])
        datadict[key] = [lon,lat]

    return datadict

equakes_datadict_example = readFile('equake_test.csv',1)
equakes_datadict = readFile('equakes_world_50f_2019.csv',1)

def euclidD(point1,point2):
    '''
    (list,list) -> float

    This function computes the distance
    between two given points in the form
    of lists (point1 and point2).

    >>> euclidD([0,3],[4,0])
    5.0
    '''

    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        total = total + diff

    euclidDistance = math.sqrt(total)
    return euclidDistance

euclidD_test = euclidD([0,3],[4,0])

def createCentroids(k, datadict):
    '''
    (int,dictionary) -> list (list of lists)

    This funtion picks (k) random keys
    from a dictionary and then puts the lists
    associated with each key into a list
    and returns a list.

    >>> createCentroids(3,equakes_datadict_example)
    [[11.3306, -52.8602], [-178.4753, -33.6142], [87.155675, 31.6149]]

    '''

    centroids = []
    centroidCount = 0
    centroidKeys = []

    while centroidCount < k:
        rkey = random.randint(1,len(datadict))
        if rkey not in centroidKeys:
            centroids.append(datadict[rkey])
            centroidKeys.append(rkey)
            centroidCount = centroidCount + 1

    return centroids

createCentroids_test = createCentroids(3,equakes_datadict_example)
myCentroids = createCentroids(3,equakes_datadict)

def createClusters(k,centroids,datadict,repeats):
    '''
    (int,list of lists,dictionary,int) -> list of lists

    This function takes a dictionary of points
    (datadict) and (centroids) and averages out which points are
    closest to each centroid using the distance formula. The for loop
    will go through a (repeat) amount of times to average it out,
    and will calculate it based off of k clusters.

    Calls createCentroids and euclidD

    >>> createClusters(3,createCentroids_test,equakes_datadict_example,3)
    [[6], [1], [2, 3, 4, 5]]

    '''

    for apass in range(repeats):
        #print('***PASS' ,apass, '****')
        clusters = []
        for i in range(k):
            clusters.append([])

        for akey in datadict:
            distances = []
            for clusterIndex in range(k):
                dist = euclidD(datadict[akey],centroids[clusterIndex])
                distances.append(dist)

            mindist = min(distances)
            index = distances.index(mindist)

            clusters[index].append(akey)


        dimensions = len(datadict[1])
        for clusterIndex in range(k):
            sums = [0]*dimensions
            for akey in clusters[clusterIndex]:
                datapoints = datadict[akey]
                for ind in range(len(datapoints)):
                    sums[ind] = sums[ind] + datapoints[ind]
            for ind in range(len(sums)):
                clusterLen = len(clusters[clusterIndex])
                if clusterLen != 0:
                    sums[ind] = sums[ind]/clusterLen

            centroids[clusterIndex] = sums

        #for c in clusters:
            #print('Cluster')
            #for key in c:
                #print(datadict[key], end=' ')
                #print()

    return clusters

equake_clusters_test = createClusters(3,createCentroids_test,equakes_datadict_example,3)

def visualizeQuakes(datafile):
    '''
    (string) -> None

    This fucntion uses a string (datafile)
    and will plot all the points of the datafile
    on a map and will cluster the points by color
    according to centroids
    '''
    datadict = readFile(datafile,1)
    quakeCentroids = createCentroids(6, datadict)
    clusters = createClusters(6, quakeCentroids, datadict, 7)

    turtle.speed()
    quakeT =  turtle.Turtle()
    quakeWin = turtle.Screen()
    quakeWin.bgpic('worldmap1800_900.gif')
    quakeWin.screensize(1800,900)

    wFactor = (quakeWin.screensize()[0]/2)/180
    hFactor = (quakeWin.screensize()[1]/2)/90

    quakeT.hideturtle()
    quakeT.up()

    colorlist = ['red','purple', 'blue', 'orange', 'cyan', 'yellow']

    for clusterIndex in range(6):
        quakeT.color(colorlist[clusterIndex])
        for akey in clusters[clusterIndex]:
            lon = datadict[akey][0]
            lat = datadict[akey][1]
            quakeT.goto(lon*wFactor, lat*hFactor)
            quakeT.dot()
    quakeWin.exitonclick()
    return None

def main():
    '''
    Main program driver function
    '''
    display_visualizeQuakes = visualizeQuakes('equakes_world_50f_2019.csv')
    return None

main()

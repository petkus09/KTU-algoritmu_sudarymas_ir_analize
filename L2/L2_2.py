#!/usr/bin/env python

import math
import random
import time
from random import randint
const = 0;

class City:
   def __init__(self, x=None, y=None):
      global const
      self.x = None
      self.y = None
      const += 2
      if x is not None:
         self.x = x
         const += 1
      else:
         self.x = int(random.random() * 200)
         const += 1
      if y is not None:
         self.y = y
         const += 1
      else:
         self.y = int(random.random() * 200)
         const += 1
   
   def getX(self):
      return self.x
   
   def getY(self):
      return self.y
   
   def distanceTo(self, city):
      global const
      xDistance = abs(self.getX() - city.getX())
      yDistance = abs(self.getY() - city.getY())
      distance = math.sqrt( (xDistance*xDistance) + (yDistance*yDistance) )
      const += 3
      return distance
   
   def __repr__(self):
      return str(self.getX()) + ", " + str(self.getY())


class TourManager:
   destinationCities = []
   
   def addCity(self, city):
      self.destinationCities.append(city)
   
   def getCity(self, index):
      return self.destinationCities[index]
   
   def numberOfCities(self):
      return len(self.destinationCities)


class Tour:
   def __init__(self, tourmanager, tour=None):
      global const
      self.tourmanager = tourmanager
      self.tour = []
      self.fitness = 0.0
      self.distance = 0
      const += 4
      if tour is not None:
         self.tour = tour
         const += 1
      else:
         for i in range(0, self.tourmanager.numberOfCities()):
            self.tour.append(None)
            const += 1
   
   def __len__(self):
      return len(self.tour)
   
   def __getitem__(self, index):
      return self.tour[index]
   
   def __setitem__(self, key, value):
      self.tour[key] = value
   
   def __repr__(self):
      global const
      geneString = "|"
      const += 1
      for i in range(0, self.tourSize()):
         geneString += str(self.getCity(i)) + "|"
         const += 1
      return geneString
   
   def generateIndividual(self):
      global const
      for cityIndex in range(0, self.tourmanager.numberOfCities()):
         self.setCity(cityIndex, self.tourmanager.getCity(cityIndex))
         const += 1
      random.shuffle(self.tour)
   
   def getCity(self, tourPosition):
      return self.tour[tourPosition]
   
   def setCity(self, tourPosition, city):
      global const
      self.tour[tourPosition] = city
      self.fitness = 0.0
      self.distance = 0
      const += 3
   
   def getFitness(self):
      global const
      if self.fitness == 0:
         self.fitness = 1/float(self.getDistance())
         const += 1
      return self.fitness
   
   def getDistance(self):
      global const
      if self.distance == 0:
         tourDistance = 0
         const += 1
         for cityIndex in range(0, self.tourSize()):
            fromCity = self.getCity(cityIndex)
            destinationCity = None
            const += 2
            if cityIndex+1 < self.tourSize():
               destinationCity = self.getCity(cityIndex+1)
               const += 1
            else:
               destinationCity = self.getCity(0)
               const += 1
            tourDistance += fromCity.distanceTo(destinationCity)
            const += 1
         self.distance = tourDistance
         const += 1
      return self.distance
   
   def tourSize(self):
      return len(self.tour)
   
   def containsCity(self, city):
      return city in self.tour


class Pop:
   def __init__(self, tourmanager, populationSize, initialise):
      global const
      self.tours = []
      for i in range(0, populationSize):
         self.tours.append(None)
         const += 1
      
      if initialise:
         for i in range(0, populationSize):
            newTour = Tour(tourmanager)
            newTour.generateIndividual()
            self.saveTour(i, newTour)
            const += 3
      
   def __setitem__(self, key, value):
      self.tours[key] = value
   
   def __getitem__(self, index):
      return self.tours[index]
   
   def saveTour(self, index, tour):
      self.tours[index] = tour
   
   def getTour(self, index):
      return self.tours[index]
   
   def getFittest(self):
      global const
      fittest = self.tours[0]
      const += 1
      for i in range(0, self.popSize()):
         if fittest.getFitness() <= self.getTour(i).getFitness():
            fittest = self.getTour(i)
            const += 1
      return fittest
   
   def popSize(self):
      return len(self.tours)


class GA:
   def __init__(self, tourmanager):
      global const
      self.tourmanager = tourmanager
      self.mutationRate = 0.015
      self.tournamentSize = 5
      self.elitism = True
      const += 4
   
   def evolvePop(self, pop):
      global const
      newPopulation = Pop(self.tourmanager, pop.popSize(), False)
      elitismOffset = 0
      const += 2
      if self.elitism:
         newPopulation.saveTour(0, pop.getFittest())
         elitismOffset = 1
         const += 2
      
      for i in range(elitismOffset, newPopulation.popSize()):
         parent1 = self.tournamentSelection(pop)
         parent2 = self.tournamentSelection(pop)
         child = self.crossover(parent1, parent2)
         newPopulation.saveTour(i, child)
         const += 4
      
      for i in range(elitismOffset, newPopulation.popSize()):
         self.mutate(newPopulation.getTour(i))
      
      return newPopulation
   
   def crossover(self, parent1, parent2):
      global const
      child = Tour(self.tourmanager)
      
      startPos = int(random.random() * parent1.tourSize())
      endPos = int(random.random() * parent1.tourSize())
      const += 3
      
      for i in range(0, child.tourSize()):
         if startPos < endPos and i > startPos and i < endPos:
            child.setCity(i, parent1.getCity(i))
            const += 1
         elif startPos > endPos:
            if not (i < startPos and i > endPos):
               child.setCity(i, parent1.getCity(i))
               const += 1
      
      for i in range(0, parent2.tourSize()):
         if not child.containsCity(parent2.getCity(i)):
            for ii in range(0, child.tourSize()):
               if child.getCity(ii) == None:
                  child.setCity(ii, parent2.getCity(i))
                  const += 1
                  break
      
      return child
   
   def mutate(self, tour):
      global const
      for tourPos1 in range(0, tour.tourSize()):
         if random.random() < self.mutationRate:
            tourPos2 = int(tour.tourSize() * random.random())
            
            city1 = tour.getCity(tourPos1)
            city2 = tour.getCity(tourPos2)
            
            tour.setCity(tourPos2, city1)
            tour.setCity(tourPos1, city2)
            const += 5
   
   def tournamentSelection(self, pop):
      global const
      tournament = Pop(self.tourmanager, self.tournamentSize, False)
      const += 1
      for i in range(0, self.tournamentSize):
         randomId = int(random.random() * pop.popSize())
         tournament.saveTour(i, pop.getTour(randomId))
         const += 2
      fittest = tournament.getFittest()
      const += 1
      return fittest

def main(amount):
    global const
    const = 0;
    time1 = time.time()
    print "-----------------------\n"
    print "Miestu skaicius: " + str(amount) + "\n"
    tourmanager = TourManager()
    const += 2
    for i in range(0, amount):
        tourmanager.addCity(City(randint(1, 1000), randint(1, 1000)))
        const += 1
   
    pop = Pop(tourmanager, 50, True);
    print "Pradinis atstumas: " + str(pop.getFittest().getDistance())
   
    ga = GA(tourmanager)
    pop = ga.evolvePop(pop)
    const += 4
    for i in range(0, 100):
        pop = ga.evolvePop(pop)
        const += 1
   
    print "Pabaigta"
    print "Galutinis atstumas: " + str(pop.getFittest().getDistance())
    print "Sprendimas:"
    print pop.getFittest()
    const += 4
    time2 = time.time()
    skirtumas = time2 - time1
    print "Bendras uztruktas laikas sekundemis: %(time)s" %{'time': skirtumas}
    print "Eiluciu kiekis: %(const)s" %{'const': const}

if __name__ == '__main__':
   main(20)
   main(40)
   main(60)
   main(80)
   main(120)
   main(140)
   main(160)
   main(180)
   main(200)
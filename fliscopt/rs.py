import sys
import os 
sys.path.append(os.getcwd())
import time
from abc import ABCMeta
from .utils.util import plot_scores, print_schedule, read_file
from .base_algorithm import FlightAlgorithm

import random
from .fitness import *


class RandomSearch(FlightAlgorithm, metaclass=ABCMeta):
    def __init__(self, domain=domain['domain'], fitness_function=fitness_function, seed=random.randint(10, 100),
                 seed_init=True, init=None,max_time=1000,epochs=100) -> None:
        super().__init__(domain, fitness_function, seed, seed_init, init,max_time)        
        self.epochs = epochs
        self.best_cost=sys.maxsize
        self.best_solution=0.0

    """ Flight Algorithm implemented
       Args:
        domain (list): List containing the upper and lower bound.i.e domain of our inputs
        fitness_function (function): This parameter accepts a fitness function of given optimization problem.
        seed (int,optional): Set the seed value of the random seed generator. Defaults to random integer value.
        seed_init(bool,optional): True set's the seed of only population init generator, False sets all generators
        init (list, optional): List for initializing the initial solution. Defaults to [].
        epochs (int, optional): Number of times the algorithm runs. Defaults to 100.
    Returns:
        list: List containing the best_solution,
        int: The final cost after running the algorithm,
        list: List containing all costs during all epochs.
        int: The number of function evaluations(NFE) after running the algorithm
        int: Seed value used by random generators.
    """

        
        
    def get_base(self) -> str:
        pass
    """Args:
        domain (list): List containing the upper and lower bound.i.e domain of our inputs
        fitness_function (function): This parameter accepts a fitness function of given optimization problem.
        seed (int,optional): Set the seed value of the random seed generator. Defaults to random integer value.
        seed_init(bool,optional): True set's the seed of only population init generator, False sets all generators
        init (list, optional): List for initializing the initial solution. Defaults to [].
        epochs (int, optional): Number of times the algorithm runs. Defaults to 100.
    Returns:
        list: List containing the best_solution,
        int: The final cost after running the algorithm,
        list: List containing all costs during all epochs.
        int: The number of function evaluations(NFE) after running the algorithm
        int: Seed value used by random generators.
    """
    
    def get_name(self) -> str:
     """Args:
        domain (list): List containing the upper and lower bound.i.e domain of our inputs
        fitness_function (function): This parameter accepts a fitness function of given optimization problem.
        seed (int,optional): Set the seed value of the random seed generator. Defaults to random integer value.
        seed_init(bool,optional): True set's the seed of only population init generator, False sets all generators
        init (list, optional): List for initializing the initial solution. Defaults to [].
        epochs (int, optional): Number of times the algorithm runs. Defaults to 100.
    Returns:
        list: List containing the best_solution,
        int: The final cost after running the algorithm,
        list: List containing all costs during all epochs.
        int: The number of function evaluations(NFE) after running the algorithm
        int: Seed value used by random generators.
    """

        return self.__class__.__name__

 
        
    def run(self,domain,fitness_function,seed):
            self.__init__(domain,fitness_function,seed,self.seed_init, self.init,self.max_time)
            scores = []
            nfe = 0
            if len(self.init) > 0:
                solution = self.init
            else:
                solution = [self.r_init.randint(self.domain[i][0], self.domain[i][1])
                            for i in range(len(self.domain))]

            self.start_time=time.time()
    """ Args:
        domain (list): List containing the upper and lower bound.i.e domain of our inputs
        fitness_function (function): This parameter accepts a fitness function of given optimization problem.
        seed (int,optional): Set the seed value of the random seed generator. Defaults to random integer value.
        seed_init(bool,optional): True set's the seed of only population init generator, False sets all generators
        init (list, optional): List for initializing the initial solution. Defaults to [].
        epochs (int, optional): Number of times the algorithm runs. Defaults to 100.
    Returns:
        list: List containing the best_solution,
        int: The final cost after running the algorithm,
        list: List containing all costs during all epochs.
        int: The number of function evaluations(NFE) after running the algorithm
        int: Seed value used by random generators.
    """

            for i in range(self.epochs):
                if i != 0:
                    solution = [random.randint(self.domain[i][0], self.domain[i][1])
                                for i in range(len(self.domain))]
                if not self.fitness_function.__name__ == 'fitness_function':
                    cost = self.fitness_function(solution)
                else:
                    cost = self.fitness_function(solution, 'FCO')
                nfe += 1
                if cost < self.best_cost:
                    self.best_cost = cost
                    self.best_solution = solution
                scores.append(self.best_cost)
                if time.time()-self.start_time>self.max_time:
                    return self.best_solution, self.best_cost, scores, nfe, self.seed
            return self.best_solution, self.best_cost, scores, nfe, self.seed
    

if __name__ == '__main__':
    read_file('flights.txt')
    rs=RandomSearch(max_time=0.00001)  #def run():
    soln, cost, scores, nfe, seed=rs.run(domain=domain['domain'],fitness_function=fitness_function,seed=5)
    #plot_scores(scores,rs.get_name(),fname='flight_scheduling',save_fig=False)
    #print_schedule(soln,'FCO')

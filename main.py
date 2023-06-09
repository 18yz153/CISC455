import random
import numpy
import itertools
import matplotlib.pyplot as plt

import initialization
import evaluation
import parent_selection
import recombination
import mutation
import survivor_selection

#create fake orders
class create_orders():
    def __init__(self,storesize,ordersize):
        self.storesize = storesize
        self.ordersize = ordersize
        self.store = self.genstore()
        self.orders =  self.genorders()
    def genstore(self):
        stores = []
        for i in range(0,self.storesize):
            storexy = (random.randint(0,100),random.randint(0,100))
            stores.append(storexy)
        return stores

    def genorders(self):
        orders = []
        for i in range(0,self.ordersize):
            keep_running = True
            while keep_running:
                deliveryxy = (random.randint(0,100),random.randint(0,100))
                if deliveryxy not in self.store:
                    keep_running = False
            orders.append([random.sample(self.store,1)[0],deliveryxy])
        return orders
   
def ga(survivor,routere,routesurvivor):
    #use random seed to make sure random orders are the same every time
    random.seed(42)
    numpy.random.seed(42)
    O = create_orders(7,20)
    stores = O.store
    orders = O.orders
    random.seed()
    numpy.random.seed()
    #set parameters
    workers = 3
    pop_size = 60
    mating_pool_size = int(pop_size*0.5) # has to be even
    tournament_size = 4
    xover_rate = 0.9
    mut_rate = 0.9
    gen_limit = 30

    #initialize the population
    population = initialization.permutation(pop_size, workers, orders)
    gen = 0
    #initialize the result we need to save
    fitness=[]
    all_fitness = dict()
    all_solution = []
    his = []
    routehis = []
    for i in range (0, pop_size):
        fitness.append(evaluation.fitness_fun(population[i],orders,all_fitness,all_solution,routehis,routere,routesurvivor))
    print("generation", gen, ": best fitness", min(fitness), "\taverage fitness", sum(fitness)/len(fitness))

    while gen < gen_limit:
        parents_index = parent_selection.tournament(fitness, mating_pool_size, tournament_size)
        random.shuffle(parents_index)
        offspring =[]
        offspring_fitness = []
        i= 0
        while len(offspring) < mating_pool_size:
        
            if random.random() < xover_rate:            
                off1,off2 = recombination.permutation_cut_and_crossfill(population[parents_index[i]], population[parents_index[i+1]])
            else:
                off1 = population[parents_index[i]].copy()
                off2 = population[parents_index[i+1]].copy()
                
            if random.random() < mut_rate:
                off1 = mutation.permutation_swap(off1)
            if random.random() < mut_rate:
                off2 = mutation.permutation_swap(off2)
        
            offspring.append(off1)
            offspring_fitness.append(evaluation.fitness_fun(off1,orders,all_fitness,all_solution,routehis,routere,routesurvivor))
            offspring.append(off2)
            offspring_fitness.append(evaluation.fitness_fun(off2,orders,all_fitness,all_solution,routehis,routere,routesurvivor))
            i = i+2 
        if survivor == 'mu+lambda':
            population, fitness = survivor_selection.mu_plus_lambda(population, fitness, offspring, offspring_fitness,int(0.8*pop_size),int(0.2*pop_size))
        elif survivor == 'sus':
            population, fitness = survivor_selection.sus(population, fitness, offspring, offspring_fitness)
        gen = gen + 1  # update the generation counter
        his.append(min(fitness))
        print("generation", gen, ": best fitness", min(fitness), "average fitness", sum(fitness)/len(fitness))
    k = 0
    #plot and save the route
    for i in range (0, len(all_solution)):
        if all_solution[i][0] == min(fitness):
            print("best solution", k, all_solution[i][1], all_solution[i][0])
            k = k+1
            fig, ax = plt.subplots()
            for i, all_solution[i][1] in enumerate(all_solution[i][1]):
                x, y = zip(*all_solution[i][1])
                label = f'Route {i+1}'
                ax.plot(x, y, label=label)
            ax.set_title('All routes '+ survivor +' '+routere + ' '+ routesurvivor)
            ax.legend()
            fig.savefig('All routes '+ survivor +' '+routere + ' '+ routesurvivor+'.png',dpi = 500)
    
    
    return his, routehis

def main():
    #define all combinations
    survivor = ['mu+lambda','sus']
    routere = ['heuristic','pmx']
    routesurvivor = ['mu+lambda','sus']

    combinations = list(itertools.product(survivor,routere, routesurvivor))

    print(combinations)
    #run and plot all result in one figure.
    allhis = []
    fig2, ax2 = plt.subplots()
    for e in combinations:
        his,routehis = ga(e[0],e[1],e[2])
        ax2.plot(range(len(his)), his, label = e[0]+' & '+e[1]+' & '+e[2])
        print(e[0]+' & '+e[1]+' & '+e[2]+': caculated '+str(len(routehis)) + ' gens')
    ax2.legend()
    ax2.set_xlabel('generations')
    ax2.set_ylabel('route distance')
    ax2.set_ylim([0, 1000])
    fig2.savefig('gen comparison.png',dpi = 500)

main()






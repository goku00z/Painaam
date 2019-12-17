#include<bits/stdc++.h>
using namespace std;
typedef struct
{
string arrangement;
int cost;
} individual;
typedef vector<individual*> population_type;
population_type population;
int chessBoardSize;
int initialPopulationCount=4;
int fitnessValue(string arrangement)
{
int fitness=(chessBoardSize*(chessBoardSize-1))/2; //initialize to
a solution
//removing pairs that lie on the same row and on the same diagonal
for(int i=0; i<chessBoardSize; i++)
for(int j=i+1; j<chessBoardSize; j++)
if((arrangement[i] == arrangement[j]) || (i-arrangement[i] ==
j-arrangement[j]) || (i+arrangement[i] == j+arrangement[j]))
fitness--;
return fitness;
}
individual* createNode()
{
individual *newNode = new individual;
return newNode;
}
void generatePopulation()
{
string sampleArrangement="";
individual *temp;
for(int i=1; i<=chessBoardSize; i++)
{
ostringstream ostr;
int x;
cout<<"Enter position of queen for x= "<<i<<endl;
cin>>x;
ostr<<x;
sampleArrangement += ostr.str();
}
cout<<sampleArrangement<<endl;
//adds entries to population list
for(int i=0; i<initialPopulationCount; i++)
{
random_shuffle( sampleArrangement.begin(), sampleArrangement.end());
temp = createNode();
temp->arrangement = sampleArrangement;
temp->cost = fitnessValue(sampleArrangement);
population.push_back(temp);
cout<<"Initial 4 offsprings from 1 input"<<endl;
cout<<sampleArrangement<<endl;
}
}
individual* reproduce(individual *x, individual *y)
{
individual *child = createNode();
int n = chessBoardSize;
int c = rand()%n;
child->arrangement = (x->arrangement).substr(0,c) +
(y->arrangement).substr(c,n-c+1);
child->cost = fitnessValue(child->arrangement);
return child;
}
individual* mutate(individual *child)
{
int randomQueen = rand()%(chessBoardSize)+1;
int randomPosition= rand()%(chessBoardSize)+1;
child->arrangement[randomQueen] = randomPosition+48;
return child;
}
int randomSelection()
{
int randomPos = rand()%population.size() %2;
return randomPos;
}
bool isFit(individual *test)
{
if(fitnessValue(test->arrangement)==((chessBoardSize*(chessBoardSize-1))/2))
return true;
return false;
}
bool comp(individual *a, individual*b)
{
return(a->cost > b->cost);
}
individual* GA()
{
int randomNum1,randomNum2;
individual *individualX,*individualY,*child;
bool found =0;
while(!found)
{
population_type new_population;
for(unsigned int i=0; i<population.size(); i++)
{
sort(population.begin(),population.end(),comp);
randomNum1 = randomSelection();
individualX = population[randomNum1];
randomNum2 =randomSelection();
individualY = population[randomNum2];
child = reproduce(individualX,individualY);
if(rand()%2==0) //random probability
child = mutate(child);
cout<<"fitness cost= "<<child->cost<<"
"<<child->arrangement<<endl;
if(isFit(child))
{
found=1;
return child;
}
new_population.push_back(child);
}
population = new_population;
}
return child;
}
void initialize()
{
chessBoardSize=8;
}
int main()
{
initialize();
generatePopulation();
individual *solution = GA();
for(int i=0;i<8;i++)
{
for(int j=0;j<8;j++)
{
if((((int)(solution->arrangement[i]))-48)-1==j)
cout<<'Q'<<" ";
else
cout<<'X'<<" ";
}
cout<<endl;
}
return 0;
}
After some more offsprings...

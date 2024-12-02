import math
MU,SD=list(map(float,input().rstrip().split()))
X_1=float(input())
X_2=float(input())
def normal_distribution(X,MU,SD):
    return 1/2*(1+math.erf((X-MU)/(SD*math.sqrt(2))))
print(round((1-normal_distribution(X_1,MU,SD))*100,2))
print(round((1-normal_distribution(X_2,MU,SD))*100,2))
print(round((normal_distribution(X_2,MU,SD))*100,2))
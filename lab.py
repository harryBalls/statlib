import math

def standard_deviation(data):
    def fun(x_):
        x = x_ - (sum(data)/len(data))
        return x*x
    map_ = list(map(fun,data))
    return math.sqrt(sum(map_)/len(map_))

def sample_standard_deviation(data):
    def fun(x_):
        x = x_ - sum(data)/len(data)
        return x*x
    map_ = list(map(fun,data))
    return math.sqrt(sum(map_)/(len(map_)-1))

def z_score(x,mn,sd):
	return ((x-mn)/sd)

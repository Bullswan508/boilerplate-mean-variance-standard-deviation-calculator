import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    calculations = {}

    list_flattened = np.array(list, np.int32)

    list_matrix = list_flattened.reshape(3,3)

    calculations['mean'] = [np.mean(list_matrix, axis=0).tolist(), np.mean(list_matrix, axis=1).tolist(), np.mean(list_flattened)]
    calculations['variance'] = [np.var(list_matrix, axis=0).tolist(), np.var(list_matrix, axis=1).tolist(), np.var(list_flattened)]
    calculations['standard deviation'] = [np.std(list_matrix, axis=0).tolist(), np.std(list_matrix, axis=1).tolist(), np.std(list_flattened)]
    calculations['max'] = [np.max(list_matrix, axis=0).tolist(), np.max(list_matrix, axis=1).tolist(), np.max(list_flattened)]
    calculations['min'] = [np.min(list_matrix, axis=0).tolist(), np.min(list_matrix, axis=1).tolist(), np.min(list_flattened)]
    calculations['sum'] = [np.sum(list_matrix, axis=0).tolist(), np.sum(list_matrix, axis=1).tolist(), np.sum(list_flattened)]



    return calculations


if __name__ == "__main__":
    
    nums = [0,1,2,3,4,5,6,7,8]
    
    print(calculate(nums))

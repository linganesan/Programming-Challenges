import numpy as np
import pandas as pd
import math

def fit_coef(col_lst):
    global train, test
    merge = None

    def cal_x_y(col_lst):
        col1 = col_lst[0]
        col2 = col_lst[1]

        name1 = '_'.join([''.join(x.split('_')) for x in col1])
        mean_train = train.groupby(col1)['log_demand'].mean().reset_index(name=name1)
        merge = pd.merge(test, mean_train, how='inner', on=col1)

        name2 = '_'.join([''.join(x.split('_')) for x in col2])
        mean_train = train.groupby(col2)['log_demand'].mean().reset_index(name=name2)
        merge = pd.merge(merge, mean_train, how='inner', on=col2)

        x1 = merge[name1].apply(np.expm1)
        x2 = merge[name2].apply(np.expm1)
        y = merge['log_demand']
        return x1, x2, y

    x1, x2, y = cal_x_y(col_lst)
    print('cal_x_y called')
    n = x1.size

    def f(v, x1, x2, y):
        a = v[0]
        b = v[1]
        c = v[2]
        square = (np.log1p(a*x1 + b*x2 + c) - y)**2
        return square.sum() / n

    def Df(v, x1, x2, y):
        a = v[0]
        b = v[1]
        c = v[2]
        t = a*x1 + b*x2 + c
        tmp = 2*(np.log1p(t) - y) / (1+t) / n
        d1 = tmp * x1
        d2 = tmp * x2
        d0 = tmp
        return np.array([d1.sum(), d2.sum(), d0.sum()])

    v0 = np.random.rand(3)
    v = None
    f1 = None
    max_iter = 1000
    eps = 1.0e-8

    # using gradient descent method to fit coefs
    for i in range(max_iter):
	
        g = Df(v0, x1, x2, y)
	print('called Df():')
	print(i)        
	gl2 = (g**2).sum()
        f0 = f(v0, x1, x2, y)
	print('called f():')
	print(i)   

        alpha = 1
        c = 0.5
        rho = 0.5
        # line search
        while f(v0 - alpha * g, x1, x2, y) > f0 - c * alpha * gl2:
            alpha = alpha * rho

        v = v0 - g * alpha
        f1 = f(v, x1, x2, y)
        if abs(math.sqrt(f0)-math.sqrt(f1)) < eps:
            break
        v0 = v
    
    return v, math.sqrt(f1)


if __name__ == "__main__":

    
# python 3.5 version: {**dtypes_test, **{'Venta_uni_hoy': np.uint16, 'Dev_uni_proxima': np.int32, 'Demanda_uni_equil': np.int16}}
	dtypes_col = {'Semana': np.int8, 'Agencia_ID': np.int16, 'Canal_ID': np.int8, 'Producto_ID': np.uint16,
               'Venta_uni_hoy': np.uint16, 'Dev_uni_proxima': np.int32, 'Demanda_uni_equil': np.int16}

# Now load train+test data

	print ('Reading train dataset')
	train = pd.read_csv('../data/train_3_8.csv', dtype = dtypes_col, usecols = ['Producto_ID', 'Ruta_SAK', 'Agencia_ID', 'Cliente_ID', 'Demanda_uni_equil'])
	print('train_3_8 loaded')

	print ('Reading test dataset')
	test= pd.read_csv('../data/train_9.csv', dtype = dtypes_col, usecols = ['Producto_ID', 'Ruta_SAK', 'Agencia_ID', 'Cliente_ID', 'Demanda_uni_equil'])
	print('Get train_9 loaded')





	train['log_demand'] = np.log1p(train.Demanda_uni_equil)

    #train['log_demand'] = train['Demanda_uni_equil'].apply(np.log1p)

	test['log_demand'] = np.log1p(test.Demanda_uni_equil)

    #test['log_demand'] = test['Demanda_uni_equil'].apply(np.log1p)

	col_lst = [
            ['Producto_ID', 'Cliente_ID', 'Agencia_ID'],
            ['Producto_ID', 'Ruta_SAK'],
            ]
	f = open('coef.csv', 'a')
	print('coef.csv created')
    	f.write("coef,log_rmse\n")
    	v, sqrt_f1 = fit_coef(col_lst)
    	print('last func call happened')
    	f.write("%s,%s,%s\n" % (col_lst, v, sqrt_f1))
    	f.close()


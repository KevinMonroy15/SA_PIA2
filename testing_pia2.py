def exact_answer(value, correct_value):
    if value==correct_value:
        return 1
    else:
        return 0

def compare(q1, q2, tolerance):
    diff=abs(q1-q2)
    if diff<=tolerance:
        return 1
    else:
        return 0

def not_empty(size):
    if size>0:
        return 1
    else:
        return 0

def evaluate(values,avalues,lvalues):
    
    score_exactans=[5,5,15,7,8,3,4,4,4]
    score_approxans=[2,3,5,5]
    #score_list=[5,5,2]
    
    correct_values=[2651,2,1855,(2643,8),(2643,),(1855,8),(788,8),(1855,1),(788,1)]
    
    #avalues=[datos[0,0],datos[-1,0],datos_estandarizados[0,0],datos_estandarizados[-1,0]]
    cvalues=[43221.71,363.59,0.639,0.003]
    
    exact_checks=[exact_answer(values[i],correct_values[i]) for i in range(len(correct_values))]
    approximate_checks=[compare(avalues[i],cvalues[i],0.01) for i in range(len(cvalues))]
    list_checks=[not_empty(v) for v in lvalues]
    
    puntos_aprox=[approximate_checks[i]*score_approxans[i] for i in range(len(score_approxans))]
    puntos_exactas=[exact_checks[i]*score_exactans[i] for i in range(len(score_exactans))]
    #puntos_listas=[list_checks[i]*score_list[i] for i in range(len(score_list))]
    
    sum_approxans=sum(puntos_aprox)
    sum_exactans=sum(puntos_exactas)
    sum_list=0
    #sum_list=sum(puntos_listas)
    total=sum_approxans+sum_exactans+sum_list
    
    poss_approxans=sum(score_approxans)
    poss_exactans=sum(score_exactans)
    #poss_list=sum(score_list)
    poss_list=0
    possible=poss_approxans+poss_exactans+poss_list
    
    dataframe_points=puntos_exactas[0]+puntos_exactas[1]
    numpy_points=puntos_aprox[0]+puntos_aprox[1]
    stand_points=puntos_aprox[2]+puntos_aprox[3]
    split_points=puntos_exactas[3]+puntos_exactas[4]
    sets_points=puntos_exactas[5]+puntos_exactas[6]+puntos_exactas[7]+puntos_exactas[8]
    
    print("===============================================")
    print("Generación dataframe: ",dataframe_points)
    print("Conversión a array numpy: ",numpy_points)
    print("Estandarización: ",stand_points)
    print("Cálculo tamaño entrenamiento: ",puntos_exactas[2])
    print("División X,y:",split_points)
    print("División entrenamiento y prueba: ",sets_points)
    print("===============================================")
    
    print("Puntos: ",total,"/",possible)
#Hallamos la energía potencial elástica
constante_elastica_del_resorte, deformacion_del_resorte, energia_potencial_elastica= 0.0, 0.0, 0.0

#Asiganacion de valores
constante_elastica_del_resorte= 8.7
deformacion_del_resorte= 6.9

#Calculo
energia_potencial_elastica= (1/2*constante_elastica_del_resorte)*deformacion_del_resorte**2

#Mostrar Valores
print("constante elastica del resorte:", constante_elastica_del_resorte)
print("deformacion del resorte:", deformacion_del_resorte)
print("energia potencial elastica:", energia_potencial_elastica)

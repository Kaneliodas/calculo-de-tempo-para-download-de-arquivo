#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
#Tamanho do arquivo em megabytes / (velocidade de download em megabits / 8) =  tempo em segundos.
Tamanho = float(input("Me diga o tamanho do arquivo para download (em MB)"))
velocidade = float(input("Me diga a velocidade do arquivo para download (em MB)"))
print("O tempo de download é esse " + str((Tamanho/(velocidade/8))/60) + " minutos")

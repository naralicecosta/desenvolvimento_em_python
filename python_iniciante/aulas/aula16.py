velocidade = 61
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_muldato_radar_1 = local_carro >= (LOCAL_1 - RADAR_1)
local_carro <= (LOCAL_1 - RADAR_RANGE)

if vel_carro_pass_radar_1:
    print("velocidade carro passou do radar 1")
    
if carro_muldato_radar_1 and vel_carro_pass_radar_1:
        print("carro multado em radar 1")
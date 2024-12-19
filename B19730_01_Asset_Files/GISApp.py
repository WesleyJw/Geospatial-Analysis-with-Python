# %%
import turtle as t

# %%
# Parametros
NAME = 0
POINTS = 1
POP = 2

# %%

# Criar a camada estado
state = [
    "PERNAMBUCO",
    [
        [-41.5, -7.0],  # Extremo noroeste
        [-34.8, -7.0],  # Extremo nordeste
        [-34.8, -10.5],  # Extremo sudeste
        [-41.5, -10.5],  # Extremo sudoeste
        [-41.5, -7.0]   # Fechando o polígono
    ],
    9616621  # População estimada
]

# Criar uma camada para cada cidade
cities = []
cities.append(["CABROBÓ", [-39.31, -8.51], 34262])   # Coordenadas aproximadas e população estimada
cities.append(["CUSTÓDIA", [-37.64, -8.09], 35927])  # Coordenadas aproximadas e população estimada
cities.append(["SERRA TALHADA", [-38.29, -7.99], 87457])  # Coordenadas aproximadas e população estimada

# %%
# Definir o tamanho da janela para renderizar o nosso mapa
map_width = 400
map_height = 300

# %%
# Definir o bouding box para o estado que é a maior camada

def cria_bouding_box(corrdenadas):
    
    # maior bounding box possivel
    minx = 180
    maxx = -180
    miny = 90
    maxy = -90
    for x,y in corrdenadas:
        if x < minx:
            minx = x
        elif x > maxx:
            maxx = x
        if y < miny:
            miny = y
        elif y > maxy:
            maxy = y
    return minx, maxx, miny, maxy

minx, maxx, miny, maxy = cria_bouding_box(state[POINTS])

minx, maxx, miny, maxy
# %%
# Definir a razão de escala entre as coordenadas e o tamnho da janela que será utilizada

# Encontra a distância entre pixels na terra
dist_x = maxx - minx
dist_y = maxy - miny

# Taxa da scala entre pixels com o tamnho da janela do grafico
x_ratio = map_width / dist_x
y_ratio = map_height / dist_y

# %%
# Essa função transforma um ponto de coordenadas do mapa em coordenadas de pixel.
def convert(point):
    """Converta lat/lon para a janela de coordenadas"""
    lon = point[0]
    lat = point[1]
    x = map_width - ((maxx - lon) * x_ratio)
    y = map_height - ((maxy - lat) * y_ratio)
    # Os gráficos d (turtle) do Python começam no centro da tela
    # então precisamos deslocar os pontos para que eles fiquem centralizados
    x = x - (map_width/2)
    y = y - (map_height/2)
    return [x, y]

# %%
# Definir a janela com a biblioteca turtle
t.setup(900,600)
t.screensize(800,500)
wn = t.Screen()
wn.title("Wesley GIS")

# %%
# Desenhar a camada estado
t.up()
first_pixel = None

for point in state[POINTS]:
    pixel = convert(point)
    if not first_pixel:
        first_pixel = pixel
    t.goto(pixel)
    t.down()
# Volte ao primeiro ponto
t.goto(first_pixel)
# Adicionar o nome do estado
t.up()
t.goto([0, 0])
t.write(state[NAME], align="center", font=("Arial", 16, "bold"))

# %%
# Desenhar as cidades
for city in cities:
    pixel = convert(city[POINTS])
    t.up()
    t.goto(pixel)
    # Coloque um ponto para as cidades
    t.dot(10)
    # Nome das cidades
    t.write(city[NAME] + ", Pop.: " + str(city[POP]), align="left")
    t.up()

# %%
# Realizar uma consulta por atributo  
# Pergunta: Qual cidade tem a maior população?  
# Escreva o resultado, mas certifique-se de que ele esteja abaixo do mapa.  
biggest_city = max(cities, key=lambda city: city[POP])
t.goto(0, -1*((map_height/2)+20))
t.write("The highest-populated city is: " + biggest_city[NAME], align="center")

# Realizar uma consulta espacial  
# Pergunta: Qual é a cidade mais a oeste?  
# Escreva o resultado, mas certifique-se de que ele esteja abaixo da outra pergunta.  
western_city = min(cities, key=lambda city: city[POINTS])
t.goto(0, -1*((map_height/2)+40))
t.write("The western-most city is: " + western_city[NAME], align="center")

# Esconder a caneta que desenha o mapa.
t.pen(shown=False)
t.done()
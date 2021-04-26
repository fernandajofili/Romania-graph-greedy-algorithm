dist = {
	'Arad':             366,
    'Bucharest': 	   	  0,
    'Craiova':          160, 
    'Dobreta':          242, 
    'Eforie':           161, 
    'Fagaras':          176, 
    'Giurgiu':           77, 
    'Hirsova':          151, 
    'Iasi':             226, 
    'Lugoj':            244, 
    'Mehadia':          241, 
    'Neamt':            234, 
    'Oradea':           380, 
    'Pitesti':           10, 
    'Rimnicu Vilcea':   193, 
    'Sibiu':            253, 
    'Timisoara':        329, 
    'Urziceni':          80, 
    'Vaslui':           199, 
    'Zerind':           374	
}


vizinhancas = {
    'Arad': 			['Zerind', 		        'Timisoara', 	'Sibiu'		                 ],
    'Bucharest': 		['Urziceni', 	        'Giurgiu', 		'Pitesti', 		    'Fagaras'],
	'Craiova': 			['Dobreta', 	        'Pitesti',      'Rimnicu Vilcea'	         ],
    'Dobreta': 			['Mehadia', 			'Craiova'	                                 ],
    'Eforie':           ['Hirsova'                                                           ],
    'Fagaras':			['Sibiu',               'Bucharest'                                  ],
    'Giurgiu': 			['Bucharest'	                                                     ],
    'Hirsova':          ['Eforie',              'Urziceni'                                   ],
    'Iasi':             ['Neamt',               'Vaslui'                                     ],
	'Lugoj': 			['Mehadia',             'Timisoara'	                    	         ],
	'Mehadia': 			['Lugoj',               'Dobreta'	                    	         ],
    'Neamt':            ['Iasi'                                                              ],
	'Oradea': 			['Zerind', 		        'Sibiu'		                                 ],
    'Pitesti': 			['Rimnicu Vilcea', 	    'Bucharest',    'Craiova'	                 ],
    'Rimnicu Vilcea': 	['Sibiu',               'Pitesti', 	    'Craiova'		             ],
    'Sibiu': 			['Rimnicu Vilcea',      'Fagaras', 		'Arad',             'Oradea' ],
	'Timisoara': 		['Lugoj',               'Arad'		                                 ],
    'Urziceni':         ['Bucharest',           'Hirsova',      'Vaslui'                     ],
    'Vaslui':           ['Iasi',                'Urziceni'                                   ],
	'Zerind':			['Oradea',              'Arad'                                       ]	
}

global cidade_origem

def obter_melhor_vizinhanca(cidade):
	global cidade_origem
	menor_distancia = 99999
	melhor_vizinhanca = None

	for cidade_local in vizinhancas[cidade]:
		if cidade_local == cidade_origem:
			continue
		distancia_do_destino = dist[cidade_local]
		if menor_distancia > distancia_do_destino:
			menor_distancia = distancia_do_destino
			melhor_vizinhanca = cidade_local
	return melhor_vizinhanca


def melhor_caminho(cidade_origem, cidade_destino):

	cidade_atual = cidade_origem
	if cidade_atual == cidade_destino:
		print(f'Você chegou ao seu destino: {cidade_atual}')
	else:
		proxima_cidade = obter_melhor_vizinhanca(cidade_atual)
		print("\t  ", proxima_cidade)
		melhor_caminho(proxima_cidade, cidade_destino)


def main():
	global cidade_origem
	cidade_origem = "Arad"
	cidade_destino = "Bucharest"

	print(f'Saindo de: {cidade_origem}')
	melhor_caminho(cidade_origem, cidade_destino)


if __name__ == "__main__":
	main()

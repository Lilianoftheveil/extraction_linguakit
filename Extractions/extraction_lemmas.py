from jjcli import *
from linguakit import *
from collections import Counter

cl = clfilter("")

lemmas_clean = ["<blank>", ".", ",", ":", ";", "...", "?", "!", "—", "-", '"', "(", ")"]

light_words_pt = ["ir" ,"ser", "estar", "ter", "haver", "tipo", "coisa", "que", "aí", "aqui", "alí"]

stop_words_pt = ["a", "ao", "aos", "aquela", "aquelas",	"aquele", "aqueles", "aquilo", "as", "até",	
"com", "como", "da", "das",	"de", "dela", "delas", "dele", "deles", "depois", "do",	"dos", "e", "ela",
"elas",	"ele", "eles", "em", "entre", "era", "eram", "essa", "essas", "esse", "esses",
"esta",	"estamos", "estas",	"estava", "estavam", "este", "esteja", "estejam", "estejamos",
"estes", "esteve", "estive", "estivemos", "estiver", "estivera", "estiveram", "estiverem",
"estivermos", "estivesse", "estivessem", "estivéramos",	"estivéssemos",	"estou", "está",
"estávamos", "estão", "eu",	"foi", "fomos",	"for", "fora",	"foram", "forem", "formos",	"fosse",
"fossem", "fui", "fôramos",	"fôssemos",	"haja",	"hajam", "hajamos",	"havemos", "hei",	
"houve", "houvemos", "houver", "houvera", "houveram", "houverei", "houverem", "houveremos",
"houveria",	"houveriam", "houvermos", "houverá", "houverão", "houveríamos",	"houvesse",
"houvessem", "houvéramos", "houvéssemos", "há", "hão", "isso", "isto", "já", "lhe",	"lhes",
"mais",	"mas", "me", "mesmo", "meu", "meus", "minha", "minhas", "muito", "na", "nas", "nem",
"no", "nos", "nossa", "nossas",	"nosso", "nossos", "num", "numa", "não", "nós",	"o", "os", "ou",
"para",	"pela",	"pelas", "pelo", "pelos", "por", "qual", "quando", "que", "quem", "se",	"seja",
"sejam", "sejamos",	"sem", "serei",	"seremos", "seria",	"seriam", "será", "serão", "seríamos",
"seu", "seus",	"somos", "sou",	"sua", "suas", "são", "só",	"também", "te",	"tem", "temos",
"tenha", "tenham", "tenhamos", "tenho",	"terei", "teremos",	"teria", "teriam", "terá", "terão",
"teríamos",	"teu", "teus", "teve", "tinha",	"tinham", "tive", "tivemos", "tiver", "tivera",
"tiveram", "tiverem", "tivermos", "tivesse", "tivessem", "tivéramos", "tivéssemos",	"tu",
"tua", "tuas", "tém", "tínhamos", "um", "uma", "você", "vocês", "vos", "à",	"às", "éramos"]


lemma_type = []


def ajuda():
	print("""Comandos:\n
help 
- Imprime a lista de comandos

lemmas
- Imprime a extração de todos os lemmas encontrados

lemmas_clean
- Imprime a extração de todos os lemmas encontrados,
eliminando os lemmas derivados de pontuações, stop words e linhas em branco <blank>

names
- Imprime a extração de todos os lemmas derivados de Nomes Próprios

subs
- Imprime a extração de todos os lemmas derivados de Substantivos

adj
- Imprime a extração de todos os lemmas derivados de Adjetivos

verbs
- Imprime a extração de todos os lemmas derivados de Verbos

exit
- encerra o programa
""")
       
def lemmas():
	a = input('''Gostaria de guardar a extração em um arquivo? 
Digite: s/S (sim) or n/N (não)''').lower()
	if a == "s":
		b = input("Nome do Arquivo: ")
		c = input ("Formato: txt ou csv? ").lower()
		if c == "txt":
			f = open(b + ".txt", "w")
			for y in cl.input():
				if y != "":
					k, l, m = y.split()
					f.write(f"{l}\n")
			f.close()
		elif c == "csv":
			f = open(b + ".csv", "w")
			for y in cl.input():
				if y != "":
					k, l, m = y.split()
					f.write(f"{l}\n")
			f.close()
		else:
			print("ERRO: Formato Inválido.")
			print("Não foi possível gerar o resultado.")

	elif a == "n":     
		for a in cl.input():
			if a != "":
				x, y, z = a.split()
				print(y)
	else:
		for a in cl.input():
			if a != "":
				x, y, z = a.split()
				print(y)

def lemmas_cll():
	a = input('''Gostaria de guardar a extração em um arquivo? 
Digite: s/S (sim) or n/N (não)''').lower()
	if a == "s":
		b = input("Nome do Arquivo: ")
		c = input ("Formato: txt ou csv? ").lower()
		if c == "txt":
			f = open(b + ".txt", "w")
			for y in cl.input():
				if y != "":
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						f.write(f"{l}\n")
			f.close()
		elif c == "csv":
			f = open(b + ".csv", "w")
			for y in cl.input():
				if y != "":
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						f.write(f"{l}\n")
			f.close()
		else:
			print("ERRO: Formato Inválido.")
			print("Não foi possível gerar o resultado.")

	elif a == "n":     
		for y in cl.input():
			if y != "":
				k, l, m = y.split()
				if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
					print(y)
	else:
		for y in cl.input():
			if y != "":
				k, l, m = y.split()
				if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
					print(y)

def lemmas_cl():
	lemma_type = []
	z = input('''Digite "allocc" para a lista de todas lemmas (com as devidas limpezas) por ordem de ocorrência. 
Digite (x) - um número inteiro - para a extração apenas dos x lemmas (com as devidas limpezas) mais recorrentes.\n''').lower()
	if z == "allocc":
		a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
		if a == "s":
			b = input("Nome do Arquivo: ")
			c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if y != "":
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							f.write(f"{l, m}\n")
					d = (Counter(lemma_type).most_common())
					for e in d:
						f.write(f"{e}\n")
				lemma_type = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if y != "":
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							f.write(f"{l, m}\n")
					d = (Counter(lemma_type).most_common())
					for e in d:
						f.write(f"{e}\n")
				lemma_type = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
					if y != "":
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							lemma_type.append(y)
						
			print(Counter(lemma_type).most_common())
			lemma_type = []
		else:
			for y in cl.input():
					if y != "":
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							lemma_type.append(y)
						
			print(Counter(lemma_type).most_common())
			lemma_type = []

	elif z != "allocc":
		try:
			int(z)
			z = int(z)
			lemma_type = []
			a = input('''Digite "allocc" para a lista de todas lemmas (com as devidas limpezas) por ordem de ocorrência. 
		Digite (x) - um número inteiro - para a extração apenas dos x lemmas (com as devidas limpezas) mais recorrentes.\n''').lower()
			if a == "allocc":
				a = input('''Gostaria de guardar a extração em um arquivo? 
		s/S (sim) n/N (não): ''')
				if a == "s":
					b = input("Nome do Arquivo: ")
					c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
					if c == "txt":
						f = open(b + ".txt", "w")
						for y in cl.input():
							if y != "":
								k, l, m = y.split()
								if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
									f.write(f"{l, m}\n")
							d = (Counter(lemma_type).most_common(z))
							for e in d:
								f.write(f"{e}\n")
						lemma_type = []
						f.close()
					elif c == "csv":
						f = open(b + ".csv", "w")
						for y in cl.input():
							if y != "":
								k, l, m = y.split()
								if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
									f.write(f"{l, m}\n")
							d = (Counter(lemma_type).most_common(z))
							for e in d:
								f.write(f"{e}\n")
						lemma_type = []
						f.close()
					else:
						print("ERRO: Formato Inválido.")
						print("Não foi possível gerar o resultado.")

				elif a == "n":
					for y in cl.input():
							if y != "":
								k, l, m = y.split()
								if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
									lemma_type.append(y)
								
					print(Counter(lemma_type).most_common(z))
					lemma_type = []
				else:
					for y in cl.input():
							if y != "":
								k, l, m = y.split()
								if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
									lemma_type.append(y)
								
					print(Counter(lemma_type).most_common(z))
					lemma_type = []
		except:
			print("Por favor, digite 'allocc' ou apenas números inteiros.")

def lemma_name():
	a = input('''Gostaria de guardar a extração em um arquivo? 
Digite: s/S (sim) or n/N (não)''').lower()
	if a == "s":
		b = input("Nome do Arquivo: ")
		c = input ("Formato: txt ou csv? ").lower()
		if c == "txt":
			f = open(b + ".txt", "w")
			for y in cl.input():
				if "NP0" in y:
					k, l, m = y.split()
					if l not in lemmas_clean:
						f.write(f"{l}\n")
			f.close()
		elif c == "csv":
			f = open(b + ".csv", "w")
			for y in cl.input():
				if "NP0" in y:
					k, l, m = y.split()
					if l not in lemmas_clean:
						f.write(f"{l}\n")
			f.close()
		else:
			print("ERRO: Formato Inválido.")
			print("Não foi possível gerar o resultado.")
	
	elif a == "n":     
		for y in cl.input():
				if "NP0" in y:
					k, l, m = y.split()
					if l not in lemmas_clean:
						print(l)
	else:
		for y in cl.input():
				if "NP0" in y:
					k, l, m = y.split()
					if l not in lemmas_clean:
						print(l)

def lemma_subs():
	a = input('''Gostaria de guardar a extração em um arquivo? 
Digite: s/S (sim) or n/N (não)''').lower()
	if a == "s":
		b = input("Nome do Arquivo: ")
		c = input ("Formato: txt ou csv? ").lower()
		if c == "txt":
			f = open(b + ".txt", "w")
			for y in cl.input():
				if "NCM" in y:
					k, l, m = y.split()
					if l not in lemmas_clean:
						f.write(f"{l}\n")
			f.close()
		elif c == "csv":
			f = open(b + ".csv", "w")
			for y in cl.input():
				if "NCM" in y:
					k, l, m = y.split()
					if l not in lemmas_clean:
						f.write(f"{l}\n")
			f.close()
		else:
			print("ERRO: Formato Inválido.")
			print("Não foi possível gerar o resultado.")
	
	elif a == "n":     
		for y in cl.input():
				if "NCM" in y:
					k, l, m = y.split()
					if l not in lemmas_clean:
						print(l)
	else:
		for y in cl.input():
				if "NCM" in y:
					k, l, m = y.split()
					if l not in lemmas_clean:
						print(l)

def lemma_adj():
	a = input('''Gostaria de guardar a extração em um arquivo? 
Digite: s/S (sim) or n/N (não)''').lower()
	if a == "s":
		b = input("Nome do Arquivo: ")
		c = input ("Formato: txt ou csv? ").lower()
		if c == "txt":
			f = open(b + ".txt", "w")
			for y in cl.input():
				if "AQ0" in y:
					k, l, m = y.split()
					if l not in lemmas_clean:
						f.write(f"{l}\n")
			f.close()
		elif c == "csv":
			f = open(b + ".csv", "w")
			for y in cl.input():
				if "AQ0" in y:
					k, l, m = y.split()
					if l not in lemmas_clean:
						f.write(f"{l}\n")
			f.close()
		else:
			print("ERRO: Formato Inválido.")
			print("Não foi possível gerar o resultado.")
	
	elif a == "n":     
		for y in cl.input():
				if "AQ0" in y:
					k, l, m = y.split()
					if l not in lemmas_clean:
						print(l)
	else:
		for y in cl.input():
				if "AQ0" in y:
					k, l, m = y.split()
					if l not in lemmas_clean:
						print(l)

def lemma_verbs():
	a = input('''Gostaria de guardar a extração em um arquivo? 
Digite: s/S (sim) or n/N (não)''').lower()
	if a == "s":
		b = input("Nome do Arquivo: ")
		c = input ("Formato: txt ou csv? ").lower()
		if c == "txt":
			f = open(b + ".txt", "w")
			for y in cl.input():
				if "VMI" in y:
					k, l, m = y.split()
					if l not in lemmas_clean:
						f.write(f"{l}\n")
			f.close()
		elif c == "csv":
			f = open(b + ".csv", "w")
			for y in cl.input():
				if "VMI" in y:
					k, l, m = y.split()
					if l not in lemmas_clean:
						f.write(f"{l}\n")
			f.close()
		else:
			print("ERRO: Formato Inválido.")
			print("Não foi possível gerar o resultado.")
	
	elif a == "n":     
		for y in cl.input():
				if "VMI" in y:
					k, l, m = y.split()
					if l not in lemmas_clean:
						print(l)
	else:
		for y in cl.input():
				if "VMI" in y:
					k, l, m = y.split()
					if l not in lemmas_clean:
						print(l)

def lemmas_main():    
	ent_list = []
	z = input('''Digite "allocc" para a lista de todas as entidades por ordem de ocorrência. 
Digite (x) - um número inteiro - para a extração apenas das x entidades mais recorrentes.\n''').lower()
	if z == "allocc":
		a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
		if a == "s":
			b = input("Nome do Arquivo: ")
			c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
						ent_list.append(y)
				d = (Counter(ent_list).most_common())
				for e in d:
					f.write(f"{e}\n")
				ent_list = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
						ent_list.append(y)
				d = (Counter(ent_list).most_common())
				for e in d:
					f.write(f"{e}\n")
				ent_list = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
					ent_list.append(y)
						
			print(Counter(ent_list).most_common())
			ent_list = []
		else:
			for y in cl.input():
					ent_list.append(y)
						
			print(Counter(ent_list).most_common())
			ent_list = []

	elif z != "allocc":
		try:
			int(z)
			z = int(z)
			a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
			if a == "s":
				b = input("Nome do Arquivo: ")
				c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
				if c == "txt":
					f = open(b + ".txt", "w")
					for y in cl.input():
							ent_list.append(y)
					d = (Counter(ent_list).most_common(z))
					for e in d:
						f.write(f"{e}\n")
					ent_list = []
					f.close()
				elif c == "csv":
					f = open(b + ".csv", "w")
					for y in cl.input():
							ent_list.append(y)
					d = (Counter(ent_list).most_common(z))
					for e in d:
						f.write(f"{e}\n")
					ent_list = []
					f.close()
				else:
					print("ERRO: Formato Inválido.")
					print("Não foi possível gerar o resultado.")

			elif a == "n":
				for y in cl.input():
						ent_list.append(y)
						
				print(Counter(ent_list).most_common(z))
				ent_list = []
			else:
				for y in cl.input():
						ent_list.append(y)
						
				print(Counter(ent_list).most_common(z))
				ent_list = []
		except:
			print("Por favor, digite 'allocc' ou apenas números inteiros.")

def names_main():    
	ent_list = []
	z = input('''Digite "allocc" para a lista de todos os Verbos (por ordem de ocorrência). 
Digite (x) - um número inteiro - para a extração apenas dos x Verbos mais recorrentes.\n''').lower()
	if z == "allocc":
		a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
		if a == "s":
			b = input("Nome do Arquivo: ")
			c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if "NP0" in y:
						ent_list.append(y)
				d = (Counter(ent_list).most_common())
				for e in d:
					f.write(f"{e}\n")
				ent_list = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if "NP0" in y:
						ent_list.append(y)
				d = (Counter(ent_list).most_common())
				for e in d:
					f.write(f"{e}\n")
				ent_list = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
					if "NP0" in y:
						ent_list.append(y)
						
			print(Counter(ent_list).most_common())
			ent_list = []
		else:
			for y in cl.input():
					if "NP0" in y:
						ent_list.append(y)
						
			print(Counter(ent_list).most_common())
			ent_list = []

	elif z != "allocc":
		try:
			int(z)
			z = int(z)
			a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
			if a == "s":
				b = input("Nome do Arquivo: ")
				c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
				if c == "txt":
					f = open(b + ".txt", "w")
					for y in cl.input():
						if "NP0" in y:
							ent_list.append(y)
					d = (Counter(ent_list).most_common(z))
					for e in d:
						f.write(f"{e}\n")
					ent_list = []
					f.close()
				elif c == "csv":
					f = open(b + ".csv", "w")
					for y in cl.input():
						if "NP0" in y:
							ent_list.append(y)
					d = (Counter(ent_list).most_common(z))
					for e in d:
						f.write(f"{e}\n")
					ent_list = []
					f.close()
				else:
					print("ERRO: Formato Inválido.")
					print("Não foi possível gerar o resultado.")

			elif a == "n":
				for y in cl.input():
					if "NP0" in y:
						ent_list.append(y)
						
				print(Counter(ent_list).most_common(z))
				ent_list = []
			else:
				for y in cl.input():
					if "NP0" in y:
						ent_list.append(y)
						
				print(Counter(ent_list).most_common(z))
				ent_list = []
		except:
			print("Por favor, digite 'allocc' ou apenas números inteiros.")

def subs_main():    
	ent_list = []
	z = input('''Digite "allocc" para a lista de todos os Verbos (por ordem de ocorrência). 
Digite (x) - um número inteiro - para a extração apenas dos x Verbos mais recorrentes.\n''').lower()
	if z == "allocc":
		a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
		if a == "s":
			b = input("Nome do Arquivo: ")
			c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if "NCM" in y:
						ent_list.append(y)
				d = (Counter(ent_list).most_common())
				for e in d:
					f.write(f"{e}\n")
				ent_list = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if "NCM" in y:
						ent_list.append(y)
				d = (Counter(ent_list).most_common())
				for e in d:
					f.write(f"{e}\n")
				ent_list = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
					if "NCM" in y:
						ent_list.append(y)
						
			print(Counter(ent_list).most_common())
			ent_list = []
		else:
			for y in cl.input():
					if "NCM" in y:
						ent_list.append(y)
						
			print(Counter(ent_list).most_common())
			ent_list = []

	elif z != "allocc":
		try:
			int(z)
			z = int(z)
			a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
			if a == "s":
				b = input("Nome do Arquivo: ")
				c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
				if c == "txt":
					f = open(b + ".txt", "w")
					for y in cl.input():
						if "NCM" in y:
							ent_list.append(y)
					d = (Counter(ent_list).most_common(z))
					for e in d:
						f.write(f"{e}\n")
					ent_list = []
					f.close()
				elif c == "csv":
					f = open(b + ".csv", "w")
					for y in cl.input():
						if "NCM" in y:
							ent_list.append(y)
					d = (Counter(ent_list).most_common(z))
					for e in d:
						f.write(f"{e}\n")
					ent_list = []
					f.close()
				else:
					print("ERRO: Formato Inválido.")
					print("Não foi possível gerar o resultado.")

			elif a == "n":
				for y in cl.input():
					if "NCM" in y:
						ent_list.append(y)
						
				print(Counter(ent_list).most_common(z))
				ent_list = []
			else:
				for y in cl.input():
					if "NCM" in y:
						ent_list.append(y)
						
				print(Counter(ent_list).most_common(z))
				ent_list = []
		except:
			print("Por favor, digite 'allocc' ou apenas números inteiros.")

def adj_main():    
	ent_list = []
	z = input('''Digite "allocc" para a lista de todos os Verbos (por ordem de ocorrência). 
Digite (x) - um número inteiro - para a extração apenas dos x Verbos mais recorrentes.\n''').lower()
	if z == "allocc":
		a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
		if a == "s":
			b = input("Nome do Arquivo: ")
			c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if "AQ0" in y:
						ent_list.append(y)
				d = (Counter(ent_list).most_common())
				for e in d:
					f.write(f"{e}\n")
				ent_list = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if "AQ0" in y:
						ent_list.append(y)
				d = (Counter(ent_list).most_common())
				for e in d:
					f.write(f"{e}\n")
				ent_list = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
					if "AQ0" in y:
						ent_list.append(y)
						
			print(Counter(ent_list).most_common())
			ent_list = []
		else:
			for y in cl.input():
					if "AQ0" in y:
						ent_list.append(y)
						
			print(Counter(ent_list).most_common())
			ent_list = []

	elif z != "allocc":
		try:
			int(z)
			z = int(z)
			a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
			if a == "s":
				b = input("Nome do Arquivo: ")
				c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
				if c == "txt":
					f = open(b + ".txt", "w")
					for y in cl.input():
						if "AQ0" in y:
							ent_list.append(y)
					d = (Counter(ent_list).most_common(z))
					for e in d:
						f.write(f"{e}\n")
					ent_list = []
					f.close()
				elif c == "csv":
					f = open(b + ".csv", "w")
					for y in cl.input():
						if "AQ0" in y:
							ent_list.append(y)
					d = (Counter(ent_list).most_common(z))
					for e in d:
						f.write(f"{e}\n")
					ent_list = []
					f.close()
				else:
					print("ERRO: Formato Inválido.")
					print("Não foi possível gerar o resultado.")

			elif a == "n":
				for y in cl.input():
					if "AQ0" in y:
						ent_list.append(y)
						
				print(Counter(ent_list).most_common(z))
				ent_list = []
			else:
				for y in cl.input():
					if "AQ0" in y:
						ent_list.append(y)
						
				print(Counter(ent_list).most_common(z))
				ent_list = []
		except:
			print("Por favor, digite 'allocc' ou apenas números inteiros.")

def verbs_main():    
	ent_list = []
	z = input('''Digite "allocc" para a lista de todos os Verbos (por ordem de ocorrência). 
Digite (x) - um número inteiro - para a extração apenas dos x Verbos mais recorrentes.\n''').lower()
	if z == "allocc":
		a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
		if a == "s":
			b = input("Nome do Arquivo: ")
			c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if "VMI" in y:
						ent_list.append(y)
				d = (Counter(ent_list).most_common())
				for e in d:
					f.write(f"{e}\n")
				ent_list = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if "VMI" in y:
						ent_list.append(y)
				d = (Counter(ent_list).most_common())
				for e in d:
					f.write(f"{e}\n")
				ent_list = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
					if "VMI" in y:
						ent_list.append(y)
						
			print(Counter(ent_list).most_common())
			ent_list = []
		else:
			for y in cl.input():
					if "VMI" in y:
						ent_list.append(y)
						
			print(Counter(ent_list).most_common())
			ent_list = []

	elif z != "allocc":
		try:
			int(z)
			z = int(z)
			a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
			if a == "s":
				b = input("Nome do Arquivo: ")
				c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
				if c == "txt":
					f = open(b + ".txt", "w")
					for y in cl.input():
						if "VMI" in y:
							ent_list.append(y)
					d = (Counter(ent_list).most_common(z))
					for e in d:
						f.write(f"{e}\n")
					ent_list = []
					f.close()
				elif c == "csv":
					f = open(b + ".csv", "w")
					for y in cl.input():
						if "VMI" in y:
							ent_list.append(y)
					d = (Counter(ent_list).most_common(z))
					for e in d:
						f.write(f"{e}\n")
					ent_list = []
					f.close()
				else:
					print("ERRO: Formato Inválido.")
					print("Não foi possível gerar o resultado.")

			elif a == "n":
				for y in cl.input():
					if "VMI" in y:
						ent_list.append(y)
						
				print(Counter(ent_list).most_common(z))
				ent_list = []
			else:
				for y in cl.input():
					if "VMI" in y:
						ent_list.append(y)
						
				print(Counter(ent_list).most_common(z))
				ent_list = []
		except:
			print("Por favor, digite 'allocc' ou apenas números inteiros.")

while True:
	x = input('''Digite o comando desejado:
Digite "help" para ter acesso a lista de comandos.\n''').lower()
	if x == ("help"):
		ajuda()
		continue
	elif x == "lemmas":
		y = input(
'''Digite "alllemmas" para a extração de todos os lemmas.
Digite "lemmamain" para a extração de todos os lemmas (dado suas ocorrências).\n''').lower()
		if y == "alllemmas":
			lemmas()
			print("\n")
			continue
		elif y == "lemmamain":
			lemmas_main()
			print("\n")
			continue
	elif x == "lemmas_clean":
		y = input(
'''Digite "alllecl" para a extração de todos os lemmas com exceção dos lemmas derivados de pontuações, stop words e linhas em branco <blank>.\n
Digite "leclmain" para a extração de todos os lemmas com exceção dos lemmas derivados de pontuações, stop words e linhas em branco <blank> (dado suas ocorrências).\n''').lower()
		if y == "alllecl":
			lemmas_cll()
			print("\n")
			continue
		elif y == "lemmamain":
			lemmas_cl()
			print("\n")
			continue
	elif x == "names":
		y = input(
'''Digite "allnames" para a extração de todos os lemmas derivados de Nomes Próprios.
Digite "namemain" para a extração de todos os lemmas derivados de Nomes Próprios (dado suas ocorrências).\n''').lower()
		if y == "allnames":
			lemma_name()
			print("\n")
			continue
		elif y == "namemain":
			names_main()
			print("\n")
			continue
	elif x == "subs":
		y = input(
'''Digite "allsubs" para a extração de todos os lemmas derivados de Substantivos.
Digite "submain" para a extração de todos os lemmas derivados de Substantivos (dado suas ocorrências)\n''').lower()
		if y == "allsubs":
			lemma_subs()
			print("\n")
			continue
		elif y == "submain":
			subs_main()
			print("\n")
			continue
	elif x == "adj":
		y = input(
'''Digite "alladj" para a extração de todos os lemmas derivados de Adjetivos.
Digite "adjmain" para a extração de todos os lemmas derivados de Adjetivos (dado suas ocorrências)\n''').lower()
		if y == "alladj":
			lemma_adj()
			print("\n")
			continue
		elif y == "adjmain":
			adj_main()
			print("\n")
			continue
	elif x == "verbs":
		y = input(
'''Digite "allverbs" para a extração de todos os lemmas derivados de Verbos.
Digite "verbmain" para a extração de todos os lemmas derivados de Verbos (dado suas ocorrências)\n''').lower()
		if y == "allverbs":
			lemma_verbs()
			print("\n")
			continue
		elif y == "verbmain":
			verbs_main()
			print("\n")
			continue
	elif x == "exit":
		break
	else:
		pass
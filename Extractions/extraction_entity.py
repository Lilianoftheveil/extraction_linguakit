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

ent_list = []

person_list = []

local_list = []

org_list = []

orther_list = []


def ajuda():
	print("""Comandos:\n
help 
- Imprime a lista de comandos

entities
- Imprime a extração de todas as entidades encontradas (PESSOA, LOCAL, ORGANIZAÇÃO e OUTROS)

entities_clean
- Imprime a extração de todas as entidades encontradas (PESSOA, LOCAL, ORGANIZAÇÃO e OUTROS),
eliminando as entidades referentes à pontuações, stop words e linhas em branco <blank>

entity_person
- Imprime a lista de comandos referentes à extração de entidades (PESSOA)

entity_local
- Imprime a lista de comandos referentes à extração de entidades (LUGARES)

entity_org
- Imprime a lista de comandos referentes à extração de entidades (ORGANIZAÇÕES)

entity_orther
- Imprime a lista de comandos referentes à extração de entidades (OUTROS)
'a entidades nomeadas que não se integram em nenhuma das categorias anteriores'

exit
- encerra o programa
""")
       

def entities():
	a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
	if a == "s":
		b = input("Nome do Arquivo: ")
		c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
		if c == "txt":
			f = open(b + ".txt", "w")
			for y in cl.input():
				f.write(f"{y}\n")
			f.close()
		elif c == "csv":
			f = open(b + ".csv", "w")
			for y in cl.input():
				f.write(f"{y}\n")
			f.close()
		else:
			print("ERRO: Formato Inválido.")
			print("Não foi possível gerar o resultado.")
	elif a == "n":    
		for y in cl.input():
			print(y)
		print("\n")
	else:
		for y in cl.input():
			print(y)
		print("\n") 
		

def entities_cl_stop():
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
					if k not in lemmas_clean and k not in light_words_pt and k not in stop_words_pt:
						f.write(f"{k, l, m}\n")
			f.close()
		elif c == "csv":
			f = open(b + ".csv", "w")
			for y in cl.input():
				if y != "":
					k, l, m = y.split()
					if k not in lemmas_clean and k not in light_words_pt and k not in stop_words_pt:
						f.write(f"{k, l, m}\n")
			f.close()
		else:
			print("ERRO: Formato Inválido.")
			print("Não foi possível gerar o resultado.")
	elif a == "n":    
		for y in cl.input():
			if y != "":
				k, l, m = y.split()
				if k not in lemmas_clean and k not in light_words_pt and k not in stop_words_pt:
					print(k, l, m)
		print("\n")
	else:
		for y in cl.input():
			if y != "":
				k, l, m = y.split()
				if k not in lemmas_clean and k not in light_words_pt and k not in stop_words_pt:
					print(k, l, m)


def entity_np():
	a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
	if a == "s":
		b = input("Nome do Arquivo: ")
		c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
		if c == "txt":
			f = open(b + ".txt", "w")
			for y in cl.input():
				if "NP00SP0" in y:
					f.write(f"{y}\n")
			f.close()
		elif c == "csv":
			f = open(b + ".csv", "w")
			for y in cl.input():
				if "NP00SP0" in y:
					f.write(f"{y}\n")
			f.close()
		else:
			print("ERRO: Formato Inválido.")
			print("Não foi possível gerar o resultado.")
	elif a == "n":    
		for y in cl.input():
			if "NP00SP0" in y:
				print(y)
	else:
		for y in cl.input():
			if "NP00SP0" in y:
				print(y) 


def entity_lc():
	a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
	if a == "s":
		b = input("Nome do Arquivo: ")
		c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
		if c == "txt":
			f = open(b + ".txt", "w")
			for y in cl.input():
				if "NP00G00" in y:
					f.write(f"{y}\n")
			f.close()
		elif c == "csv":
			f = open(b + ".csv", "w")
			for y in cl.input():
				if "NP00G00" in y:
					f.write(f"{y}\n")
			f.close()
		else:
			print("ERRO: Formato Inválido.")
			print("Não foi possível gerar o resultado.")
	elif a == "n":    
		for y in cl.input():
			if "NP00G00" in y:
				print(y)
	else:
		for y in cl.input():
			if "NP00G00" in y:
				print(y) 
				

def entity_org():
	a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
	if a == "s":
		b = input("Nome do Arquivo: ")
		c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
		if c == "txt":
			f = open(b + ".txt", "w")
			for y in cl.input():
				if "NP00O00" in y:
					f.write(f"{y}\n")
			f.close()
		elif c == "csv":
			f = open(b + ".csv", "w")
			for y in cl.input():
				if "NP00O00" in y:
					f.write(f"{y}\n")
			f.close()
		else:
			print("ERRO: Formato Inválido.")
			print("Não foi possível gerar o resultado.")
	elif a == "n":    
		for y in cl.input():
			if "NP00O00" in y:
				print(y)
	else:
		for y in cl.input():
			if "NP00O00" in y:
				print(y) 
				

def entity_orther():
	a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
	if a == "s":
		b = input("Nome do Arquivo: ")
		c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
		if c == "txt":
			f = open(b + ".txt", "w")
			for y in cl.input():
				if "NP00V00" in y:
					f.write(f"{y}\n")
			f.close()
		elif c == "csv":
			f = open(b + ".csv", "w")
			for y in cl.input():
				if "NP00V00" in y:
					f.write(f"{y}\n")
			f.close()
		else:
			print("ERRO: Formato Inválido.")
			print("Não foi possível gerar o resultado.")
	elif a == "n":    
		for y in cl.input():
			if "NP00V00" in y:
				print(y)
	else:
		for y in cl.input():
			if "NP00V00" in y:
				print(y) 
				

def entities_main():    
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


def entity_np_main():    
	ent_list = []
	z = input('''Digite "allocc" para a lista de todas as PESSOAS por ordem de ocorrência. 
Digite (x) - um número inteiro - para a extração apenas das x PESSOAS mais recorrentes.\n''').lower()
	if z == "allocc":
		a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
		if a == "s":
			b = input("Nome do Arquivo: ")
			c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if "NP00SP0" in y:
						person_list.append(y)
				d = (Counter(person_list).most_common())
				for e in d:
					f.write(f"{e}\n")
				person_list = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if "NP00SP0" in y:
						person_list.append(y)
				d = (Counter(person_list).most_common())
				for e in d:
					f.write(f"{e}\n")
				person_list = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
				if "NP00SP0" in y:
					person_list.append(y)
						
			print(Counter(person_list).most_common())
			person_list = []
		else:
			for y in cl.input():
				if "NP00SP0" in y:
					person_list.append(y)
						
			print(Counter(person_list).most_common())
			person_list = []

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
						if "NP00SP0" in y:
							person_list.append(y)
					d = (Counter(person_list).most_common(z))
					for e in d:
						f.write(f"{e}\n")
					person_list = []
					f.close()
				elif c == "csv":
					f = open(b + ".csv", "w")
					for y in cl.input():
						if "NP00SP0" in y:
							person_list.append(y)
					d = (Counter(person_list).most_common(z))
					for e in d:
						f.write(f"{e}\n")
					person_list = []
					f.close()
				else:
					print("ERRO: Formato Inválido.")
					print("Não foi possível gerar o resultado.")

			elif a == "n":
				for y in cl.input():
					if "NP00SP0" in y:
						person_list.append(y)
						
				print(Counter(person_list).most_common(z))
				person_list = []
			else:
				for y in cl.input():
					if "NP00SP0" in y:
						person_list.append(y)
						
				print(Counter(person_list).most_common(z))
				person_list = []
		except:
			print("Por favor, digite 'allocc' ou apenas números inteiros.")


def entity_lc_main():    
	ent_list = []
	z = input('''Digite "allocc" para a lista de todas as PESSOAS por ordem de ocorrência. 
Digite (x) - um número inteiro - para a extração apenas das x PESSOAS mais recorrentes.\n''').lower()
	if z == "allocc":
		a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
		if a == "s":
			b = input("Nome do Arquivo: ")
			c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if "NP00G00" in y:
						person_list.append(y)
				d = (Counter(person_list).most_common())
				for e in d:
					f.write(f"{e}\n")
				person_list = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if "NP00G00" in y:
						person_list.append(y)
				d = (Counter(person_list).most_common())
				for e in d:
					f.write(f"{e}\n")
				person_list = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
				if "NP00G00" in y:
					person_list.append(y)
						
			print(Counter(person_list).most_common())
			person_list = []
		else:
			for y in cl.input():
				if "NP00G00" in y:
					person_list.append(y)
						
			print(Counter(person_list).most_common())
			person_list = []

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
						if "NP00G00" in y:
							person_list.append(y)
					d = (Counter(person_list).most_common(z))
					for e in d:
						f.write(f"{e}\n")
					person_list = []
					f.close()
				elif c == "csv":
					f = open(b + ".csv", "w")
					for y in cl.input():
						if "NP00G00" in y:
							person_list.append(y)
					d = (Counter(person_list).most_common(z))
					for e in d:
						f.write(f"{e}\n")
					person_list = []
					f.close()
				else:
					print("ERRO: Formato Inválido.")
					print("Não foi possível gerar o resultado.")

			elif a == "n":
				for y in cl.input():
					if "NP00G00" in y:
						person_list.append(y)
						
				print(Counter(person_list).most_common(z))
				person_list = []
			else:
				for y in cl.input():
					if "NP00G00" in y:
						person_list.append(y)
						
				print(Counter(person_list).most_common(z))
				person_list = []
		except:
			print("Por favor, digite 'allocc' ou apenas números inteiros.")
					

def entity_org_main():    
	ent_list = []
	z = input('''Digite "allocc" para a lista de todas as PESSOAS por ordem de ocorrência. 
Digite (x) - um número inteiro - para a extração apenas das x PESSOAS mais recorrentes.\n''').lower()
	if z == "allocc":
		a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
		if a == "s":
			b = input("Nome do Arquivo: ")
			c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if "NP00O00" in y:
						person_list.append(y)
				d = (Counter(person_list).most_common())
				for e in d:
					f.write(f"{e}\n")
				person_list = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if "NP00O00" in y:
						person_list.append(y)
				d = (Counter(person_list).most_common())
				for e in d:
					f.write(f"{e}\n")
				person_list = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
				if "NP00O00" in y:
					person_list.append(y)
						
			print(Counter(person_list).most_common())
			person_list = []
		else:
			for y in cl.input():
				if "NP00O00" in y:
					person_list.append(y)
						
			print(Counter(person_list).most_common())
			person_list = []

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
						if "NP00O00" in y:
							person_list.append(y)
					d = (Counter(person_list).most_common(z))
					for e in d:
						f.write(f"{e}\n")
					person_list = []
					f.close()
				elif c == "csv":
					f = open(b + ".csv", "w")
					for y in cl.input():
						if "NP00O00" in y:
							person_list.append(y)
					d = (Counter(person_list).most_common(z))
					for e in d:
						f.write(f"{e}\n")
					person_list = []
					f.close()
				else:
					print("ERRO: Formato Inválido.")
					print("Não foi possível gerar o resultado.")

			elif a == "n":
				for y in cl.input():
					if "NP00O00" in y:
						person_list.append(y)
						
				print(Counter(person_list).most_common(z))
				person_list = []
			else:
				for y in cl.input():
					if "NP00O00" in y:
						person_list.append(y)
						
				print(Counter(person_list).most_common(z))
				person_list = []
		except:
			print("Por favor, digite 'allocc' ou apenas números inteiros.")


def entity_orther_main():    
	ent_list = []
	z = input('''Digite "allocc" para a lista de todas as PESSOAS por ordem de ocorrência. 
Digite (x) - um número inteiro - para a extração apenas das x PESSOAS mais recorrentes.\n''').lower()
	if z == "allocc":
		a = input('''Gostaria de guardar a extração em um arquivo? 
s/S (sim) n/N (não): ''')
		if a == "s":
			b = input("Nome do Arquivo: ")
			c = input ("Formato (txt/TXT ou csv/CSV)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if "NP00V00" in y:
						person_list.append(y)
				d = (Counter(person_list).most_common())
				for e in d:
					f.write(f"{e}\n")
				person_list = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if "NP00V00" in y:
						person_list.append(y)
				d = (Counter(person_list).most_common())
				for e in d:
					f.write(f"{e}\n")
				person_list = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
				if "NP00V00" in y:
					person_list.append(y)
						
			print(Counter(person_list).most_common())
			person_list = []
		else:
			for y in cl.input():
				if "NP00V00" in y:
					person_list.append(y)
						
			print(Counter(person_list).most_common())
			person_list = []

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
						if "NP00V00" in y:
							person_list.append(y)
					d = (Counter(person_list).most_common(z))
					for e in d:
						f.write(f"{e}\n")
					person_list = []
					f.close()
				elif c == "csv":
					f = open(b + ".csv", "w")
					for y in cl.input():
						if "NP00V00" in y:
							person_list.append(y)
					d = (Counter(person_list).most_common(z))
					for e in d:
						f.write(f"{e}\n")
					person_list = []
					f.close()
				else:
					print("ERRO: Formato Inválido.")
					print("Não foi possível gerar o resultado.")

			elif a == "n":
				for y in cl.input():
					if "NP00V00" in y:
						person_list.append(y)
						
				print(Counter(person_list).most_common(z))
				person_list = []
			else:
				for y in cl.input():
					if "NP00V00" in y:
						person_list.append(y)
						
				print(Counter(person_list).most_common(z))
				person_list = []
		except:
			print("Por favor, digite 'allocc' ou apenas números inteiros.")			



def entities_all_clean():    
	ent_list = []
	z = input('''Digite "allocc" para a lista de todas as PESSOAS por ordem de ocorrência. 
Digite (x) - um número inteiro - para a extração apenas das x PESSOAS mais recorrentes.\n''').lower()
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
						if k not in lemmas_clean and k not in light_words_pt and k not in stop_words_pt:
							ent_list.append(y)
				d = (Counter(ent_list).most_common())
				for e in d:
					f.write(f"{e}\n")
				ent_list = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if y != "":
						k, l, m = y.split()
						if k not in lemmas_clean and k not in light_words_pt and k not in stop_words_pt:
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
				if y != "":
					k, l, m = y.split()
					if k not in lemmas_clean and k not in light_words_pt and k not in stop_words_pt:
						ent_list.append(y)
						
			print(Counter(ent_list).most_common())
			ent_list = []
		else:
			for y in cl.input():	
				if y != "":
					k, l, m = y.split()
					if k not in lemmas_clean and k not in light_words_pt and k not in stop_words_pt:
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
						if y != "":
							k, l, m = y.split()
							if k not in lemmas_clean and k not in light_words_pt and k not in stop_words_pt:
								ent_list.append(y)
					d = (Counter(ent_list).most_common(z))
					for e in d:
						f.write(f"{e}\n")
					ent_list = []
					f.close()
				elif c == "csv":
					f = open(b + ".csv", "w")
					for y in cl.input():
						if y != "":
							k, l, m = y.split()
							if k not in lemmas_clean and k not in light_words_pt and k not in stop_words_pt:
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
					if y != "":
						k, l, m = y.split()
						if k not in lemmas_clean and k not in light_words_pt and k not in stop_words_pt:
							ent_list.append(y)
						
				print(Counter(ent_list).most_common(z))
				ent_list = []
			else:
				for y in cl.input():	
					if y != "":
						k, l, m = y.split()
						if k not in lemmas_clean and k not in light_words_pt and k not in stop_words_pt:
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
	elif x == "entities":
		y = input(
'''Digite "allent" para a extração de todas as entidadades.
Digite "entmain" para a extração das entidades (dado suas ocorrências).\n''').lower()
		if y == "allent":
			entities()
			print("\n")
			continue
		elif y == "entmain":
			entities_main()
			print("\n")
			continue
	elif x == "entity_person":
		y = input(
'''Digite "allnp" para a extração de todas as entidadades referentes à PESSOAS.
Digite "npmain" para a extração das entidadades referentes à PESSOAS (dado suas ocorrências).\n''').lower()
		if y == "allnp":
			entity_np()
			print("\n")
			continue
		elif y == "npmain":
			entity_np_main()
			print("\n")
			continue
	elif x == "entity_local":
		y = input(
'''Digite "alllc" para a extração de todas as entidadades referentes à LUGARES.
Digite "lcmain" para a extração das entidadades referentes à LUGARES (dado suas ocorrências).\n''').lower()
		if y == "alllc":
			entity_lc()
			print("\n")
			continue
		elif y == "lcmain":
			entity_lc_main()
			print("\n")
			continue
	elif x == "entity_org":
		y = input(
'''Digite "allorg" para a extração de todas as entidadades referentes à ORGANIZAÇÕES.
Digite "orgmain" para a extração das entidadades referentes à ORGANIZAÇÕES (dado suas ocorrências).\n''').lower()
		if y == "allorg":
			entity_org()
			print("\n")
			continue
		elif y == "orgmain":
			entity_org_main()
			print("\n")
			continue
	elif x == "entity_orther":
		y = input(
'''Digite "allotr" para a extração de todas as entidadades referentes à OUTROS.
Digite "otrmain" para a extração das entidadades referentes à OUTROS (dado suas ocorrências).\n''').lower()
		if y == "allotr":
			entity_orther()
			print("\n")
			continue
		elif y == "otrmain":
			entity_orther_main()
			print("\n")
			continue
	elif x == "entities_clean":
		y = input(
'''Digite "allclean" para a extração de todas as entidadades com exceção das stopwords e pontuações e <blank>.
Digite "cleanmain" para a extração de todas as entidadades com exceção das stopwords e pontuações e <blank> (dado suas ocorrências).\n''').lower()
		if y == "allclean":
			entities_cl_stop()
			print("\n")
			continue
		elif y == "cleanmain":
			entities_all_clean()
			print("\n")
			continue
	elif x == "exit":
		break
	else:
		pass
class biblioteca():
	'''em ambas as funções, o objetivo é retornar o erro absoluto 
	e o erro relativo com a precisão de 4 algarismos significativos'''
	def erro_absoluto(self,valor,aprox):
		self.valor = valor
		self.aproximado = aprox
		return(float(f"{abs(self.valor-self.aproximado):.4g}"))
	def erro_relativo(self,valor,aprox):
		self.valor = valor
		self.aproximado = aprox
		resposta = abs(self.valor-self.aproximado)/abs(self.valor)
		return(float(f"{resposta:.4g}"))
		

	
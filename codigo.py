import random

class Page:
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
        return self.data

class GerenciadorMemoria:
    def __init__(self):
        self.ram = [None] * 4
        self.hd = [None] * 6
        
        self.hd[0] = Page("PARTE 1 DE A")
        self.hd[1] = Page("PARTE 2 DE A")
        self.ram[0] = Page("PARTE 3 DE A")
        
        self.hd[2] = Page("PARTE 1 DE B")
        self.hd[3] = Page("PARTE 2 DE B")
        self.hd[4] = Page("PARTE 3 DE B")
        self.hd[5] = Page("PARTE 4 DE B")
        
        self.ram[1] = Page("PARTE 1 DE C")
        self.ram[2] = Page("PARTE 2 DE C")
        self.ram[3] = Page("PARTE 3 DE C")
    
    def page_in(self, indice_hd):
        if not 0 <= indice_hd < len(self.hd):
            print("Índice do HD inválido")
            return
            
        indice_ram = random.randint(0, len(self.ram) - 1)
        
        self.ram[indice_ram], self.hd[indice_hd] = self.hd[indice_hd], self.ram[indice_ram]
        
        return indice_ram

    def referenciar_pagina(self, indice_ram):
        if not 0 <= indice_ram < len(self.ram):
            print("Índice da RAM inválido")
            return
            
        if self.ram[indice_ram] is None:
            print("Nenhuma página neste índice da RAM")
            return
            
        print(f"Página referenciada: {self.ram[indice_ram]}")

    def exibir_memoria(self):
        self._imprimir_cabecalho(" MEMÓRIA RAM ATUAL ", len(self.ram))
        for i, pagina in enumerate(self.ram):
            print(f"| {str(pagina):<15} ", end="")
        print("|\n+" + "-" * (17 * len(self.ram) + len(self.ram) - 1) + "+")
        
        self._imprimir_cabecalho(" MEMÓRIA HDD ATUAL ", len(self.hd))
        for i, pagina in enumerate(self.hd):
            print(f"| {str(pagina):<15} ", end="")
        print("|\n+" + "-" * (17 * len(self.hd) + len(self.hd) - 1) + "+")

    def _imprimir_cabecalho(self, titulo, tamanho):
        print(titulo)
        print("+" + "-" * (17 * tamanho + tamanho - 1) + "+")
        for i in range(tamanho):
            print(f"| {'Índice ' + str(i):<15} ", end="")
        print("|\n+" + "-" * (17 * tamanho + tamanho - 1) + "+")

def main():
    gerenciador = GerenciadorMemoria()
    
    while True:
        print("\n+----------------- MENU ------------------+")
        print("| 1 - REALIZAR PAGE IN ")
        print("| 2 - REFERENCIAR QUADRO DA RAM ")
        print("| 3 - VISUALIZAR RAM E DISCO ATUALMENTE ")
        print("| 0 - SAIR ")
        print("+-----------------------------------------+")
        
        try:
            opcao = int(input("O que deseja fazer? "))
            
            if opcao == 0:
                break
                
            elif opcao == 1:
                indice_hd = int(input(f"Qual índice do disco será usada no page in? 0 a {len(gerenciador.hd)-1} "))
                print(f"A página atualmente associada a esse índice do disco é: {gerenciador.hd[indice_hd]}")
                print("O algoritmo está selecionando página da RAM para ser substituída...")
                
                indice_selecionado = gerenciador.page_in(indice_hd)
                print(f"O índice escolhido pelo algoritmo para sair da RAM foi: {indice_selecionado}")
                
            elif opcao == 2:
                indice_ram = int(input(f"Qual índice da RAM será referenciado? 0 a {len(gerenciador.ram)-1} "))
                gerenciador.referenciar_pagina(indice_ram)
                
            elif opcao == 3:
                gerenciador.exibir_memoria()
                
            else:
                print("Opção inválida!")
                
        except ValueError:
            print("Por favor, insira um número válido")
            
if __name__ == "__main__":
    main()

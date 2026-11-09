class GrafoListaArestas:
    def __init__(self, dir=True):
        self.vertices = []  
        self.arestas = []   
        self.dir = dir

    def inserir_vertice(self, v):
        if v not in self.vertices:
            self.vertices.append(v)
            print(f"Vertice '{v}' inserido com sucesso")
        else:
            print(f"Vertice '{v}' ja existe")

    def remover_vertice(self, v):
        if v not in self.vertices:
            print(f"Vertice '{v}' nao encontrado")
            return
        
        self.vertices.remove(v)
        
        self.arestas = [aresta for aresta in self.arestas if aresta[0] != v and aresta[1] != v]
        print(f"Vertice '{v}' e suas arestas foram removidos")

    def inserir_aresta(self, u, v, peso=1):
        if u not in self.vertices or v not in self.vertices:
            print(f"Ambos os vertices ({u}, {v}) precisam existir")
            return
            
        for aresta in self.arestas:
            if aresta[0] == u and aresta[1] == v:
                print(f"Aresta ({u} ---> {v}) ja existe")
                return

        self.arestas.append((u, v, peso))
        print(f"Aresta ({u} ---> {v}) inserida")

        if not self.dir:
            self.arestas.append((v, u, peso))

    def remover_aresta(self, u, v):
        encontrou = False
        arestas_restantes = []
        
        for aresta in self.arestas:
            if aresta[0] == u and aresta[1] == v:
                encontrou = True
            elif not self.dir and aresta[0] == v and aresta[1] == u:
                pass  
            else:
                arestas_restantes.append(aresta)
                
        if encontrou:
            self.arestas = arestas_restantes
            print(f"Aresta ({u} --> {v}) removida")
        else:
            print(f"Aresta ({u} --> {v}) nao existe")

    def exibir_graus(self):
        if not self.vertices:
            print("O grafo esta vazio.")
            return

        print("\n--- Grau dos Vertices ---")
        for v in self.vertices:
            grau_saida = sum(1 for aresta in self.arestas if aresta[0] == v)
            grau_entrada = sum(1 for aresta in self.arestas if aresta[1] == v)

            if self.dir:
                print(f"Vertice '{v}': Saida = {grau_saida} | Entrada = {grau_entrada} | Total = {grau_saida + grau_entrada}")
            else:
                print(f"Vertice '{v}': Grau = {grau_saida}")

    def existe_aresta(self, u, v, silencioso=False):
        existe = any(aresta[0] == u and aresta[1] == v for aresta in self.arestas)
        if not silencioso:
            print(f"Existe aresta ({u} -> {v})? {'SIM' if existe else 'NAO'}")
        return existe

    def listar_vizinhos(self, v):
        if v not in self.vertices:
            print(f"Vertice '{v}' nao encontrado.")
            return []

        vizinhos = [aresta[1] for aresta in self.arestas if aresta[0] == v]
        print(f"Vizinhos de '{v}' (Saida): {vizinhos}")
        return vizinhos

    def percurso_valido(self, sequencia_vertices):
        if not sequencia_vertices or len(sequencia_vertices) < 2:
            print("Percurso invalido: E necessario informar ao menos 2 vertices.")
            return False

        for i in range(len(sequencia_vertices) - 1):
            atual = sequencia_vertices[i]
            proximo = sequencia_vertices[i + 1]

            if atual not in self.vertices or proximo not in self.vertices:
                print(f"Percurso {' -> '.join(sequencia_vertices)}: INVALIDO (Vertice nao existe)")
                return False

            if not self.existe_aresta(atual, proximo, silencioso=True):
                print(f"Percurso {' -> '.join(sequencia_vertices)}: INVALIDO (Falha na transicao {atual} -> {proximo})")
                return False

        print(f"Percurso {' -> '.join(sequencia_vertices)}: VALIDO")
        return True

    def exibir_grafo(self):
        print("\n--- Lista de Arestas ---")
        if not self.vertices:
            print("(Grafo Vazio)")
            return
            
        print(f"Vertices: {', '.join(self.vertices)}")
        if not self.arestas:
            print("Arestas: Nenhuma")
        else:
            print("Arestas:")

            exibidas = []
            for u, v, peso in self.arestas:
                if not self.dir and (v, u) in exibidas:
                    continue
                print(f"  ({u}) --[{peso}]--> ({v})")
                exibidas.append((u, v))


def menu():
    print("\n" + "="*40)
    print("      CONFIGURACAO INICIAL DO GRAFO")
    print("="*40)
    tipo = input("Deseja criar um grafo direcionado? (s/n): ").strip().lower()
    dir = tipo != 'n'
    
    g = GrafoListaArestas(dir=dir)

    while True:
        print("\n" + "="*40)
        print("            MENU DE OPCOES")
        print("="*40)
        print("1. Inserir vertice")
        print("2. Remover vertice")
        print("3. Inserir aresta")
        print("4. Remover aresta")
        print("5. Exibir grau de todos os vertices")
        print("6. Verificar se existe uma aresta")
        print("7. Listar vizinhos de um vertice")
        print("8. Verificar se um percurso e possivel")
        print("9. Exibir estrutura do grafo")
        print("0. Sair")
        print("="*40)

        opcao = input("Escolha uma opcao (0-9): ").strip()

        if opcao == "1":
            v = input("Digite o nome do vertice: ").strip()
            if v: g.inserir_vertice(v)
        elif opcao == "2":
            v = input("Digite o nome do vertice a remover: ").strip()
            if v: g.remover_vertice(v)
        elif opcao == "3":
            u = input("Vertice de origem: ").strip()
            v = input("Vertice de destino: ").strip()
            if u and v: g.inserir_aresta(u, v)
        elif opcao == "4":
            u = input("Vertice de origem: ").strip()
            v = input("Vertice de destino: ").strip()
            if u and v: g.remover_aresta(u, v)
        elif opcao == "5":
            g.exibir_graus()
        elif opcao == "6":
            u = input("Vertice de origem: ").strip()
            v = input("Vertice de destino: ").strip()
            if u and v: g.existe_aresta(u, v)
        elif opcao == "7":
            v = input("Digite o nome do vertice: ").strip()
            if v: g.listar_vizinhos(v)
        elif opcao == "8":
            entrada = input("Digite a sequencia de vertices separada por espaco (ex: A B C D): ").strip()
            if entrada:
                percurso = entrada.split()
                g.percurso_valido(percurso)
        elif opcao == "9":
            g.exibir_grafo()
        elif opcao == "0":
            print("\nSaindo do programa. Ate logo!")
            break
        else:
            print("Opcao invalida! Tente novamente.")


if __name__ == "__main__":
    menu()
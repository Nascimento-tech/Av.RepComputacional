class GrafoListaAdjacencia:
    def __init__(self, direcionado=False):
        self.adj = {}
        self.direcionado = direcionado

    def inserir_vertice(self, vertice):
        if vertice not in self.adj:
            self.adj[vertice] = []
        else:
            print("Esse vertice ja existe.")

    def inserir_aresta(self, origem, destino):
        if origem not in self.adj or destino not in self.adj:
            print("Cadastre os dois vertices primeiro.")
            return

        if destino not in self.adj[origem]:
            self.adj[origem].append(destino)
        if not self.direcionado and origem not in self.adj[destino]:
            self.adj[destino].append(origem)

    def exibir_grafo(self):
        for vertice in self.adj:
            print(vertice, "->", self.adj[vertice])

    def busca_em_largura(self, origem):
        if origem not in self.adj:
            print("Vertice nao encontrado.")
            return []

        fila = [origem]
        visitados = [origem]
        ordem = []

        while fila:
            atual = fila.pop(0)
            ordem.append(atual)

            for vizinho in self.adj[atual]:
                if vizinho not in visitados:
                    visitados.append(vizinho)
                    fila.append(vizinho)

        print("Busca em largura:", ordem)
        return ordem

    def menor_caminho(self, origem, destino):
        if origem not in self.adj or destino not in self.adj:
            print("Vertice nao encontrado.")
            return []

        fila = [origem]
        anterior = {origem: None}

        while fila:
            atual = fila.pop(0)

            if atual == destino:
                caminho = [destino]
                # Volta do destino ate a origem pelos vertices anteriores.
                while atual != origem:
                    atual = anterior[atual]
                    caminho.append(atual)
                caminho.reverse()
                print("Menor caminho:", caminho)
                print("Quantidade de arestas:", len(caminho) - 1)
                return caminho

            for vizinho in self.adj[atual]:
                if vizinho not in anterior:
                    anterior[vizinho] = atual
                    fila.append(vizinho)

        print("Nao existe caminho entre esses vertices.")
        return []


def menu():
    tipo = input("Grafo direcionado? (s/n): ").strip().lower()
    grafo = GrafoListaAdjacencia(direcionado=tipo == "s")

    while True:
        print("\n1 - Inserir vertice")
        print("2 - Inserir aresta")
        print("3 - Exibir grafo")
        print("4 - Busca em largura")
        print("5 - Menor caminho")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            vertice = input("Vertice: ").strip()
            if vertice:
                grafo.inserir_vertice(vertice)
        elif opcao == "2":
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            grafo.inserir_aresta(origem, destino)
        elif opcao == "3":
            grafo.exibir_grafo()
        elif opcao == "4":
            origem = input("Origem: ").strip()
            grafo.busca_em_largura(origem)
        elif opcao == "5":
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            grafo.menor_caminho(origem, destino)
        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    menu()

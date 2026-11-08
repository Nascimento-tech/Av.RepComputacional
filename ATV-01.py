class Grafo:
    def __init__(self, dir=True):
        self.adj = {}
        self.dir = dir

    def inserir_vertice(self, v):
        if v not in self.adj:
            self.adj[v] = {}
            print(f"Vertice '{v}' inserido com sucesso")
        else:
            print(f"Vertice '{v}' ja existe")

    def remover_vertice(self, v):
        if v not in self.adj:
            print(f"Vertice {v} nao encontrado")
            return
        del self.adj[v]
        for vertice in self.adj:
            if v in self.adj[vertice]:
                del self.adj[vertice][v]

        print(f"Vertice '{v}' e suas arestas foram removidos")

    def inserir_aresta(self, u, v, peso=1):
        if u not in self.adj or v not in self.adj:
            print(f"Ambos os vertices ({u}, {v}) precisam existir")
            return

        self.adj[u][v] = peso
        print(f"Aresta ({u} ---> {v}) inserida")

        if not self.dir:
            self.adj[v][u] = peso

    def remover_aresta(self, u, v):
        if u in self.adj and v in self.adj[u]:
            del self.adj[u][v]
            print(f"Aresta ({u} --> {v}) removida")
            if not self.dir and u in self.adj[v]:
                del self.adj[v][u]
        else:
            print(f"Aresta ({u} --> {v}) nao existe")

    def exibir_graus(self):
        if not self.adj:
            print("O grafo esta vazio.")
            return

        print("\n--- Grau dos Vertices ---")
        for v in self.adj:
            grau_saida = len(self.adj[v])
            grau_entrada = sum(1 for u in self.adj if v in self.adj[u])

            if self.dir:
                print(f"Vertice '{v}': Saida = {grau_saida} | Entrada = {grau_entrada} | Total = {grau_saida + grau_entrada}")
            else:
                print(f"Vertice '{v}': Grau = {grau_saida}")

    def existe_aresta(self, u, v):
        existe = u in self.adj and v in self.adj[u]
        print(f"Existe aresta ({u} -> {v})? {'SIM' if existe else 'NAO'}")
        return existe

    def listar_vizinhos(self, v):
        if v not in self.adj:
            print(f"Vertice '{v}' nao encontrado.")
            return []

        vizinhos = list(self.adj[v].keys())
        print(f"Vizinhos de '{v}' (Saida): {vizinhos}")
        return vizinhos

    def percurso_valido(self, sequencia_vertices):
        if not sequencia_vertices or len(sequencia_vertices) < 2:
            print("Percurso invalido: E necessario informar ao menos 2 vertices.")
            return False

        for i in range(len(sequencia_vertices) - 1):
            atual = sequencia_vertices[i]
            proximo = sequencia_vertices[i + 1]

            if atual not in self.adj or proximo not in self.adj[atual]:
                print(f"Percurso {' -> '.join(sequencia_vertices)}: INVALIDO (Falha na transicao {atual} -> {proximo})")
                return False

        print(f"Percurso {' -> '.join(sequencia_vertices)}: VALIDO")
        return True

    def exibir_grafo(self):
        print("\n--- Estrutura Atual do Grafo ---")
        if not self.adj:
            print("(Grafo Vazio)")
        for vertice, vizinhos in self.adj.items():
            print(f"  {vertice} -> {list(vizinhos.keys())}")


def menu():
    print("\n" + "="*40)
    print("      CONFIGURACAO INICIAL DO GRAFO")
    print("="*40)
    tipo = input("Deseja criar um grafo direcionado? (s/n): ").strip().lower()
    dir = tipo != 'n'

    g = Grafo(dir=dir)

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
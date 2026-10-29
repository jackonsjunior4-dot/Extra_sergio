
import random


class ListaDividida:
    def __init__(self, tamanho_inicial=1024, semente=42):
        self.regiao_ordenada = sorted(
            random.Random(semente).sample(range(100001), tamanho_inicial)
        )
        self.cauda = []

    def inserir(self, chave):
        if not isinstance(chave, int) or isinstance(chave, bool):
            return False, "Digite um número inteiro."

        if chave in self.regiao_ordenada or chave in self.cauda:
            return False, "Esse número já existe!"

        self.cauda.append(chave)

        if len(self.cauda) == 10:
            self.intercalar()

        return True, "Número inserido com sucesso!"

    def busca_binaria(self, chave):
        esquerda = 0
        direita = len(self.regiao_ordenada) - 1
        iteracoes = 0

        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            iteracoes += 1

            if self.regiao_ordenada[meio] == chave:
                return True, iteracoes

            if self.regiao_ordenada[meio] < chave:
                esquerda = meio + 1
            else:
                direita = meio - 1

        return False, iteracoes

    def busca_sequencial(self, chave):
        iteracoes = 0

        for numero in self.cauda:
            iteracoes += 1

            if numero == chave:
                return True, iteracoes

        return False, iteracoes

    def buscar(self, chave):
        encontrou, iteracoes_binarias = self.busca_binaria(chave)

        if encontrou:
            return {
                "encontrou": True,
                "local": "Região ordenada",
                "binaria": iteracoes_binarias,
                "sequencial": 0,
                "total": iteracoes_binarias
            }

        encontrou, iteracoes_sequenciais = self.busca_sequencial(chave)

        return {
            "encontrou": encontrou,
            "local": "Cauda" if encontrou else "Não encontrada",
            "binaria": iteracoes_binarias,
            "sequencial": iteracoes_sequenciais,
            "total": iteracoes_binarias + iteracoes_sequenciais
        }

    def intercalar(self):
        cauda_ordenada = sorted(self.cauda)
        resultado = []
        i = 0
        j = 0

        while i < len(self.regiao_ordenada) and j < len(cauda_ordenada):
            if self.regiao_ordenada[i] <= cauda_ordenada[j]:
                resultado.append(self.regiao_ordenada[i])
                i += 1
            else:
                resultado.append(cauda_ordenada[j])
                j += 1

        resultado.extend(self.regiao_ordenada[i:])
        resultado.extend(cauda_ordenada[j:])

        self.regiao_ordenada = resultado
        self.cauda = []

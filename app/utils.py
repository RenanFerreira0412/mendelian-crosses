from itertools import product


class Utils:
    @classmethod
    def reverse_str(cls, string):
        if string[0].islower() and string[-1].isupper():
            return string[::-1]  # Inverte a string usando slice
        return string

    @classmethod
    def sep_character(cls, gene):
        l = len(gene)
        vet = []

        for i in range(0, l, 2):
            vet.append(list(gene)[i:i+2])

        return vet

    @classmethod
    def combine_character(cls, character1, character2, n):
        result = [None] * n
        for i in range(n):
            # Realiza as combinações
            combinations = [''.join(comb)
                            for comb in product(character1[i], character2[i])]

            # Inverte as combinações que começam com letras minúsculas e terminam com letras maiúsculas
            final_combinations = [cls.reverse_str(
                string) for string in combinations]

            # Armazena as combinações
            result[i] = final_combinations

        return result

    @classmethod
    def genetic_cross(cls, comb):
        # Realiza a combinação entre todos os genótipos possíveis desse cruzamento
        result = [''.join(comb) for comb in product(*comb)]

        return result

    @classmethod
    def cal_probability(cls, genotypes, n):
        genotype = {}

        # Quantidade total de genótipos
        total = 4*pow(4, n-1)

        for g in genotypes:
            if g in genotype:
                genotype[g] += 1 / total * 100
            else:
                genotype[g] = 1 / total * 100

        return genotype

from flask import render_template, request, redirect, url_for
from app.main import main
from app.utils import Utils

# página inicial


@main.route('/')
def index():
    return render_template('index.html')


# documentação sobre as leis de mendel
@main.route('/leis-de-mendel')
def laws():
    return render_template('laws.html')


# formulário para o cruzamento genético
@main.route('/form')
def form():
    return render_template('form.html')

@main.route('/result')
def result():
    return render_template('result.html')


# realizando o cruzamento genético
@main.route('/form', methods=['POST'])
def form_post():
    genotype1 = request.form.get('genotype1')
    genotype2 = request.form.get('genotype2')

    print(genotype1)
    print(genotype2)

    # Vetor que armazena cada característica
    character_gene_1 = Utils.sep_character(genotype1)
    character_gene_2 = Utils.sep_character(genotype2)

    # quantidade de características observadas
    n = len(character_gene_1)

    # Cruzamento de cada característica
    comb = Utils.combine_character(character_gene_1, character_gene_2, n)

    # Cruzamento de todas as possíveis combinações
    result = Utils.genetic_cross(comb)
    # print(result)

    # Cálculo da probabilidade de cada genótipo
    probability = Utils.cal_probability(result, n)

    print(probability)

    return render_template('result.html',  result=probability)

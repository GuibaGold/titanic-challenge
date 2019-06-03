import numpy as numpy
import pandas as panda


def limpar_dados(dados):
    dados["Fare"] = dados["Fare"].fillna(dados["Fare"].dropna().median())
    dados["Age"] = dados["Age"].fillna(dados["Age"].dropna().median())


    dados.loc[dados["Sex"] == "male", "Sex"] = 0
    dados.loc[dados["Sex"] == "female", "Sex"] = 1

    dados["Embarked"] = dados["Embarked"].fillna("S")
    dados.loc[dados["Embarked"] == "S", "Embarked"] = 0
    dados.loc[dados["Embarked"] == "C", "Embarked"] = 1
    dados.loc[dados["Embarked"] == "Q", "Embarked"] = 2

def escrever_previsao(previsao, nome):
    IdPassageiro = numpy.array(teste["PassengerId"]).astype(int)
    solucao = panda.DataFrame(previsao, IdPassageiro, columns = ["Survived"])
    solucao.to_csv(nome, index_label = ["PassengerId"])
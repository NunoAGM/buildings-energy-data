# Como usar
Este repositório permite trabalhar com dados do projeto **End-Use Load Profiles for the U.S. Building Stock (NREL)** de forma modular.
O processo está dividido em três passos independentes:

## Passo 1 — Filtrar edifícios com PV + EV
1. O utilizador faz download manual do ficheiro `upgradeXX.csv` do portal NREL/ResStock  
2. Executa o script: _python src/step1_filter_buildings.py_
   
**Resultado**: 
É criado o ficheiro `filtered_buildings.csv`, contendo apenas edifícios que:
- têm painéis solares (PV)
- têm carregador para veículo elétrico (EV)

## Passo 2 — Descarregar perfis horários
1. Descarregar os ficheiros `.parquet` (um por edifício)
2. Executa: _python src/step2_download_timeseries.py_
   
**Resultado**: 
Os ficheiros são descarregados automaticamente do **NREL OEDI Data Lake**.

## Passo 3 — Exportar informações
1. Se quiser guardar uma tabela com os edifícios filtrados e estado dos downloads
2. Executa: _python src/step3_export_metadata.py_
**Resultado**: 
Será gerado o ficheiro `data_infos.xlsx`.

---


# How to use

This repository enables working with the **End-Use Load Profiles for the U.S. Building Stock (NREL)** dataset in a modular workflow.  
The process is divided into three independent steps:

## Step 1 — Filter buildings with PV + EV

1. The user manually downloads the `upgradeXX.csv` file from the NREL/ResStock portal  
2. Run the script: _python src/step1_filter_buildings.py_
   
**Result:**  
A file named `filtered_buildings.csv` is generated, containing only buildings that:

- have solar photovoltaic panels (PV)
- have an electric vehicle charger (EV)

## Step 2 — Download time-series data

1. Time-series `.parquet` files are downloaded (one per building)
2. Run: _python src/step2_download_timeseries.py_
   
**Result:**  
The files are automatically downloaded from the **NREL OEDI Data Lake**.


## Step 3 — Export metadata

1. If you want to save a table with the filtered buildings and their download status
2. Run: _python src/step3_export_metadata.py_

**Result:**  
An Excel file named `data_infos.xlsx` will be generated.

---





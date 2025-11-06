# 📊 Buildings Energy Data — End-Use Load Profiles for the U.S. Building Stock

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Data Source](https://img.shields.io/badge/Data-NREL-yellow)
![License](https://img.shields.io/badge/License-Restricted-lightgrey)

---

**🌐 PT**

### 🏢 Descrição

Este repositório contém código em **Python** para **recolha automática e processamento** de dados de perfis horários de consumo energético em edifícios nos Estados Unidos.  
Os dados são provenientes do projeto **"End-Use Load Profiles for the U.S. Building Stock"** desenvolvido pelo **NREL — National Renewable Energy Laboratory**.

> ⚠️ **Nota:** Este repositório *não* inclui os dados originais.  
> Inclui apenas o código Python que descarrega, organiza e prepara os dados para análise.

---

### 🔍 Sobre o dataset

O dataset contém perfis horários de consumo energético para edifícios residenciais e comerciais, úteis para:

- Estudos de eficiência energética
- Modelação de carga e eletrificação
- Planeamento de rede elétrica

Mais informações:  
https://www.nrel.gov/buildings/end-use-load-profiles

---

### 🔧 Funcionalidades do repositório

- Descarregamento automático dos dados (API / endpoint do NREL)
- Processamento e organização dos ficheiros
- Exportação para formatos de análise (CSV, Parquet, etc.)

---

### 📁 Estrutura do repositório
```
/
├── src/
│   └── data_collection.py      
├── docs/
│   └── references/
├── README.md
└── requirements.txt
```


---

### 🚀 Como utilizar

1. Instalar dependências
  - pip install -r requirements.txt
2. Executar o script
  - python src/data_collection.py



---

### 🧾 Citação (copiável)

Se utilizar os dados ou este repositório, cite conforme recomendado pelo NREL:

Wilson et al. 2021. End-Use Load Profiles for the U.S. Building Stock: Methodology and Results of Model Calibration, Validation, and Uncertainty Quantification. NREL/TP-5500-80889. https://www.nrel.gov/docs/fy22osti/80889.pdf

Para o dataset comercial (ComStock):

Parker, Andrew, et al. 2023. ComStock Reference Documentation. Golden, CO: National Renewable Energy Laboratory. NREL/TP-5500-83819. https://www.nrel.gov/docs/fy23osti/83819.pdf

---

### 📄 Licença (copiável)

Os dados pertencem ao **National Renewable Energy Laboratory (NREL)**.  
O uso dos dados deve seguir os termos definidos em:

https://www.nrel.gov/buildings/end-use-load-profiles

Este repositório **apenas disponibiliza o código** utilizado na recolha e preparação dos dados.  
Os dados originais **não são redistribuídos**.

---

### ✉️ Contacto

Para dúvidas ou sugestões, abre um *Issue* neste repositório.

---

---

**🌐 EN**

### 🏢 Description

This repository contains **Python code** for automated **download and preprocessing** of hourly energy load profile data for U.S. buildings.  
The data comes from the project **"End-Use Load Profiles for the U.S. Building Stock"** developed by the **National Renewable Energy Laboratory (NREL)**.

> ⚠️ **Note:** The dataset is *not* stored in this repository.  
> Only the Python code used to download and process it is included.

---

### 🔍 Dataset overview

The dataset provides hourly load profiles for residential and commercial buildings, supporting:

- Energy efficiency studies
- Electrification modeling
- Grid planning and forecasting

More info:  
https://www.nrel.gov/buildings/end-use-load-profiles

---

### 🔧 Repository features

- Automatic dataset download (via NREL API / endpoints)
- Data processing and organization
- Export to analysis-ready formats (CSV, Parquet, etc.)

---

### 📁 Repository structure
```
/
├── src/
│   └── data_collection.py      
├── docs/
│   └── references/
├── README.md
└── requirements.txt
```

---

### 🚀 How to use

1. Install dependencies
  - pip install -r requirements.txt
2. Run the script
  - python src/data_collection.py


---

### 🧾 Citation (copy-friendly)

Wilson et al. 2021. *End-Use Load Profiles for the U.S. Building Stock: Methodology and Results of Model Calibration, Validation, and Uncertainty Quantification.*  
NREL/TP-5500-80889. https://www.nrel.gov/docs/fy22osti/80889.pdf

ComStock reference:

Parker, Andrew, et al. 2023. *ComStock Reference Documentation.*  
NREL/TP-5500-83819. https://www.nrel.gov/docs/fy23osti/83819.pdf

---

### 📄 License (copy-friendly)

The dataset belongs to **National Renewable Energy Laboratory (NREL)**.  
Use of the dataset must follow the terms stated on:

https://www.nrel.gov/buildings/end-use-load-profiles

This repository **only provides the downloadable and processing code** —  
the dataset itself is **not redistributed**.

---

### ✉️ Contact

For questions or improvements, open an Issue in this repository.

---


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

📄 Para instruções completas de utilização, consulte:

👉 `USAGE.md`

---

### 🧾 Citação (copiável)

#### Citar o dataset NREL:

```
Wilson et al. 2021. End-Use Load Profiles for the U.S. Building Stock: Methodology and Results of Model Calibration, Validation, and Uncertainty Quantification. NREL/TP-5500-80889. https://www.nrel.gov/docs/fy22osti/80889.pdf
```

Dataset comercial / ComStock:

```
Parker, Andrew, et al. 2023. ComStock Reference Documentation. Golden, CO: National Renewable Energy Laboratory. NREL/TP-5500-83819. https://www.nrel.gov/docs/fy23osti/83819.pdf
```

#### Citar este repositório:

```
Mendes, Nuno A.G. (2025). Buildings Energy Data — End-Use Load Profiles for the U.S. Building Stock.
Repositório GitHub. Disponível em: https://github.com/NunoAGM/buildings-energy-data
```

BibTeX:

```bibtex
@software{mendes_energy_data_2025,
  author       = {Nuno A. G. Mendes},
  title        = {Buildings Energy Data — End-Use Load Profiles for the U.S. Building Stock},
  year         = {2025},
  publisher    = {GitHub},
  url          = {https://github.com/NunoAGM/buildings-energy-data},
}
```

---

### 📄 Licença (copiável)

Os dados pertencem ao **National Renewable Energy Laboratory (NREL)**.  
O uso dos dados deve seguir os termos definidos em:

https://www.nrel.gov/buildings/end-use-load-profiles

Este repositório **apenas disponibiliza o código** utilizado na recolha e preparação dos dados.  
Os dados originais **não são redistribuídos**.

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

📄 For full usage instructions, please check:

👉 `USAGE.md`

---

### 🧾 Citation (copy-friendly)

#### Cite the NREL dataset:

```
Wilson et al. 2021. End-Use Load Profiles for the U.S. Building Stock: Methodology and Results of Model Calibration, Validation, and Uncertainty Quantification.
NREL/TP-5500-80889. https://www.nrel.gov/docs/fy22osti/80889.pdf
```

ComStock dataset reference:

```
Parker, Andrew, et al. 2023. ComStock Reference Documentation.
NREL/TP-5500-83819. https://www.nrel.gov/docs/fy23osti/83819.pdf
```

#### Cite this repository:

```
Mendes, Nuno A.G. (2025). Buildings Energy Data — End-Use Load Profiles for the U.S. Building Stock.
GitHub repository. Available at: https://github.com/NunoAGM/buildings-energy-data
```

BibTeX:

```bibtex
@software{mendes_energy_data_2025,
  author       = {Nuno A. G. Mendes},
  title        = {Buildings Energy Data — End-Use Load Profiles for the U.S. Building Stock},
  year         = {2025},
  publisher    = {GitHub},
  url          = {https://github.com/NunoAGM/buildings-energy-data},
}
```

---

### 📄 License (copy-friendly)

The dataset belongs to **National Renewable Energy Laboratory (NREL)**.  
Dataset usage must follow the terms stated at:

https://www.nrel.gov/buildings/end-use-load-profiles

This repository **only provides the download and processing code** —  
the dataset is **not redistributed**.


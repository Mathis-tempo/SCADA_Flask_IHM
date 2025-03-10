# SCADA_Flask_IHM

## Description
SCADA web interface developed with Flask for controlling and monitoring an automated sorting system.

## Project overview

![Project overview](./img/overview.png)


![Control panel](./img/control-panel.png)

## Functionalities
-  Real-time display of conveyor and sorter status
- ON/OFF control of each component
- Communication via Modbus TCP

## 🛠️ Technologies used
- **Backend**: Flask, python
- **Frontend**: HTML, CSS, JavaScript
- **Communication**: Modbus TCP

## Installation
```bash
git clone https://github.com/Mathis-tempo/SCADA_Flask_IHM.git
cd SCADA_Flask_IHM
pip install -r requirements.txt
```

## Run
```bash
python driver.py
```
The interface will be accessible at : `http://localhost:5000`

## 👤 Author
Mathis TEMPO
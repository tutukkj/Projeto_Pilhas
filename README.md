# 🤖 Sistema de Detecção de Objetos com YOLO e Integração ao Arduino

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![YOLO](https://img.shields.io/badge/YOLOv8-Ultralytics-FF6F00?style=for-the-badge&logo=yolo&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-Hardware-00979D?style=for-the-badge&logo=arduino&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Teste-yellow?style=for-the-badge)

Um sistema desenvolvido em **Python** para **detecção em tempo real de objetos** utilizando **YOLOv8** (Ultralytics) e **OpenCV**, com integração ao **Arduino** para envio de sinais em tempo real baseados no número de detecções.

---

## 🧠 Tecnologias Utilizadas

- **Python 3.10+** – Linguagem principal.  
- **OpenCV** – Captura de vídeo e renderização dos bounding boxes.  
- **YOLOv8 (Ultralytics)** – Modelo de detecção de objetos.  
- **PySerial** – Comunicação com o Arduino.  
- **Arduino** – Recepção de sinais e acionamento de periféricos.  

---

## 📸 Demonstração / Prints

<!-- Adicione capturas de tela ou GIFs do sistema rodando -->
![Detecção em tempo real](link-para-screenshot1.png)

---

## 🚀 Funcionalidades

1. **Detecção em tempo real**  
   - Captura imagens da webcam.  
   - Detecta objetos configurados no modelo YOLO.  
   - Exibe bounding boxes e probabilidades.

2. **Integração com Arduino**  
   - Envia via porta serial a contagem de objetos detectados a cada 5 segundos, apenas quando o valor muda.  

3. **Avisos Visuais**  
   - Exibe mensagem de alerta no frame quando objetos são detectados.  

4. **Interface simples**  
   - Pressione **`Q`** para encerrar a aplicação.

---

## 📂 Estrutura do Projeto

├── app.py # Script principal do sistema]

├── bestn.pt # Modelo YOLO treinado

├── bestm.pt # Modelo YOLO alternativo (Mais pesado)

├── README.md # Documentação

---

## ⚙️ Como Rodar o Sistema

### 2 Clone o repositório
```bash
git clone https://github.com/tutukkj/Projeto_Pilhas.git

```

### 2 Instale as dependências
```
pip install -r requirements.txt
```

### 3 Conecte o Arduino

* Certifique-se de alterar a porta serial correta no código:

```
arduino = serial.Serial("COM4", 9600, timeout=1)
```
---
### 📝 Integração com o Arduino

* O Arduino recebe a contagem de objetos detectados via porta serial a cada 5 segundos.

* Esse valor pode ser usado para acionar LEDs, buzzer ou outros periféricos conforme necessário.

---
### ✨ Autor

Desenvolvido por Arthur Nunes para aplicações de automação e visão computacional integrada a hardware.

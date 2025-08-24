import cv2
from ultralytics import YOLO
import time
import serial

arduino = serial.Serial("COM4", 9600, timeout=1)
time.sleep(2)  # Aguarda Arduino iniciar
  
# Carregar modelo
model = YOLO("bestn.pt")

# Iniciar webcam
cap = cv2.VideoCapture(1)
cap.set(3, 640)  # largura
cap.set(4, 480)  # altura

ultimo_aviso = 0
tempo_aviso = 2  
ultimo_envio = 0
intervalo_envio = 5  
ultimo_qtd = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.6)

    qtd_detectadas = 0

    for result in results:
        for box in result.boxes:
            conf = float(box.conf[0])
            label = model.names[int(box.cls[0])]

            # Contar todas as detecções com confiança > 0.70
            if conf > 0.70:
                qtd_detectadas += 1
                ultimo_aviso = time.time()

            # Mostrar bounding box se confiança > 0.60
            if conf > 0.60:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f'{label} {conf:.2f}', (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Aviso visual no frame
    if time.time() - ultimo_aviso < tempo_aviso and qtd_detectadas > 0:
        texto = f'Objetos detectados! ({qtd_detectadas} encontrados)'
        cv2.putText(frame, texto, (20, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # Enviar para Arduino a cada 5 segundos somente se mudou
    if time.time() - ultimo_envio >= intervalo_envio:
        if qtd_detectadas != ultimo_qtd:
            arduino.write(f"{qtd_detectadas}\n".encode("utf-8"))
            ultimo_qtd = qtd_detectadas
        ultimo_envio = time.time()

    cv2.imshow("Detecção de Objetos", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()

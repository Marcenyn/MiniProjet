import Adafruit_DHT
import time

# Choisissez le type de capteur (DHT11 ou DHT22)
SENSOR = Adafruit_DHT.DHT22  # ou Adafruit_DHT.DHT11

# Pin GPIO auquel le capteur est connecté
PIN = 4  # Exemple: GPIO 4

def lire_temperature_humidite():
    # Lire la température et l'humidité depuis le capteur
    humidite, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    
    if humidite is not None and temperature is not None:
        print(f"Température: {temperature:.2f}°C, Humidité: {humidite:.2f}%")
    else:
        print("Échec de la lecture du capteur. Réessayer...")
    
if __name__ == "__main__":
    while True:
        lire_temperature_humidite()
        time.sleep(2)  # Pause de 2 secondes avant la prochaine lecture
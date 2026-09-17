import logging
import os
import random
import time

# Garante que a pasta 'logs' exista antes de salvar o arquivo
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Cria um logger dedicado para a aplicação
logger = logging.getLogger(__name__)

errors = [
    "DATABASE_ERROR: Connection timed out to PostgreSQL on port 5432",
    "AUTH_ERROR: Invalid JWT Signature for user_id=9841",
    "PAYMENT_ERROR: Gateway Timeout from Stripe API",
]

print("Simulador de aplicação rodando... Pressione Ctrl+C para parar.")

while True:
    if random.random() < 0.3:
        err = random.choice(errors)
        logger.error(err)
        print(f"[ERRO GERADO]: {err}")
    else:
        logger.info("HTTP 200 - /api/v1/healthcheck OK")
    time.sleep(3)
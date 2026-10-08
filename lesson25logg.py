import logging

#

logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')


# darajalar
logging.debug("tafsilot")       # 10 < 30 → ko'rinmaydi
logging.info("axborot")         # 20 < 30 → ko'rinmaydi
logging.warning("diqqat!")      # 30 ≥ 30 → ✅ chiqadi
logging.error("xato!")         # 40 ≥ 30 → ✅ chiqadi
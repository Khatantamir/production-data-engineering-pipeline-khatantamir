import logging
from src.extract import extract
from src.transform import transform
from src.load import load

logging.basicConfig(level=logging.INFO)

def main():
    try:
        logging.info("Starting pipeline...")

        extract()
        logging.info("Data extracted")

        transform()
        logging.info("Data transformed")

        load()
        logging.info("Data loaded")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    main()

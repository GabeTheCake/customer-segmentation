from src.pipeline import CustomerSegmentationPipeline
from src.logger_config import setup_logger


def main():
    logger = setup_logger()
    logger.info("Iniciando pipeline de segmentação")

    pipeline = CustomerSegmentationPipeline(logger)
    pipeline.run()

    logger.info("Pipeline finalizado com sucesso")

if __name__ == "__main__":
    main()
from src.datascienceproject.config.configuration import ConfigurationManager
from src.datascienceproject.components.data_transformation import DataTransformation
from src.datascienceproject import logger

STAGE_NAME="Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config=ConfigurationManager()
        data_transfomration_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transfomration_config)
        data_transformation.train_test_splitting()

if __name__=='__main__':
    try:
        logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
        obj=DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<\n\nx=======================x")
    except Exception as e:
        logger.exception(e)
        raise e
from src.datascienceproject.config.configuration import ConfigurationManager
from src.datascienceproject.components.model_evaluator import ModelEvaluation
from src.datascienceproject import logger

STAGE_NAME="Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation_config=ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()

if __name__=='__main__':
    try:
        logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
        obj=ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<\n\nx=======================x")
    except Exception as e:
        logger.exception(e)
        raise e
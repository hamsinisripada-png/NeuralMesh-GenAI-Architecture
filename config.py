class ModelConfig:
    MODEL_NAME = "llama3"
    MAX_TOKENS = 2048
    TEMPERATURE = 0.7
    TOP_P = 0.9
    EMBEDDING_MODEL = "all-MiniLM-L6-v2"

class VectorDBConfig:
    CHUNK_SIZE = 512
    CHUNK_OVERLAP = 50

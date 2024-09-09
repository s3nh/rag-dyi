from typing import List, Dict, Union
from typing import Any, TypeVar

class ChromaStorage:
    n_results: int = 3
    path: str = 'chroma-base'

class RagCFG:
    model_name: str = 'mixedbread-ai/mxbai-embed-large-v1'
    llm_path: str = 'models/Llama-3-8B-Ultra-Instruct.Q4_K_M.gguf'
    chat_template: str = """
        <|start_header_id|>system<|end_header_id|>

        {System}<|eot_id|>
        <|start_header_id|>user<|end_header_id|>

        {User}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

        {Assistant}
        """ 

class RetrCFG:
    model_name: str = 'mixedbread-ai/mxbai-embed-large-v1'
    model_path: str = '../assets/retriever'
    padding: bool = True
    truncation: bool = True
    return_tensors: str = 'pt'
    pad_token: str = 'PAD ' 
    model_half: bool = True






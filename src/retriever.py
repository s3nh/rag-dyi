import os 
import sys
import torch
import torch.nn.functional as F

from cfg import RetrCFG
from typing import List, Dict, Union
from typing import Any, TypeVar

from transformers import AutoModel, AutoTokenizer # ;D 

class Retriever:

    def __init__(self):
        self.config = RetrCFG
        # its stupid af
        self._input_text: str = None
        self.device = torch.device('mps')
        self.retriever = self.load_retriever()
        self.tokenizer = self.load_tokenizer()
    
    @property
    def input_text(self):
        return self._input_text
    
    @input_text.setter
    def input_text(self, value):
        self._input_text = value

    @input_text.getter
    def input_text(self):
        return self._input_text

    @input_text.deleter
    def input_text(self):
        self._input_text = None

    def load_retriever(self):
        retriever = AutoModel.from_pretrained(
            pretrained_model_name_or_path = RetrCFG.model_name, 
        )
        if RetrCFG.model_half and self.device == 'cpu':
            torch.set_default_dtype(torch.half)
            return retriever.to(self.device).half().eval()
        else:
            return retriever.to(self.device).eval()

    def load_tokenizer(self):
        return AutoTokenizer.from_pretrained(
            pretrained_model_name_or_path = RetrCFG.model_name
        )

    def process_data(data: Union[str, List]) -> torch.Tensor:
        """
        Infer through retriever and lfg 
        """
        _batch = self.tokenizer(data, max_length = self.config.max_length, 
                                padding = self.config.padding, 
                                truncation = self.config.truncation, 
                                return_tensors = self.config.return_tensors).to(self.device)
        
        # Tokenized moving to retr
        with torch.no_grad():
            outputs = self.retriever(**_batch)
            # Assumingthat those are proper embedds
            embedds = outputs[:, 0] 
            return embedds


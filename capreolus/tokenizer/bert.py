from transformers import AutoTokenizer

from capreolus import ConfigOption

from . import Tokenizer


@Tokenizer.register
class BertTokenizer(Tokenizer):
    module_name = "berttokenizer"
    config_spec = [ConfigOption("pretrained", "bert-base-uncased", "pretrained model to load vocab from")]

    def build(self):
        self.bert_tokenizer = AutoTokenizer.from_pretrained(self.config["pretrained"], use_fast=True)
        # see supported tokenizers here: https://huggingface.co/transformers/model_doc/auto.html#transformers.AutoTokenizer

    def convert_tokens_to_ids(self, tokens):
        return self.bert_tokenizer.convert_tokens_to_ids(tokens)

    def tokenize(self, sentences):
        if not sentences or len(sentences) == 0:  # either "" or []
            return []

        if isinstance(sentences, str):
            return self.bert_tokenizer.tokenize(sentences)

        return [self.bert_tokenizer.tokenize(s) for s in sentences]

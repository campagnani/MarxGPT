#!./marxgpt-env/bin/python

import os
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments

# Função para treinar o modelo
def train_model():
    # Carregar tokenizador e modelo
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    # Pasta onde serão salvos os modelos treinados
    output_dir = "./modelo-treinado"
    os.makedirs(output_dir, exist_ok=True)

    # Carregar dados dos livros
    train_dataset = TextDataset(
        tokenizer=tokenizer,
        file_path="./txtgen/all.txt",
        block_size=128
    )

    # Configurar treinamento
    training_args = TrainingArguments(
        output_dir=output_dir,
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=8,
        save_steps=10_000,
        save_total_limit=2
    )

    # Criar trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False),
        train_dataset=train_dataset
    )

    # Treinar o modelo
    trainer.train()


# Função principal
def main():
    train_model()

if __name__ == "__main__":
    main()

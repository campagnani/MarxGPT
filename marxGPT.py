#!./marxgpt-env/bin/python

from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Carregar tokenizador e modelo treinado
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("modelo-treinado")

# Função para gerar resposta
def generate_response(input_text, model, tokenizer):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, early_stopping=True)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response


# Loop de interação com o usuário
while True:
    user_input = input("Você: ")
    if user_input.lower() == 'sair':
        print("Até logo!")
        break
    response = generate_response(user_input, model, tokenizer)
    print("Bot:", response)

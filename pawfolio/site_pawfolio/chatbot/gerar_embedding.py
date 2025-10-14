# Este arquivo é criado porque precisamos gerar embeddings (representação numérica das palavras)
# Usar os embedding para um chatbot simples como esse é recomendável pois as pessoas podem fazer as mesmas perguntas
# com conjunto de letras e palavras diferentes, porém, a ordem dos fatores não altera o resultado.
# Dito isso, usando o modelo "intfloat/multilingual-e5-small" para ler os embeddings, ele procura a pergunta FAQ
# mais parecida com a feita pelo usuário, para gerar uma unica resposta pré-programada no JSON. 


from sentence_transformers import SentenceTransformer
import json

with open('base_faq_raw.json', 'r', encoding='utf-8') as f:
    faq = json.load(f)

modelo = SentenceTransformer('intfloat/multilingual-e5-small')

# Extrai apenas as perguntas para gerar embeddings
perguntas = [item['pergunta'] for item in faq]

# Gera os embeddings
vetores = modelo.encode(perguntas).tolist()

# Junta pergunta, resposta e embedding
faq_completo = []
for i, item in enumerate(faq):
    faq_completo.append({
        "pergunta": item['pergunta'],
        "resposta": item['resposta'],
        "embedding": vetores[i]
    })

# Salva tudo no base_faq.json final
with open('base_faq.json', 'w', encoding='utf-8') as f:
    json.dump(faq_completo, f, ensure_ascii=False, indent=2)

print("base_faq.json gerado com sucesso!")


# Transcrição de Áudio, Resumo e Geração de Áudio a partir de Texto
## Este projeto realiza três etapas principais:

Transcrição de Áudio: Usa o modelo Whisper para converter o áudio em texto.
Geração de Pontos-chave: Utiliza o modelo Ollama para resumir o conteúdo transcrito.
Geração de Áudio: Converte o resumo gerado de volta para um arquivo de áudio utilizando o Bark.
Funcionalidades
Transcrição de áudio para texto: Converte arquivos de áudio (como MP3) em texto utilizando o modelo Whisper da OpenAI.
Resumir o conteúdo transcrito: Utiliza o Ollama para gerar um resumo dos pontos-chave do texto transcrito.
Conversão de texto em áudio: Gera áudio a partir do texto resumido usando o modelo Bark.
Tecnologias Utilizadas
OpenAI Whisper para transcrição de áudio.
LangChain Ollama para gerar resumos.
Bark para gerar áudio a partir de texto.
Pré-requisitos
Antes de rodar o script, você precisa instalar as dependências necessárias.

## Instalar as Dependências
> [!IMPORTANT]
Instale as seguintes bibliotecas necessárias:
```bash bash
pip install -U openai-whisper
pip install langchain-ollama
pip install git+https://github.com/suno-ai/bark.git
pip install ipython
```
> [!CAUTION]
> Talvez seja necessario atualizar ^também o ffmpeg
## Como Usar?
Este projeto está dividido em três etapas, como descrito abaixo:

### Etapa 1: Transcrição de Áudio para Texto
Primeiro, você deve transcrever o áudio para texto usando o modelo Whisper. Para isso, execute o seguinte código:

```python python

import whisper

# Carrega o modelo
model = whisper.load_model("small")

# Transcreve o áudio
result = model.transcribe("/caminho/para/seu/audio.mp3")

# Exibe o texto extraído
print(f"\n\nTexto Extraido do audio: {result['text']}")
```
>[!NOTE]
> Substitua "/caminho/para/seu/audio.mp3" pelo caminho real do seu arquivo de áudio.

### Etapa 2: Geração de Resumo com Ollama
Depois de transcrever o áudio para texto, você pode usar o Ollama para gerar um resumo do texto. O código para isso é o seguinte:

```python python
from langchain_ollama.llms import OllamaLLM

# Carrega o modelo Ollama
model = OllamaLLM(model="llama3.2:latest")

# Resumo do texto transcrito
resposta = model.invoke("Faça um resumo o mais resumidamente possível com os principais pontos-chaves do seguinte texto:  "+result['text'])

# Exibe o resumo gerado
print(f"\n\nResumo do Ollama: {resposta}")
```

### Etapa 3: Geração de Áudio a partir do Resumo
Agora, você pode gerar um arquivo de áudio com o resumo utilizando o modelo Bark. O código para gerar o áudio é o seguinte:

```python python
from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio

# Carrega os modelos do Bark
preload_models()

# Gera áudio a partir do texto do resumo
text_prompt = f"[PORTUGUESE-BR] {resposta}"
audio_array = generate_audio(text_prompt)

# Reproduz o áudio gerado
Audio(audio_array, rate=SAMPLE_RATE)
```
Esse código converterá o resumo do áudio de volta para áudio, permitindo que você ouça o conteúdo resumido.

> Referncia de Audio: https://youtu.be/S3RrknnJvGY?feature=shared



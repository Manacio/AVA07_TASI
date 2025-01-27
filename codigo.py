
# O CODICO ESTÁ DIVIDIDO EM DUAS ESTAPAS
# PRIMEIRA ETAPA: FAZER A INSTALAÇÃO DO WHISPER E EM SEGUIDA CONVERTER O AUDIO PARA O FORMATO DE TEXTO
# Para instalação do Whisper digite o seguinte comando no terminal: pip install -U openai-whisper
import whisper
model = whisper.load_model("small")
result = model.transcribe("/Users/Manacio/Documents/Ava07TASI/AVA07_TASI/alarmeMagnata.mp3") # endeço onde se localiza o audio que sera trancrito
print(f"\n\nTexto Extraido do audio: {result['text']}")

# SEGUNDA ETAPA: USAR O OLLAMA PARA FAZER UM RESUMO DA TRANCRIÇÃO DO AUDIO
# o ollama sera utilizado para fazer um resumo do audio trancrito
from langchain_ollama.llms import OllamaLLM
model = OllamaLLM(model="llama3.2:latest") # Modelo que sera usado

resposta = model.invoke("Faça um resumo o mais resumidamente possivel com os principais pontos-chaves do seguinte texto:  "+result['text']) # o texto extraido pelo o whisper sera resumido pelo Ollama
print(f"\n\nResumo do Ollama: {resposta}")

# TERCEIRA ETAPA: TORNARÁ O RESUMO DO ALLAMA EM ARQUIVO DE AUDIO
#!pip install git+https://github.com/suno-ai/bark.git
from bark import SAMPLE_RATE, generate_audio, preload_models
#  pip install ipython
from IPython.display import Audio

preload_models()

text_prompt = f"""
      [PORTUGUESE-BR] {resposta}
 """
audio_array = generate_audio(text_prompt)
Audio(audio_array, rate=SAMPLE_RATE)
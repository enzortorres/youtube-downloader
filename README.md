# 📥 YouTube Downloader CLI (Python + yt-dlp)

Um script em Python para baixar vídeos ou áudios do YouTube automaticamente, salvando na pasta padrão de vídeos do sistema operacional.

O projeto detecta o sistema (Windows, Mac ou Linux), cria uma pasta dedicada e permite escolher entre:

🎬 Download de vídeo na melhor qualidade disponível
🎧 Download de áudio em português (se disponível) convertido para MP3

## 🚀 Funcionalidades

- Detecção automática do sistema operacional
- Criação automática da pasta youtube_downloads
- Download de vídeo em melhor qualidade
- Download de áudio com preferência para PT-BR
- Conversão automática para MP3 (via FFmpeg)

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- yt-dlp
- FFmpeg
- pathlib
- os
- platform

## 📦 Instalação

### 1️⃣ Clone o repositório

```bash
    git clone https://github.com/enzortorres/youtube-downloader.git
    cd youtube-downloader
```

### 2️⃣ Crie um Ambiente Virtual (recomendado)

🔹 Windows
```bash
    python -m venv venv
    venv\Scripts\activate
```

🔹 MacOS / Linux
```bash
    python3 -m venv venv
    source venv/bin/activate
```

Se ativou corretamente, você verá algo assim no terminal:

```(venv)```

### 3️⃣ Instale as dependências

```bash
    pip install -r requirements.txt
```

### 4️⃣ Instale o FFmpeg (obrigatório para converter para MP3)

Windows (recomendado)

```bash
    winget install ffmpeg
```

Teste:

```bash
    ffmpeg -version
```

Se aparecer a versão, está tudo certo ✅, caso não ❌, reinicie seu terminal/IDE.

## ▶️ Como Usar

### Execute:

```bash
    python main.py
```

O programa solicitará:

```
    Digite a URL do vídeo que deseja baixar:
```

Depois:

```
    1 - Vídeo
    2 - Áudio (PT-BR se disponível)
```

Escolha a opção desejada e o download será iniciado automaticamente.

### 📂 Estrutura do Projeto
```
    youtube-downloader/
    │
    ├── main.py
    ├── requirements.txt
    ├── README.md
    └── venv/
```
🎧 Download de Áudio

### O script:

- Prioriza áudio em português (pt)
- Extrai somente o áudio
- Converte automaticamente para MP3
- Utiliza a melhor qualidade disponível
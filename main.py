import os
import platform
from pathlib import Path

sistema = platform.system()

# > Seleciona a pasta (Vídeos) de acordo com o sistema operacional
if sistema == 'Windows':  # ? Windows
    pasta_videos = Path.home() / "Videos"
elif sistema == 'Darwin':  # ? Mac-OS
    pasta_videos = Path.home() / "Movies"
else:  # ? Linux e outros
    pasta_videos = Path.home() / "Videos"

pasta_destino = pasta_videos / "youtube_downloads"
pasta_destino.mkdir(parents=True, exist_ok=True)

url = input("Digite a URL do vídeo que deseja baixar: ").strip()

try:
    opcao = int(input("O que deseja baixar?\n1 - Vídeo\n2 - Áudio (PT-BR se disponível)\n>>> "))

    if opcao == 1:
        print("\nBaixando vídeo em melhor qualidade disponível...")
        comando = f'yt-dlp -f "bestvideo+bestaudio/best" -o "{pasta_destino}/%(title)s.%(ext)s" "{url}"'
        os.system(comando)
        print("\033[32mDownload de vídeo completo!\033[m")

    elif opcao == 2:
        print("\nBaixando áudio em português (se disponível)...")
        comando = f'yt-dlp -f "bestaudio[language=pt]/bestaudio" -o "{pasta_destino}/%(title)s.%(ext)s" "{url}"'
        os.system(comando)
        print("\033[32mDownload de áudio completo!\033[m")

    else:
        print("Opção inválida.")

except Exception as error:
    print("Download falhou")
    print(f"\033[1;31m{error.__class__.__name__}: {error}\033[0m")

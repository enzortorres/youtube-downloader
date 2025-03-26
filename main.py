from pytubefix import YouTube
from pathlib import Path
import os
import platform

sistema = platform.system()
# > Seleciona a pasta (Vídeos) de acordo com o sistema operacional
if sistema == 'Windows': # ? Windows
    pasta_videos = Path.home() / "Videos"
elif sistema == 'Darwin': # ? Mac-OS
    pasta_videos = Path.home() / "Movies"
else: # ? Linux e outros
    pasta_videos = Path.home() / "Videos"

pasta_destino = pasta_videos / "youtube_downloads"
pasta_destino.mkdir(parents=True, exist_ok=True)

url = input("Digite a URL do vídeo que deseja baixar: ").strip()

try:
    opcao = int(input("O que deseja baixar?\n1 - Vídeo\n2 - Áudio\n>>> "))
    yt = YouTube(url)

    print(f"Baixando: {yt.title}")

    if opcao == 1:
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=pasta_destino)
        print("Download de vídeo completo!")

    elif opcao == 2:
        stream = yt.streams.filter(only_audio=True).first()
        arquivo_temp = stream.download(output_path=pasta_destino)

        print("Download de áudio completo!")
    else:
        print("Opção inválida.")

except Exception as error:
    print("Download falhou")
    print(f"\033[1;31m{error.__class__.__name__}: {error}\033[0m")

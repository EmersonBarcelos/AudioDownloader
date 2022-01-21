# Audio Downloader
Faça downloads de áudios diretamente do youtube, por exemplo para download de podcasts no youtube,
com uma interface simples e fácil de usar.

Programa feito com interface GTK

Bibliotecas utilizadas:

<pre>
 <span style="font-weight: 400">youtube_dl -> pip install youtube_dl</span>
 <span style="font-weight: 400">gi -> ja vem por padrão em distros linux</span>
</pre>
É necessario a instalação do pacote ffmpeg para o funcionamento correto!

Para adicionar este PPA execute:

<pre>
 <span style="font-weight: 400">sudo apt-get install -y software-properties-common</span>
 <span style="font-weight: 400">add apt-repository ppa:mc3man/trusty-media</span>
</pre>

Depois que o PPA estiver instalado, vamos atualizar o repositório executando o comando:

<pre>
 <span style="font-weight: 400">apt-get update</span>
 <span style="font-weight: 400">apt-get dist-upgrade</span>
</pre>

Por último, vamos instalar o FFmpeg:

<pre>
 <span style="font-weight: 400">apt-get install ffmpeg</span>
</pre>

<img src=https://github.com/EmersonBarcelos/AudioDownloader/blob/main/LayoutPrograma.png/>

 



# atom_back

Это локальный бекенд, имеется задеплоенный бекенд по адресу https://pythonatomicbackend.ru (Ubunta 20.04, Nginx, Python, Flask)

Для запуска локального бекенда необходимо:
1. Сделать клон - https://github.com/sazonov-dev/atom_back.git
2. Перейти в папку и установить зависимости: 
    pip install Flask
    pip install Flask-CORS
    pip install -U openai-whisper / pip install git+https://github.com/openai/whisper.git / pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
    
    # on Ubuntu or Debian
    sudo apt update && sudo apt install ffmpeg
    
    # on Arch Linux
    sudo pacman -S ffmpeg
    
    # on MacOS using Homebrew (https://brew.sh/)
    brew install ffmpeg
    
    # on Windows using Chocolatey (https://chocolatey.org/)
    choco install ffmpeg
    
    # on Windows using Scoop (https://scoop.sh/)
    scoop install ffmpeg
3. Запустить сервер, python3 main.py / python main.py

Ссылка на фронт - https://github.com/sazonov-dev/atomic

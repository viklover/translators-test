
if [ ! -d "resources/libretranslate" ] 
then
    git clone https://github.com/LibreTranslate/LibreTranslate resources/libretranslate
fi

cd resources/libretranslate
python main.py

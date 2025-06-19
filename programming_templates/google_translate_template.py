import asyncio
from googletrans import Translator

async def translate_text():
    translator = Translator(service_urls=['translate.googleapis.com'])
    result = await translator.translate('Your Text Here', dest='es') # Change language by Python Lang Code.
    print(result.text)

if __name__ == "__main__":
    asyncio.run(translate_text())
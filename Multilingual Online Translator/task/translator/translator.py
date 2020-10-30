import sys
import requests
from bs4 import BeautifulSoup

langs = ['arabic', 'german', 'english', 'spanish', 'french', 'hebrew', 'japanese',
         'dutch', 'polish', 'portuguese', 'romanian', 'russian', 'turkish']


def check_lang(lang):
    if lang in langs:
        return lang
    else:
        print(f"Sorry, the program doesn't support {lang}")
        exit()
        return None


lang_from = check_lang(sys.argv[1])
if sys.argv[2] == 'all':
    langs.remove(lang_from)
    langs_to = [lang for lang in langs]
else:
    langs_to = [check_lang(sys.argv[2])]
word = sys.argv[3]

with open(f'{word}.txt', mode='w', encoding='utf-8') as f:

    session = requests.Session()
    for lang_to in langs_to:
        url = f"https://context.reverso.net/translation/{lang_from}-{lang_to}/{word}"
        try:
            request = session.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        except Exception:
            print('Something wrong with your internet connection')
        else:
            soup = BeautifulSoup(request.text, 'html.parser')
            try:
                examples = soup.select_one('#examples-content').select('.example')
            except AttributeError:
                print(f"Sorry, unable to find {word}")
            else:
                try:
                    translations = soup.select_one('#translations-content').select('a')
                except AttributeError:
                    print(f"Sorry, unable to find {word}")
                else:
                    result = '\n'.join([lang_to + ' Translations:',
                                        str.strip(translations[0].text) + '\n',
                                        lang_to + ' Examples:',
                                        str.strip(examples[0].select('.text')[0].text) + ':',
                                        str.strip(examples[0].select('.text')[1].text) + '\n\n'])

                    print(result, file=f, sep='\n', flush=True)
                    print(result)


Extrakce dat pro kontejner gql_lessons (Doskočil, Vysloužil)

Selenium - pip install selenium

1. Otevřeme předem definovaný prohlížeč a pomocí openPage se dostaneme na požadovanou url adresu
2. Na url adrese se přihlásime přes def login, kde jako přihlašovací údaje funkce přečte soubor login.txt
3. Pomocí XPATH selektujeme jaký rozvrh chceme scrapenout, stáhneme rovnou díky možnosti exportovat csv soubor na stejné stránce
4. Def csv_to_json je způsob, kterým csv soubor převedeme do json souboru a s ním můžeme dále pracovat

možnost úpravy do budoucna:
- vylepšit ukládání csv na relativní cestu
- nahradit time sleep
# Tehtävä 2: Git Commit Amend / Commitin muokkaaminen, repositorion kloonaaminen

**Amend**-optio mahdollistaa viimeisimmän commitin muokkaamisen. Tämä voi tulla tarpeeseen mikäli tekemämme commitin viesti ei ollut tarpeeksi kuvaava tai jokin tiedosto puuttui commitista. `$ git commit amend` komento lisää **staging area**lla olevat tiedostot viimeisimpään commitiin, **älä kuitenkaan vielä aja sitä**.

Lisää **index.html** tiedostoon alla olevan esimerkin mukaisesti kappale `<p>Git-oppiminen on kivaa!</p>` ja aja `$ git add index.html`. Tee muutoksista commit.

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Learning Git</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>Learning Git</h1>
    <p>Git-oppiminen on kivaa!</p>
  </body>
</html>
```

Lisää samaan index.html -tiedostoon myös toinen kappale, `<p>Todella kivaa!</p>`. Tee samaan tapaan muutoksista commit.

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Learning Git</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>Learning Git</h1>
    <p>Git-oppiminen on kivaa!</p>
    <p>Todella kivaa!</p>
  </body>
</html>
```

Oletetaan, että unohdimme lisätä viimeisimmästä commitista tärkeitä tietoja projektista sisältävän **readme.txt** -tiedoston viimeisimpään commitiin. Tämän tiedoston sisältö voi olla mitä vaan.

Luo readme.txt -tiedosto **työskentelyhakemistoosi** ja lisää se **staging arealle**. Tämän jälkeen tarkista `git status` sekä `git log`.

Korvaa aikaisempi commit (joka ei sisältänyt readme.txt -tiedostoa) käyttämällä `git commit --amend` -komentoa ja syötä tekstieditoriin viesti, jossa on maininta **readme.txt** -tiedoston lisäämisestä. Tekemäsi commit sisältää kaikki aiemman commitin muutokset sekä juuri luodun readme.txt -tiedoston.

Aja `git status`, `git log` sekä `ls -la`.

`git log` -komennon näyttämien lokitietojen pitäisi nyt sisältää maininta lisätystä readme.txt -tiedostosta kolmannessa (vai toisessa????) commitissa. `git status`-komennon pitäisi todeta, ettei repositoriossa ole mitään commitattavaa, sillä readme.txt lisättiin viimeisimmässä commitissa.

Tulevaisuudessa voi olla tarvetta muillekin commiteihin liittyviin komentoihin (esimerkiksi peruuttaminen), mutta ne eivät ole osa commit-komentoa.

## Paikallisen repositorion varmuuskopiointi toiseen kansioon

Ennen kuin alamme seikkailemaan repositorion eri versioiden välillä, nyt on erinomainen aika tehdä paikallisesta repositoriosta klooni (eli varmuuskopio). Komento `git clone` kloonaa repositorion haluamaasi kansioon (toimii myös verkossa olevien repositorioiden kanssa, tämä tulee tutuksi myöhemmin). **Huomio**: älä varmuuskopioi repositoriota samaan kansioon alkuperäisen kanssa. Esimerkiksi, jos repositorio sijaitsee kansiossa /kurssit/ohkeh/ohkeh-2-\<*käyttäjänimesi*> voit kloonata sen vaikka kansioon /kurssit/ohkeh/ohkeh2-\<*käyttäjänimesi*>-backup.

```
$ git clone path/to/source/folder path/to/destination/folder # Kopioi paikallisen repositorion uuteen kansioon
```

Tehdään pari toimenpidettä kloonatussa repositoriossa. Siirry kloonattuun repositorioon `cd` -komennolla ja aja siellä:

```
$ git remote -v
```

Terminaali/Git bash palauttaa sinulle tiedon etärepositorion **fetch**- ja **push** osoitteista. Seuraavaksi poistetaan nämä tiedot repositoriosta ajamalla `git remote rm`. **Varmista ennen tätä, että olet kloonatussa repositoriossa!**

```
$ git remote rm
```

Lopuksi tarkista `git remote -v` -komennolla, että ovatko kyseiset tiedot hävinneet. Jos komento ei palauta mitään, fetch- ja pull-osoitteet on poistettu onnistuneesti. Ota kuvankaappaus kolmesta viimeisestä komennosta ja niiden palautteista, joista selviää alkuperäiset remote-osoitteet ja se, että ne on poistettu. Tallenna kuva **alkuperäisen repositorion** img-kansioon nimellä **gitRemoteRemoval.PNG**, committaa muutokset ja pushaa ne Githubissa sijaitsevaan etärepositorioon.

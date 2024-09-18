# Kühn András Gábor
### Gépi tanulás-orientált önéletrajz

###### _A többit megtekintheti GitHub-on:_
###### _[http://github.com/kuhnandrasgabor/cv ](http://github.com/kuhnandrasgabor/cv)_

# Personal info

 * **Location:** [Szeged, Hungary](https://maps.app.goo.gl/HrTJQS68Pcr1mWZY9)

 * **Email:** [kuhnandrasgabor@gmail.com](mailto:kuhnandrasgabor@gmail.com)

 * **Social:** [LinkedIn](https://www.linkedin.com/in/andrew-k%C3%BChn-58251070/)

 * **Visuals:** [Gallery](https://drive.google.com/drive/u/1/folders/17BtC\_NqO1VWdKJ8OTOcvbAuNRcr1uOjr)

<img src="../images/profile.jpg" alt="profile_picture" width="200">


# Szakmai tapasztalatok

Több mint 10 évnyi tapasztalattal rendelkező szakember vagyok különböző területeken, a gépi tanulástól és a webfejlesztésen át a 3D vizualizációig a profi fotózásig, vezetői tapasztalattal és széles körű technikai készségekkel.

Tapasztalatom van vezetői szerepekben kisebb csapatokban, beleértve a technológiai startupokat is, ahol egyik helyen egy bonyolult online játékfejlesztési projektet vezettem, majd egy másik startup technológiai vezetőjeként AI-alapú adatkezelési és SaaS megoldásokat építettem repülő- és nehézipari ügyfelek számára.

Van némi tapasztalatom üzleti tárgyalásokban és projektmenedzsmentben, de a legjobb a kreatív tervezésben és problémamegoldásban vagyok, ahol a széles körű technikai háttéremet tudom a legjobban kihasználni, amelyet a munkám és a hobbijaim során szereztem. Nagyon hiszek a pareto-elvben, és igyekszem különböző területeken szerzett tudással felszerelni magam, miközben szakértőkre támaszkodom azokban a kérdésekben, amelyekben nem mozgok kellőképpen otthonosan.

Az angoltudásomnak köszönhetően kiválóan teljesítek multikulturális környezetekben.

Elhivatott vagyok a folyamatos tanulásban és fejlődésben, figyelek a részletekre, és szenvedélyesen érdeklődöm a technológia és az innováció iránt. Igyekszem a technológiát arra használni, hogy javítsam személyes és szakmai életem minden területét, például AI eszközök használatával, amikor az indokolt vagy megfelelő.


## 2020 – Jelen: Adattudomány, Gépi Tanulás, Full-Stack Fejlesztő & Technikai vezető Pzartech Ltd.


Eredetileg szabadúszó fejlesztőként kezdtem, végül a cég CTO-jaként találtam magam, ahol minden fejlesztési és architekturális döntésért én voltam a felelős.
Fel lettem kérve egy **adatkezelő szoftver** prototípusának **újrafejlesztésére** és az **SaaS megoldásként** való bevezetésére, amelyet a repülőgép ipari MRO-k és a nehézipar számára terveztek.

A cég stratégiai tervezésében, technikai döntéshozatalában és jövőbeli növekedésében is kollaboráltam, aminek köszönhetően részesedést ajánlottak a cégben a hozzájárulásomért.

Néhány nagyobb mérföldkő közé tartozik egy **SAP S4/HANA** integrációs prototípus, **ElasticSearch** analitikai prototípus, **Azure tároló** kezelés médiaszolgáltatásokkal, **videó streaming** prototípus, és a projekt legnagyobb értékét képviselő **vizuális keresés és OCR** megoldások fejlesztése és beüzemelése.

* Full-stack webfejlesztés .Net Core, Blazor, Razor, MongoDB, MAUI 
* ML/AI fejlesztés Pythonnal
* Képosztályozó és OCR rendszer tanítás és telepítése
* CI/CD Azure DevOps, Azure Portal-al
* Git verziókövetés az Azure DevOps-on keresztül

### Web alapú adatmanagement szoftver

Én voltam a felelős egy webes adatkezelő rendszer fejlesztéséért, amelyet MRO és ipari ügyfelek számára terveztek, Ai keresőeszközökkel tűzdelve.


#### Használt és elsajátított képességek
 * C#, Python, HTML
 * .Net Core, Blazor, Razor, MongoDB, MAUI
 * Azure DevOps, Azure Portal, CI/CD
 * Git verziókövetés az Azure DevOps-on keresztül

### Gépi Tanulás és Adattudomány

A feladatom az volt hogy fejlesszek és javítsak egy **képosztályozó hálózatot** az **ipari alkatrészek felismerésére**. Az eredeti ötletet túl nehéznek bizonyult optimalizálni hosszú távon, így egy konzultáns szakértő segítségével elkezdtem egy új hálózatot nulláról tanítani, ami a gépi tanulás világába vezetett be.

A feladatot nehezítette, hogy az **adatminőség szeszélyes volt**, **nem volt** reális **esély a videofelvételek újra rögzítésére**, és több hibás címkézés is volt mind a tanító, mind a tesztelő adatokban, így sok erőfeszítést kellett tennem az egyes tanítási futások teljesítményének vizualizálásába, hogy kiderítsem mik voltak a problémák.

Ezen hibák felfedezése arra kényszerített, hogy különböző módszereket dolgozzak ki azok észlelésére és javítására, végül egy **adatbeviteli és feldolgozási eszközsort** hoztam létre pythonban, több minőségbiztosítási lépéssel, mint például egyedi neurális hálózatokat, amelyeket arra képeztem ki, hogy észleljék a problémákat és jelöljék meg a fájlokat mielőtt továbbadnák őket a későbbi feldolgozási lépéseknek.

Az eredmény egy olyan modell volt, amely bizonyította képességét valós körülmények között, és jóval meghaladta az elvárásokat: 84% pontosság egyetlen kép használatakor top-4 szituációban, de **érzésre 100% pontosság** amikor a rendszeren aktiváltuk a többképes előrejelzést.

Egy másik feladatom az **OCR szoftver** prototípusának elkészítése volt, ahol a cél az volt, hogy a gépelt számoktól a kézzel gravírozott pontmátrixos sorozatszámokig mindenféle feliratot felismerjünk.

Ugyan ez a projekt nem jutott túl a prototípus fázison, az általam kitalált megoldás (a pre-processzálás, hiperparaméterek és a lehetséges finomhangolási módszerrel együtt) azt eredményezte, hogy a mi verziónk nagyrészt tartotta a lépést, és néhány speciálisabb és nehezebb esetben még túlszárnyalta is az iparági szabványos megoldásokat, mint például az Azure AI Vision. A finomhangolási megoldás prototípusa is elkészült: egy **szintetikus adatgeneráló szkript** Blenderhez, ami ezáltal utat nyitott a modell finomhangolásához speciális szituációkra.


* ML adatszett generálás
  * Nyers videó feldolgozás, szegmentálás, javítás, kiértékelés fél-szintetikus adatokhoz
  * Realisztikus címkézett szintetikus képek generálása
  * Adatmanagement és ehhez eszközök létrehozása
* ML tanítás
  * Képminőség-értékelő hálózat a tanítóadatok kiértékeléséhez
  * bounding-box hálózat a tanítóadatok kiértékeléséhez
  * képosztályozó hálózat ipari alkatrészfelismeréshez
  * optikai karakterfelismerő rendszer
* Létező SaaS architektúrába való integrálás az Azure felhőjében
* Teljesítménydiagramok és elemzés


<!-- PAGEBREAK -->

#### Használt és elsajátított képességek
* C# az API-hoz, de főleg Python a tanításhoz és a predikcióhoz
* FastAi, PyTorch, TensorFlow, Jupyter notebookok és Paperspace Gradient
* Flask, seaborn, matplotlib, pandas, numpy
* Docker, Docker-Compose

## 2011 – Jelen: Szabadúszó (Fotó, 3D Grafika, Webdesign, Építészeti Vizualizáció)


Dolgoztam egy többnyelvű checklist app-on iOS-re, egy PHP Magento alapú online áruházon, valós idejű interaktív 3D építészeti vizualizációs projekteken, 3D modellezésen és animáción, brandingen, reklámon, logó és web designon és szabadúszó fotósként.


#### *3D modellezés és vizuális effektek*


Lehetőségem volt dolgozni néhány 3D vizualizáción interaktív képzési anyaghoz természeti katasztrófákkal kapcsolatban.

### [Galéria](../sections/experience/freelance/3d/freelance-3d-gallery_hu.md)

#### Interaktív Építészeti Vizualizáció

Valós-idejű bejárható szimuláció Unreal Engine 4 használatával, interaktív elemekkel.

### [Galéria](../sections/experience/freelance/archviz-interactive/freelance-archviz-interactive-gallery_hu.md)

#### Realisztikus Építészeti Vizualizáció

Gyors és durva, de mégis realisztikusnak ható renderképek két kertről, kétnapos határidővel.

### [Galéria](../sections/experience/freelance/archviz-realistic/freelance-archviz-realistic-gallery_hu.md)

## 2014\. – 2020\. Stoneglass Labs KFT., Szeged (CEO)


Vezettem egy szoftverfejlesztő csapatot egy kis cégben, amely egy ambiciózus online játékot fejlesztett.



### *Stars End (MMORPG Játékszoftver projekt)*



Egy valós-idejű Sci-Fi többjátékos online szerepjátékot fejlesztettünk.


### [Galéria](../sections/experience/starsend/starsend-gallery_hu.md)

# Tanulmányok
* **Üzleti Tréning** *(2013 – 2014\)*
  Alapvető üzleti folyamatok és menedzsment képzés a Támop 2.3.6 pályázat keretében.
* **Tripont Light Academy 1-2-3** *(2011 – 2013\)* 
    Képzés fényképezési technikákban, különbözö fotózási diszciplínákban és projektmenedzsmentben.
* **SZTE JGYPK, Webprogramozó** *(2010 – 2011, Befejezetlen)*
    Alapvető készségek elsajátítása webfejlesztésben, beleértve az HTML, Java, SQL és grafikai tervezés alapjait. Elvesztettem az érdeklődést és átváltottam a fotózásra és az üzleti vállalkozásra.
* **SZTE TTIK, Mérnök-informatikus BSc.** *(2008 – 2010, Befejezetlen)*
  Részt vettem programozás (C, Assembly), számítógép-architektúra, diszkrét matematika és algoritmusok kurzusokon. Fókszváltás miatt nem fejeztem be a diplomát.

<!-- PAGEBREAK -->

# Késségek és kompetenciák

## Technikai ismeretek

### Programmozási nyelvek
  * **Tapasztalt:** C#, Python
  * **Jártas:** C++, HTML, CSS, SQL, PHP
  * **Ismer:** Java, JavaScript, TypeScript, C, Google Script, assembly

### Keretrendszerek és technológiák
  * **Web Development Frameworks:**
    * **Tapasztalt:** .NET Core, Blazor, Razor, MAUI, MudBlazor
    * **Jártas:** Angular
    * **Ismer:** Flask

  * **Gépi tanulással kapcsolatos keretrendszerek:**
    * **Ismer:** FastAI, PyTorch, TensorFlow, Scikit, Jupyter Notebooks, Paperspace Gradient

  * **DevOps and Konténerizáció:**
    * **Tapasztalt:** Azure DevOps
    * **Jártas:** CI/CD pipeline
    * **Ismer:** Docker, Docker Compose

  * **Adatelemzés és Vizualizáció:**
    * **Ismer:** Pandas, NumPy, Matplotlib, Seaborn

### Adatbázisok és adatmanagement

* **Jártas:** MongoDB, SQL databases (pl.: MySQL, SQL Server)
* **Ismer:** ElasticSearch

### Felhő alapú szolgáltatások és infrastruktúra

* **Tapasztalt:** Azure DevOps, Portal, Storage, App services and VMs
* **Jártas:** Azure Resource Management, CI/CD pipeline implementation
* **Ismer:** Docker, Docker Compose, Azure Media Services

### Szoftverek és eszközök

* **Verziókövetés:**
  * **Tapasztalt:** Git (Azure DevOps, GitHub)
  * **Ismer:** SVN

* **3D Grafika és Modellezés:**
  * **Tapasztalt:** Blender 3D, Unreal Engine 4, Unity 3D
  * **Jártas:** Substance Painter, Substance Designer, SketchUp, V*Ray
  * **Ismer:** Houdini, SolidWorks CAD, ArchiCAD, CATIA, Fusion 360

* **Adobe Creative Suite:**
  * Tapasztalt vagyok a Photoshop és Lightroom használatában

### Kreatív design és játékfejlesztés

* 2D/3D tartalomkészítés, vektorgrafika, modellezés, textúrázás, világítás és renderelés
* Web és alkalmazások UI/UX tervezése
* Vizuális történetmesélés és játéktervezés
* VFX, shader és procedurális/parametrikus modellezés
* Tapasztalat játékfejlesztésben és motor testreszabásban Unity 3D és Unreal Engine 4 környezetben
* Animáció és fizikai szimuláció


## Szakmai készségek

* **Projektmenedzsment:**
  Tapasztalat projektmenedzsmentben a kezdetektől a befejezésig, beleértve a szoftverfejlesztést, marketingkampányokat és
  kreatív projekteket. Ismerem az Agile módszertant és az Azure DevOps-szal a CI/CD pipeline kezelését.
* **Üzleti és tárgyalási készségek:**
  Tapasztalat üzleti tárgyalásokban, ügyfélkezelésben és vállalati adminisztrációban. Képzett stratégiai üzleti tervek
  kidolgozásában és végrehajtásában.
* **Kreatív és tervezési készségek:**
  Erős háttér a kreatív tervezésben, beleértve a 2D/3D tartalmak létrehozását, UI/UX tervezést és vizuális történetmesélést játékokhoz
  és szimulációkhoz. Tapasztalat a VFX, shader és procedurális/parametrikus modellezés területén.


## Lágy készségek:
* **Vezetés:**
  Tapasztalat kisebb, vegyes feladatkörű csapatok vezetésében főként startup környezetben. Képes vagyok konfliktusokat kezelni és együttműködő munkahelyi környezetet kialakítani.
* **Kommunikáció:**
  Folyékony angol nyelvtudás (C2) és kezdő német nyelvtudás (A1). Képzett vagyok a világos és hatékony kommunikációban mind a technikai, mind a nem technikai érintettekkel.
* **Problémamegoldás és alkalmazkodóképesség:**
  Erős analitikai készségekkel rendelkezem, amelyekkel bonyolult problémákat tudok megoldani és új kihívásokhoz tudok alkalmazkodni.
  Hajlamos vagyok új technológiák és eszközök használatának önálló tanulására.


# Érdeklődési körök

## Alkotás
Az alkotás és dolgok megváltoztatása az életem alapvető részévé vált. Legyen szó szoftverről, 3D modellről, bútorról vagy fotóról, gyermekkorom óta élvezem az alkotás folyamatát és az elért eredmények látványát.

## Kreativitás és dizájn
Erős a szenvedélyem a kreativitás iránt, legyen szó legókról, VR-ról, szimulációról vagy dizájnról, ez a szenvedély táplálja az érdeklődésemet a szoftverfejlesztés és dizájn iránt.

## Mechanika és elektronika
Ami hobbi R/C modellekkel kezdődött, az az életem során kísért, mivel különféle elektronikai eszközöket építettem (és javítottam). Az ilyen kézzelfogható tapasztalat, amikor szétszedek valamit, megértem működését, és újra összerakom, segít megérteni a hardver-szoftver integrációt.

## Technológia és futurizmus
Mélyen érdekelnek az új technológiák és azok lehetséges hatásai a társadalomra, mint például az AI, a kvantumszámítógépek és a világűr felfedezése. Ez a jövőbe tekintő mindent körülölelő gondolkodásmód perspektívát ad a szoftverfejlesztés és a data science területein való tevékenységemhez.

## Természet, elemek, felfedezés
Amióta az eszemet tudom, mindig is szerettem a vizet, és búvárvizsgával rendelkezem. Felnőtt éveim nagy részében sziklamászó és természet rajongó voltam. Mostanában siklóernyőzni kezdtem, ami további elemet ad az érdeklődési körömhöz. Az életem során olyan tevékenységek felé vonzódok, amelyek felfedezési élményt és kapcsolatot kínálnak a természeti világgal, miközben személyes felelősséget és önállóságot igényelnek.



A feladatom az volt, hogy fejlesszek és javítsak egy **képosztályozó hálózatot** az **ipari alkatrészek felismerésére**. Az eredeti ötlet hosszú távú optimalizálása túl bonyolultnak bizonyult, így egy konzultáns szakértő segítségével elkezdtem egy új hálózatot nulláról tanítani, ami a gépi tanulás világába vezetett be.

A feladatot nehezítette, hogy az **adatminőség ingadozó volt**, **nem volt** reális **esély a videofelvételek újra rögzítésére**, és több hibás címkézés is volt mind a tanító, mind a tesztelő adatokban, így sok erőfeszítést kellett tennem az egyes tanítási futások teljesítményének vizualizálásába, hogy kiderítsem mik voltak a problémák.

Ezen hibák felfedezése arra késztetett, hogy különböző módszereket dolgozzak ki azok észlelésére és javítására, végül egy **adatbeviteli és feldolgozási eszközsort** hoztam létre pythonban, több minőségbiztosítási lépéssel, mint például egyedi neurális hálózatokat, amelyeket arra képeztem ki, hogy észleljék a problémákat és jelöljék meg a fájlokat mielőtt továbbadnák őket a későbbi feldolgozási lépéseknek.

Az eredmény egy olyan modell volt, amely bizonyította képességét valós körülmények között, és jóval meghaladta az elvárásokat: 84% pontosság egyetlen kép használatakor top-4 szituációban, de **érzésre 100% pontosság** amikor a rendszeren aktiváltuk a többképes előrejelzést.

Egy másik feladatom az **OCR szoftver** prototípusának elkészítése volt, ahol a cél az volt, hogy a gépelt számoktól a kézzel gravírozott pontmátrixos sorozatszámokig mindenféle feliratot felismerjünk.

Ugyan ez a projekt nem jutott túl a prototípus fázison, az általam kitalált megoldás (a pre-processzálás, hiperparaméterek és a lehetséges finomhangolási módszerrel együtt) azt eredményezte, hogy a mi verziónk nagyrészt tartotta a lépést, és néhány speciálisabb és nehezebb esetben még túlszárnyalta is az iparági szabványos megoldásokat, mint például az Azure AI Vision. A finomhangolási megoldás prototípusa is elkészült: egy **szintetikus adatgeneráló szkript** Blenderhez, ami ezáltal utat nyitott a modell finomhangolásához speciális szituációkra.

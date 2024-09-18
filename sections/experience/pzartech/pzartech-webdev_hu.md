### *Web alapú adatmanagement szoftver*

A projektet Azure DevOps-ban kezeltük, CI/CD pipeline implementációval, Azure-ban hostolva.
A **.Net Core**-t választottuk **Blazor Razor** oldalakkal, **MongoDB**-t adatbázisnak és **MAUI**-t Android és WebClient build targeteknek.
A projekt egy teljes újraírása volt az eredeti szoftvernek, a hangsúly a modularitáson és skálázhatóságon volt, ezért mikroszolgáltatás architektúrát használtunk frontend szerverrel, core szerverrel és különböző felismerő modul szerverekkel.

* SaaS szoftver struktúra és design konzultáció ERP szoftverhez
* Azure felhő erőforrások telepítése és kezelése
* Azure DevOps projektmenedzsment, CI/CD
* .Net Blazor Razor oldalakon alapuló projekt MAUI többplatformos célokkal
  * Azure bucket tároló integráció és kezelése
  * API kapcsolatok
    * frontend szerver
    * core szerver
    * különböző felismerő modul szerverek
  * Kép és karakterfelismerés fejlesztése és integrációja
  * Responsive UI MudBlazorral (bár nem vagyok igazán front-end fejlesztő)
  * ElasticSearch alapú oldal és használati analitika prototípus
  * Média tárolás és streaming prototípus Azure médiaszolgáltatásokkal
  * SAP integrációs prototípus SAP HANA S/4 Product Master Adatokhoz
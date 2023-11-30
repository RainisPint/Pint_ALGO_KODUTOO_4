# Ülesanne 1: Räsimine 
# 1. Kirjuta selglitus räsimise (hashing) kontseptsioonist - põhiidee ja eesmärk. 
Põhiidee: Räsimist kasutatakse kiirete andmeotsingute jaoks. Kindlale sisendile määratakse unikaalne räsiväärtus, mille järgi saab andmeid leida või lisada.

Eesmärk: Kiire juurdepääs andmetele vähendades otsinguaega suurte andmekogumite puhul.

# 2. Kirjelda hea räsifunktsiooni omadusi ja selgita, miks need on olulised. 
Vastupidavus kokkupõrgetele - säilitab andmestruktuuri terviku.
Väike kokkupõrgete arv - räsimisalgoritm on efektiivsem, kui kokkupõrkeid on vähem. Peab erinevate sisendite puhul genereerima erinevaid räsi väärtuseid.
Ühtlane jaotumine - vältimaks seda, kus mitu võtmeväärtust jagavad sama räsiväärtust.

# 3. Selgita kokkupõrgete lahendamise tehnikaid, eriti eraldi aheldamist (separate chaining) ja avatud aadressimist (open addressing). 
Separate chaining: Iga pilu räsitablis on LinkedList ja võimaldab mitmel võtmel eksisteerida samas asukohas räsitablis.

Open addressing: Kõik elemendid on salvestatud räsitabelis endas, sekundaarset andmestruktuuri pole, säästes ruumi, väldib ülekoormust

# Ülesanne 2: Indeksi Kaardistamise (Index Mapping) Rakendamine ja Analüüs 
# 1. Rakenda Index Mapping algoritmi (triviaalne räsimine) kasutades massiive või järjendeid/liste. 
Index Mapping- tehnika, mis kasutab võtmete otsest indeksit nendekaardistamiseks räsitabelis, tööpõhimõte on iga võtme korral teisendada see indeksiks.

Index Mapping näide:
index_mapping.algo4.py
# 2. Analüüsi oma rakenduse aja- ja ruumikomplekssust. 

Indeks mapping algoritmi aja komplekksus on O(1), kuna indeksi leidmine massiivist on kiire ja konstante. Otsimine O(1), kustutamine (1).

Ruumikompkessus on O(n), kuna mälu tuleb reserveerida potentsiaalselt kõigi võimalike indeksite jaoks.

# 3. Aruta, kuidas indeksi kaardistamist massiividega saab rakendada reaalses maailmas. 

Deduplitseerimine - eemaldab duplikaadid nt failikogumtest või mingi süsteemi ID-dest.
Kiire otsing - raamatukogu süsteemis kaardistatud atorite järgi on võimalikteha kiire juurdepääas raamatutele konkreetse autori poolt.


# Ülesanne 3: Separate Chaining Kokkupõrgete Lahendamiseks 
# 1. Rakenda separate chaningut kasutades linked-liste. 
Separate_chaining näide:
separate_chaining.algo4.py

# 2. Võrdle separate chaningu efektiivsust open addressing meetodiga ajalise ja ruumilise komplekssuse mõttes. 

Ajaline komplekssus: 
Separate chaingu kokkupõrked ei suurenda aja komplekssust. Open addressingu ajakomplekssus võib suureneda, eriti kui tekib palju kokkupõrkeid. Samas Open addressing kasutab vähem mälu ja võib teha seega kiiremaid otsinguid. Separate nõuab lisamälu viidete jaoks, jõudlus halveneb, kui põrgete arv suureneb.

Ruumuline komplekssus: 
Separate chaining on ruumikasutuses suurem, kuna igas indeksis võib olla oma ahel, elementide arv pole piiratud räsitabeli suurusega. 
Open Addressingul on aga ruumikasutus väiksem, kuna andmeid hoitakse 
Massiivis, piiratud räsitabeli suurusega, jõudlus aga halveneb kui räsitabel täitub.

# 3. Aruta separate chaning kasutamise plusse ja miinuseid räsitabelites.

Plussid:
Lihtne rakendamine, pole vaja muretseda räsitabeli suuruse pärast ja elementide arv pole piiratud räsitabeli suurusega. Sisestamine, kustutamine ja otsingualgoritmid on efektiivsed, eriti hea räsifunktsiooni korral ja suudab hakkama saada kõrge koormusteguriga.

Miinused: 
Vajab lisamälu viidete jaoks LinkedListis või massiivides. Jõudlus halveneb, kui põrgete arv suureneb ja toimingute tõhusus sõltub räsifunktsiooni kvaliteedist. Jõudlus halveneb ka siis, kui räsitabel täitub.

# Ülesanne 4: Open Addressing Tehnikate Uurimine 
# 1. Kirjuta lühike ülevaade avatud aadressimise meetodist kokkupõrgete lahendamisel räsimises. 
Avatud aadressimise räsimise meetod on see, et kui tekib kokkupõrge  ehk mitmele võtmele antakse samasugune väärtus, siis uus element asetatakse järgmisse vabasse kohta räsitabelis. See on kiire, kuna pole vaja teist struktuuri kokkupõrgete haldamiseks.

# 2. Võrdle (teooria) kolme tehnikat: lineaarne otsing (linear probing), ruuduline otsing (quadratic probing) ja topelträsimine (double hashing). 

Lineaarne otsing: 
Kui põrge tekib, otsitakse järgmist saadaolevat kohta
Lihtne ja kergesti rakendatav.
Määrab iga võtme jaoks algse indeksi, kui põrge tekib liigub funktsioon 
järgmisele indeksile, kuni leitakse tühi koht.
Miinuseks elementide koondumine ühte piirkonda, mis võib vähendada
tõhusust.

Ruuduline otsing:
Avatud aadressimise variatsioon, kus kasutab ruutfunktsiooni tühja koha 
leidmiseks põrke korral. Määrab iga võtme jaoks algse indeksi. Kui põrge tekib, 
liigub funktsioon indeksile, mis on väärtuse ruudu kaugusel.
Miinuseks kui tabel saab täis, võib tekkida pikkade ahelate probleem.

Topelträsimine:
Kasutab kahte räsifunktsiooni ühe asemel. Esimene räsifunktsioon määrab iga võtme jaoks algse indeksi ja kui põrge tekib, 
määrab teine räsifunktsioon võtme 
jaoks uue indeksi. See protsess jätkub kuni leitakse tühi koht.

# 3. Aruta, millistes olukordades iga tehnika oleks kõige efektiivsem. 
Lineaarne otsing -  oleks efektiivne olukordades, kus oleksid lihtsad ja väiksed tabelid. Sobiks ka olukordadesse, kus väärtused on järjestikused ja palju vabu kohti.

Ruuduline otsing - sobiks olukordadesse, kus elementide koondumine ühte piirkonda on tõenäoline või kui lineaarne otsing ei anna tulemusi.

Topelträsimine -  oleks efektiivne suurte tabelite jaoks, toimimaks ka suurematele rakendustele.

# Ülesanne 5: Topelt Räsimise (Double hashing) Rakendamine 
# 1. Rakenda topelt räsimise algoritm ja aruta, kuidas see aitab ületada ühekordse räsimise piiranguid. 
Aitab vähendada klastrite tekke probleeme ja tagab parema võtmete jaotuse.

# 2. Analüüsi oma rakenduse aja- ja ruumikomplekssust. 

Ajakomplekkssus on kas O(1) või O(n), sõltuvalt tabeli suurusest.
Ruumikomplekssus nõuab täiendavat ruumi kahe räsifunktsiooni ja tabeli jaoks. Ruumikasutus suurenebkoos võtmete arvuga.

# 3. Paku välja stsenaarium, kus topelt räsimine oleks eriti efektiivne. 

Topelt räsimine oleks efektiivne tarkvaraarenduses või andmehalduses, kus näiteks andmete jaotus on ebaühtlane või suur tõenäosus kokkupõrgetes ja samas  neid ka tõhusalt lahendada. Topelträsisimine aitaks võtmeväärtusi hajutada ühtlasemalt.


# Boonusülesanne: Koormustegur ja Rehashing (Double hashing vs Rehashing) 
# 1. Selgita, mis on räsitabeli koormustegur ja miks see on oluline.
Määrab, millal räsitabelit suurendada ja mõjutab räsitabeli toimingute tõhusust. Tavaliselt peetakse heaks koormusteguriks 0.7, kui koormustegur muutub liiga suureks, siis suureneb kokkupõrgete tõenäosus.

# 2. Rakenda lihtsat Rehashingu protsessi ja aruta, kuidas see aitab säilitada efektiivset räsitabelit.  

Määratakse, millal koormustegur ületab lävendi. Luuakse suurema suurusega uus räsitabel. Sisestatakse kõik võtmed vanast räsitabelist uude. 


# 3. Analüüsi Rehashingu mõju räsitabeli jõudlusele.

Positiine:

Itab säilitada tasakaalustatud koormusteguri ja tagab räsitabeli tõhususe. Kui koormustegur ületab teatud lävendi, siis käivitatakse rehashing

Negatiivne:

Rehasingu protsess võib olla ajamahukas, eriti suurte räsitabelite juures.
Mälu kasutus võib sellel hetkel suureneda, sest korraga eksisteerib kaks tabelit.

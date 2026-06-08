[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=22220631&assignment_repo_type=AssignmentRepo)
# XatBot2026
- Nom del REPTE: LAN Party
- Equip de treball: 1.4
- Integrants de l'equip:Ismael El Yahmoudi
- Correu electrònic: Ismael.elyahmoudi@inscastellbisbal.net

## 📖 Descripció
__Xatbot intel·ligent__ que s'integra a una pàgina web en forma de widget per a respondre preguntes. Consta d'un Backend construit amb Python i un Frontend construit amb HTML i JavaScript.
Permet personalitzar el comportament del xatbot i proveir-lo de dades a partir d'una base de dades construïda en un document JSON.

## 🎯 Objectius finals
1. Desenvolupament de la Intel·ligència: Crearem un xatbot capaç de respondre preguntes específiques sobre l'esdeveniment (horaris, premis, normativa) utilitzant una base de dades en format JSON i tècniques de Prompt Engineering per assignar-li un rol d'organitzador professional.
2. Integració Web: Un cop el bot sigui funcional, l'integrarem a la pàgina web oficial de la LAN Party mitjançant un widget interactiu per facilitar l'accés a tots els usuaris.
## 🧰 Objectius procedimentals
1. Fer servir Google Gemini API per generar respostes.
2. Aprendre a gestionar API Keys i seguretat bàsica per a que mai quedi exposada cap dada sensible.
3. Gestionar les plataformes Google Colab, ngrok, GitHub i Google AI Studio.
4. Conèixer i treballar amb els formats JSON i MarkDown.
5. Gestionar la documentació del projecte (README, CONTRIBUTING) i les difernets versions i canvis (CHANGELOG)
6. Generació i depuració del codi, documentació, identificació i resolució d'errors mitjançant l'ús correcte de la IA generativa.

## 📦 Requisits
Abans d’iniciar el projecte, assegura’t de disposar de:

1. Google Gemini API Key (Obtenir-la a Google AI Studio)
2. Google Colab o entorn local amb biblioteques necessàries
3. Un entorn de proves per al frontend (Google Sites, WordPress, etc.)
4. Repository de GitHub on gestionar les versions de tots els documents de treball.

## 📂 Estructura del projecte
 📦 xatbot2026\
  ┣ 📂 src # Codi font del backend ┃ \
  &nbsp;&nbsp;&nbsp;&nbsp;┣ 📜 main.ipynb # Backend principal del xatbot ┃ \

  ┣ 📂 frontend # Widget frontend (HTML, CSS, JS) ┃ \
  &nbsp;&nbsp;&nbsp;&nbsp;┗ 📜 index.html # Integració al WordPress 

  ┣ 📂 docs # Documentació del projecte \
  &nbsp;&nbsp;&nbsp;&nbsp;┣ 📜 README.md # Aquest fitxer \
  &nbsp;&nbsp;&nbsp;&nbsp;┣ 📜 CHANGELOG.md # Registre de versions i canvis \
  &nbsp;&nbsp;&nbsp;&nbsp;┗ 📜 CONTRIBUTING.md # Guia per col·laboradors

## 🔧 Instal·lació

1️⃣ Instal·lació de biblioteques i mòduls (Backend)\
2️⃣ Configuració de l’API Key\
3️⃣ Executar el xatbot


## 🔁 Fluxe de dades

🔽 L'usuari escriu una consulta al XatBot (prompt) mitjançant el widget de la pàgina web o FrontEnd.\  
🔽 El FrontEnd envia la consulta al BackEnd (API REST request).\
🔽 El backend processa la consulta de l’usuari afegint-li instruccions de comportament i dades amb les que ha de basar la resposta.\
🔽 El backend envia la consulta a un model de Google Gemini (Gemini API request).\
🔽 El model de Gemini processa la consulta i genera una resposta.\
🔽 El model de Gemini envia la resposta al BackEnd (Gemini API response).\
🔽 El Backend processa la resposta.\
🔽 El Backend envia la resposta cap al frontend  (API REST response.\
🔽 El Frontend mostra la resposta a l’usuari en un widget.

## 👨‍💻 Contribució
Si vols contribuir, segueix les normes indicades a CONTRIBUTING.md.

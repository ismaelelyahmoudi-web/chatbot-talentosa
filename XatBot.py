# 1. INSTAL·LACIÓ DE DEPENDÈNCIES
!pip install -q -U google-genai flask-cors pyngrok beautifulsoup4 requests
!pip install requests==2.32.4

import json, requests, time, re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from flask import Flask, request, jsonify
from flask_cors import CORS
from pyngrok import ngrok
from google.colab import userdata
from google import genai

# --- CONFIGURACIÓ DE SEGURETAT I API ---
try:
    # Connexió amb el model Gemini i Ngrok mitjançant secrets de Colab
    client_ia = genai.Client(api_key=userdata.get('GOOGLE_API_KEY'))
    ngrok.set_auth_token(userdata.get('token_ngrok'))
    print("✅ Autenticació d'Ismael completada amb èxit.")
except Exception as e:
    print(f"❌ Error en la configuració de credencials: {e}")

app_ismael = Flask(__name__)
CORS(app_ismael)

# --- MÒDUL D'EXTRACCIÓ DE CONTINGUTS ---
URL_OBJECTIU = "https://ielyahmoudi.inscastellbisbal.net/"
base_coneixement_ismael = []

def rastrejar_web_completa():
    global base_coneixement_ismael
    visitades = set()
    cua_urls = [URL_OBJECTIU]
    domini_permès = urlparse(URL_OBJECTIU).netloc

    print(f"📡 Iniciant l'escaneig del portafolis d'Ismael: {URL_OBJECTIU}")

    while cua_urls and len(visitades) < 200:
        url_actual = cua_urls.pop(0)

        # Filtre de seguretat per evitar fitxers binaris o rutes d'administració
        if url_actual in visitades or any(ext in url_actual.lower() for ext in ['.jpg', '.png', '.pdf', 'wp-admin', 'wp-json']):
            continue

        try:
            resposta = requests.get(url_actual, timeout=12)
            if resposta.status_code != 200: continue

            nexe = BeautifulSoup(resposta.text, 'html.parser')
            visitades.add(url_actual)

            # Extracció de dades rellevants
            titol_net = nexe.title.string.strip() if nexe.title else "Pàgina d'Ismael"
            paràgrafs = [p.get_text(strip=True) for p in nexe.find_all(['p', 'h1', 'h2', 'h3', 'li'])]
            text_acumulat = " ".join([txt for txt in paràgrafs if len(txt) > 10])

            if len(text_acumulat) > 50:
                base_coneixement_ismael.append({
                    "enllaç": url_actual,
                    "titol": titol_net,
                    "contingut": text_acumulat
                })
                print(f"📥 Pàgina indexada: {titol_net}")

            # Cerca de nous enllaços interns
            for a in nexe.find_all('a', href=True):
                enllaç_complet = urljoin(URL_OBJECTIU, a['href'])
                if urlparse(enllaç_complet).netloc == domini_permès and enllaç_complet not in visitades:
                    cua_urls.append(enllaç_complet)

        except Exception:
            continue

    # Emmagatzematge local de les dades extretes
    with open('dades_ismael_web.json', 'w', encoding='utf-8') as f:
        json.dump(base_coneixement_ismael, f, ensure_ascii=False, indent=4)
    print(f"\n📂 Base de dades d'Ismael generada amb {len(base_coneixement_ismael)} entrades.")

# --- LÒGICA DE CERCA I RESPOSTA ---
def cercar_context_rellevant(pregunta, top_n=3):
    termes = re.findall(r'\w+', pregunta.lower())
    puntuacions = []

    for entrada in base_coneixement_ismael:
        text_full = (entrada['titol'] + " " + entrada['contingut']).lower()
        score = sum(1 for t in termes if len(t) > 3 and t in text_full)
        puntuacions.append((score, entrada))

    # Ordenem per rellevància
    puntuacions.sort(key=lambda x: x[0], reverse=True)
    return [p[1] for p in puntuacions[:top_n]]

def processar_amb_ia(usuari_input):
    context_seleccionat = cercar_context_rellevant(usuari_input)

    instruccions = "Ets l'assistent personal del web de l'Ismael El Yahmoudi. " \
                   "Respon de manera educada i en català. Utilitza exclusivament la " \
                   "informació que t'ofereixo a continuació per respondre:\n\n"

    for c in context_seleccionat:
        instruccions += f"FONT: {c['titol']}\nTEXT: {c['contingut'][:600]}\n---\n"

    execució = client_ia.models.generate_content(
        model="gemini-1.5-flash",
        contents=f"{instruccions}\n\nPregunta de l'usuari: {usuari_input}"
    )
    return execució.text

# --- SERVIDOR FLASK ---
@app_ismael.route('/preguntar', methods=['POST'])
def api_chat():
    try:
        dades = request.json
        missatge = dades.get("message")
        print(f"📩 Consulta rebuda: {missatge}")

        resposta_final = processar_amb_ia(missatge)
        return jsonify({"reply": resposta_final})
    except Exception as err:
        return jsonify({"reply": f"S'ha produït un error tècnic: {str(err)}"}), 500

if __name__ == '__main__':
    # Pas 1: Extreure dades del web d'Ismael
    !pkill ngrok
    time.sleep(2)
    url_publica = ngrok.connect(5000).public_url
    print(f"\n COPIA AQUESTA URL AL TEU WORDPRESS:\n{url_publica}/ask\n")


    # Pas 2: Llançar el túnel i el servidor
    !pkill ngrok
    time.sleep(2)
    url_publica = ngrok.connect(5000).public_url
# Pas 3: Configuració del servidor flask
    app = Flask(_name_)
    CORS(app) #Permet peticions externs (CORS) per al meu WordPress
    print(f"\n🚀 SERVIDOR D'ISMAEL ACTIU")
    print(f"🔗 Endpoint per a la teva web: {url_publica}/preguntar\n")

    app_ismael.run(port=5000)

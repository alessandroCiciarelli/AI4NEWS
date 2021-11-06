import streamlit as st
from newsapi import NewsApiClient
from datetime import datetime
from gtts import gTTS

st.set_page_config(page_title="Le news Intelligenti", page_icon=None, layout='wide', initial_sidebar_state='auto')


#ottengo sorgeti notizie in Italia
def nomi_sorgenti():
	#carico tutte le sorgeti di notizie
	sorgenti = newsapi.get_sources(language="it")
	nomi_sorgenti = []
	for l in sorgenti["sources"]:
		nomi_sorgenti.append(l["id"])
	return nomi_sorgenti	

#carico token accesso Api #1
newsapi = NewsApiClient(api_key='d78564fc55a6473c9597520ee6a386e8')

#carico token accesso Api #2
newsapi2 = NewsApiClient(api_key='e73ec2d966a7418f86ea1ee40e808da9')

#carico token accesso Api #3
newsapi3 = NewsApiClient(api_key='e6a433d56f744e9bb49d14c9ac86aa3c')

#carico token accesso Api #4
newsapi4 = NewsApiClient(api_key='7f10c40670f8482f8bcdda424f763e8e')

#carico token accesso Api #5
newsapi5 = NewsApiClient(api_key='7a8083f426c14292902588162ba1468d')


st.markdown("<h1 style='text-align: center; background-color:black; font-size:28px;'><bold style='color:rgb(102, 255, 51);'> A.I. <bold style='color:white;'> FOR <bold style='color:rgb(255, 26, 26);'> NEWS </bold></bold></bold></h1>", unsafe_allow_html=True)
st.write('<p style="text-align: center;font-size:15px;" >Non <bold>sei stanco di dover girare decine di siti internet solo per essere aggiornato</bold> su ciò che succede nel mondo o per <bold>sapere di più sui tuoi argomenti preferiti ?</bold><p>', unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)  
    st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">', unsafe_allow_html=True)  

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)


def controllaCampo(campo):
	if campo is not None:
		return campo
	else:
		return "Non Disponibile"
		
def stampa_Notizie(notizie_da_Stapare):

	for n in notizie_da_Stapare["articles"]:
		titolo = controllaCampo(n["title"])
		descrizione = controllaCampo(n["description"])
		data = controllaCampo(n["publishedAt"])
		link = controllaCampo(n["url"])
		autore = controllaCampo(n["author"])
		immagine = controllaCampo(n["urlToImage"])
		with st.expander(titolo):
			tts = gTTS(text=descrizione, lang="it", slow=False)
			tts.save("notizia.mp3")
			audio_file = open('notizia.mp3', 'rb')
			audio_bytes = audio_file.read()
			st.markdown("<div class='col-12 news'>\
			<div class='row'>\
			<div class='col-7'><br><img src='" + immagine + "' class='figure-img img-fluid rounded'><br></div>\
			<div class='col-5'><br><h6>Info Notizia<br><br></h6><br><p>Data : " + data[:10] +"</p><p>Autore : " + autore +"</p><a href='"+ link + "' class=''>Link Notizia Completa</a></div>", unsafe_allow_html=True)
			st.markdown("<br><p>Ascolta la descrizione della notizia</p>",unsafe_allow_html=True)
			st.audio(audio_bytes, format='audio/mp3')
			st.markdown("<br>",unsafe_allow_html=True)
			

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

argomenti = ["Intelligenza Artificiale",
	        "Machine Learning",
		"Robotica",
		"Realtà virtuale",
		"Sicurezza informatica",
		"Tecnologia",
		"Scienza dei dati",
		"Criptovalute",
		"Big tech"]
argomenti_selezionati = st.multiselect('Seleziona uno o più argomenti per le ultime notizie', argomenti,default=argomenti)


Scelte = ["Notizie del Momento","Notizie Popolari","Ultime Notizie","Cerca le notizie su ciò che ti interessa"]
Scelta = st.selectbox("Seleziona quali notizie vedere",Scelte)



if Scelta == "Ultime Notizie" :
	st.markdown("<br><br>",unsafe_allow_html=True)
	for a in argomenti_selezionati:
		all_articles = newsapi.get_everything(q=a,
                                     language='it',
                                     sort_by='publishedAt',
                                     page_size=2)
		stampa_Notizie(all_articles)
		

elif Scelta == "Notizie del Momento" :
	st.markdown("<br><br>",unsafe_allow_html=True)
	for a in argomenti_selezionati:
		all_articles = newsapi2.get_everything(q=a,
                                     language='it',
                                     sort_by='relevancy',
                                     page_size=2)
		stampa_Notizie(all_articles)
	
elif Scelta == "Notizie Popolari" :
	st.markdown("<br><br>",unsafe_allow_html=True)
	for a in argomenti_selezionati:
		all_articles = newsapi3.get_everything(q=a,
                                     language='it',
                                     sort_by='popularity',
                                     page_size=2)
		stampa_Notizie(all_articles)
	
	
elif Scelta == "Cerca le notizie su ciò che ti interessa":
	col1,col2 = st.beta_columns([5,1])
	testo_ricerca = col1.text_input("Su quale agomento desideri leggere le ultime notizie ? ","Intelligenza Artificiale")
	button_clicked = col2.button("Cerca")
	ricerca_avanzata = st.checkbox("Abilita ricerca avanzata")
	if ricerca_avanzata:
		sorgenti = nomi_sorgenti()
		col3,col4 = st.beta_columns(2)
		sorgenti_selezionate = col3.multiselect('Seleziona una o più sorgenti per le ultime notizie', sorgenti,default=sorgenti)
		s_s = ""
		for s in sorgenti_selezionate:
			s_s = s_s + s + ","
		print(s_s)
		sort = col4.radio("Come vuoi che siano ordinate le notizie",('Pubblicazione', 'Rilevanza', 'Popolarità'))
		if(sort == 'Pubblicazione'):
			sort='publishedAt'
		elif(sort == 'Rilevanza'):
			sort='relevancy'
		elif(sort == 'Popolarità'):
			sort='popularity'
			
		risultati_ricerca = st.number_input("Seleziona Numero Massimo notizie ",1,15,5,1)
		
		if button_clicked :
			print(testo_ricerca,sorgenti_selezionate,sort,risultati_ricerca)
			st.markdown("<br><br>",unsafe_allow_html=True)
			all_articles = newsapi4.get_everything(q=testo_ricerca,
		                              sources=s_s,
		                              sort_by=sort,
		                              page_size=risultati_ricerca)

			stampa_Notizie(all_articles)
				
	else:
		if button_clicked :
			top_headlines = newsapi5.get_everything(q=testo_ricerca,page_size=10,language='it')
			st.markdown("<br><br>",unsafe_allow_html=True)
			stampa_Notizie(top_headlines)
	

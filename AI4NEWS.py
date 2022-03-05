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


st.markdown("<h1 style='text-align: center; background-color:black; font-size:28px;'><b style='color:rgb(102, 255, 51);'> A.I. <b style='color:white;'> FOR <b style='color:rgb(255, 26, 26);'> NEWS </b></b></b></h1>", unsafe_allow_html=True)
st.write('<p style="text-align: left;font-size:15px;" ><b>Le notizie più importanti e più popolari sull\'intelligenza artificiale, accuratamente selezionate dai nostri algoritmi dotati di I.A. solo per te</b><p>', unsafe_allow_html=True)

st.markdown('<iframe width="100%" height="auto" src="https://rss.app/embed/v1/magazine/C3ws5QRv5zQnUXwb" frameborder="0"></iframe><br>', unsafe_allow_html=True)



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
			st.markdown("<div class=''>\
			<div class='row'>\
			<div class='col-12'><br><img src='" + immagine + "' class='figure-img img-fluid rounded'><br></div>\
			<div class='col-12'><br><h6>Info Notizia<br><br></h6><br><p>Data : " + data[:10] +"</p><p>Autore : " + autore +"</p><a href='"+ link + "' class=''>Link Notizia Completa</a></div>", unsafe_allow_html=True)
			st.markdown("<br><p>Ascolta la descrizione della notizia</p>",unsafe_allow_html=True)
			st.audio(audio_bytes, format='audio/mp3')
			st.markdown("<br>",unsafe_allow_html=True)

def stampa_Notizie_new(notizie_da_Stapare):
	i=0
	for n in notizie_da_Stapare["articles"]:
		i = i+1
		titolo = controllaCampo(n["title"])
		descrizione = controllaCampo(n["description"])
		data = controllaCampo(n["publishedAt"])
		link = controllaCampo(n["url"])
		autore = controllaCampo(n["author"])
		immagine = controllaCampo(n["urlToImage"])

		#tts = gTTS(text=descrizione, lang="it", slow=False)
		#tts.save("notizia"+str(i)+".mp3")
		#audio_file = open('notizia'+str(i)+'.mp3', 'rb')
		#audio_bytes = audio_file.read()
		st.markdown("<center>\
		<div class='row' style='margin-bottom:15px;width:90%;border:3px inset #b4b6b7;border-width:3px;border-style:inset;border-color:#b4b6b7;padding:15px;margin-bottom: 10px;'>\
  		<h3 style='text-align: left;'>"+titolo+"</h3><br><br><div class='row'>\
  		<div class='col-sm-4'><img src='" + immagine + "' class='figure-img img-fluid rounded' style=''>\
		</div><div class='col-sm-8' style='text-align: left;'>\
		<br><h5><b>Info Notizia</b></h5>\
		<p><b>Data :</b>" + data[:10] +"</p>\
		<p><b>Autore : </b>" + autore +"</p>\
		<p><b>Descrizione breve : </b>" + descrizione +"</p>\
		<b>Vuoi leggere tutta la notizia : </b><a href='"+ link + "' class=''>Link Notizia Completa</a>\
		</div>" , unsafe_allow_html=True)
		#st.audio(audio_bytes, format='audio/mp3')
		#st.markdown("<br>",unsafe_allow_html=True)

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

argomenti_selezionati = ["Intelligenza Artificiale",
	        "Machine Learning",
		"Robotica",
		"Realtà virtuale",
		"Sicurezza informatica",
		"Tecnologia",
		"Scienza dei dati",
		"Criptovalute",
		"Big tech"]
#argomenti_selezionati = st.multiselect('Seleziona uno o più argomenti per leggere le ultime notizie sull\'intelligenza artificiale e rimanere aggiornato sugli ultimi sviluppi', argomenti,default=argomenti)


Scelte = ["Ultime Notizie","Notizie del Momento","Notizie Popolari","Cerca le notizie su ciò che ti interessa"]
Scelta = st.selectbox("Seleziona quali notizie vedere",Scelte)



if Scelta == "Ultime Notizie" :
	st.markdown("<br><br>",unsafe_allow_html=True)
	for a in argomenti_selezionati:
		all_articles = newsapi.get_everything(q=a,
                                     language='it',
                                     sort_by='publishedAt',
                                     page_size=2)
		stampa_Notizie_new(all_articles)
		

elif Scelta == "Notizie del Momento" :
	st.markdown("<br><br>",unsafe_allow_html=True)
	for a in argomenti_selezionati:
		all_articles = newsapi2.get_everything(q=a,
                                     language='it',
                                     sort_by='relevancy',
                                     page_size=2)
		stampa_Notizie_new(all_articles)
	
elif Scelta == "Notizie Popolari" :
	st.markdown("<br><br>",unsafe_allow_html=True)
	for a in argomenti_selezionati:
		all_articles = newsapi3.get_everything(q=a,
                                     language='it',
                                     sort_by='popularity',
                                     page_size=2)
		stampa_Notizie_new(all_articles)
	
	
elif Scelta == "Cerca le notizie su ciò che ti interessa":
	col1,col2 = st.columns([5,1])
	testo_ricerca = col1.text_input("Su quale agomento desideri leggere le ultime notizie ? ","Intelligenza Artificiale")
	button_clicked = col2.button("Cerca")
	ricerca_avanzata = st.checkbox("Abilita ricerca avanzata")
	if ricerca_avanzata:
		sorgenti = nomi_sorgenti()
		col3,col4 = st.columns(2)
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
			
		risultati_ricerca = st.number_input("Seleziona Numero Massimo notizie ",1,10,5,1)
		
		if button_clicked :
			print(testo_ricerca,sorgenti_selezionate,sort,risultati_ricerca)
			st.markdown("<br><br>",unsafe_allow_html=True)
			all_articles = newsapi4.get_everything(q=testo_ricerca,
		                              sources=s_s,
		                              sort_by=sort,
		                              page_size=risultati_ricerca)

			stampa_Notizie_new(all_articles)
				
	else:
		if button_clicked :
			top_headlines = newsapi5.get_everything(q=testo_ricerca,page_size=10,language='it')
			st.markdown("<br><br>",unsafe_allow_html=True)
			stampa_Notizie_new(top_headlines)
	

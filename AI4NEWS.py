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
st.write('<p style="text-align: center;font-size:15px;" ><b>Le notizie più importanti e più popolari sull\'intelligenza artificiale, accuratamente selezionate dai nostri algoritmi dotati di I.A. solo per te</b><p>', unsafe_allow_html=True)

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
		st.markdown("<center><div class='' style='width:90%;border:3px inset #b4b6b7;border-width:3px;border-style:inset;border-color:#b4b6b7;border-radius:10px 25px 25px 30px;-moz-border-radius:10px 25px 25px 30px;-webkit-border-radius:10px 25px 25px 30px;padding:15px;margin-bottom: 25px;'>\
		<h3 style='text-align: left;'>"+titolo+"</h3><div class='row'  style='text-align: center; >\
		<br><div class='col col-sm-12' style='text-align: center;padding:15px;'><br>\
		<img src='" + immagine + "' class='figure-img img-fluid rounded' style='height:200px; margin:15px;'>\
		</div>\
		<div class='col col-sm-12' style='text-align: left;'>\
		<br>\
		<h5><b>Info Notizia</b></h5>\
		<p><b>Data :</b>" + data[:10] +"</p>\
		<p><b>Autore : </b>" + autore +"</p>\
		<p><b>Descrizione breve : </b>" + descrizione +"</p>\
		<b>Vuoi leggere tutta la notizia : </b><a href='"+ link + "' class=''>Link Notizia Completa</a>\
		</div>" + 
		"""<center><br><br><hr><br><div style='text-align: center;'>
		<a class="resp-sharing-button__link" href="https://facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.intelligenzaartificialeitalia.net%2Fnewsintelligenzaartificiale" target="_blank" rel="noopener" aria-label="Condividi su Facebook">
		  <div class="resp-sharing-button resp-sharing-button--facebook resp-sharing-button--medium"><div aria-hidden="true" class="resp-sharing-button__icon resp-sharing-button__icon--solid">
		    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M18.77 7.46H14.5v-1.9c0-.9.6-1.1 1-1.1h3V.5h-4.33C10.24.5 9.5 3.44 9.5 5.32v2.15h-3v4h3v12h5v-12h3.85l.42-4z"/></svg></div>Condividi su Facebook</div>
		</a>
		<a class="resp-sharing-button__link" href="https://twitter.com/intent/tweet/?text=Tutte%20le%20Notizie%20sull&#x27;Intelligenza%20Artificiale%20in%20un%20Unico%20Posto%20&amp;url=https%3A%2F%2Fwww.intelligenzaartificialeitalia.net%2Fnewsintelligenzaartificiale" target="_blank" rel="noopener" aria-label="Condividi su Twitter">
		  <div class="resp-sharing-button resp-sharing-button--twitter resp-sharing-button--medium"><div aria-hidden="true" class="resp-sharing-button__icon resp-sharing-button__icon--solid">
		    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M23.44 4.83c-.8.37-1.5.38-2.22.02.93-.56.98-.96 1.32-2.02-.88.52-1.86.9-2.9 1.1-.82-.88-2-1.43-3.3-1.43-2.5 0-4.55 2.04-4.55 4.54 0 .36.03.7.1 1.04-3.77-.2-7.12-2-9.36-4.75-.4.67-.6 1.45-.6 2.3 0 1.56.8 2.95 2 3.77-.74-.03-1.44-.23-2.05-.57v.06c0 2.2 1.56 4.03 3.64 4.44-.67.2-1.37.2-2.06.08.58 1.8 2.26 3.12 4.25 3.16C5.78 18.1 3.37 18.74 1 18.46c2 1.3 4.4 2.04 6.97 2.04 8.35 0 12.92-6.92 12.92-12.93 0-.2 0-.4-.02-.6.9-.63 1.96-1.22 2.56-2.14z"/></svg></div>Condividi su Twitter</div>
		</a>
		<a class="resp-sharing-button__link" href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https%3A%2F%2Fwww.intelligenzaartificialeitalia.net%2Fnewsintelligenzaartificiale&amp;title=Tutte%20le%20Notizie%20sull&#x27;Intelligenza%20Artificiale%20in%20un%20Unico%20Posto%20&amp;summary=Tutte%20le%20Notizie%20sull&#x27;Intelligenza%20Artificiale%20in%20un%20Unico%20Posto%20&amp;source=https%3A%2F%2Fwww.intelligenzaartificialeitalia.net%2Fnewsintelligenzaartificiale" target="_blank" rel="noopener" aria-label="Condividi su LinkedIn">
		  <div class="resp-sharing-button resp-sharing-button--linkedin resp-sharing-button--medium"><div aria-hidden="true" class="resp-sharing-button__icon resp-sharing-button__icon--solid">
		    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M6.5 21.5h-5v-13h5v13zM4 6.5C2.5 6.5 1.5 5.3 1.5 4s1-2.4 2.5-2.4c1.6 0 2.5 1 2.6 2.5 0 1.4-1 2.5-2.6 2.5zm11.5 6c-1 0-2 1-2 2v7h-5v-13h5V10s1.6-1.5 4-1.5c3 0 5 2.2 5 6.3v6.7h-5v-7c0-1-1-2-2-2z"/></svg></div>Condividi su LinkedIn</div>
		</a>
		<a class="resp-sharing-button__link" href="whatsapp://send?text=Tutte%20le%20Notizie%20sull&#x27;Intelligenza%20Artificiale%20in%20un%20Unico%20Posto%20%20https%3A%2F%2Fwww.intelligenzaartificialeitalia.net%2Fnewsintelligenzaartificiale" target="_blank" rel="noopener" aria-label="Condividi su WhatsApp">
		  <div class="resp-sharing-button resp-sharing-button--whatsapp resp-sharing-button--medium"><div aria-hidden="true" class="resp-sharing-button__icon resp-sharing-button__icon--solid">
		    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20.1 3.9C17.9 1.7 15 .5 12 .5 5.8.5.7 5.6.7 11.9c0 2 .5 3.9 1.5 5.6L.6 23.4l6-1.6c1.6.9 3.5 1.3 5.4 1.3 6.3 0 11.4-5.1 11.4-11.4-.1-2.8-1.2-5.7-3.3-7.8zM12 21.4c-1.7 0-3.3-.5-4.8-1.3l-.4-.2-3.5 1 1-3.4L4 17c-1-1.5-1.4-3.2-1.4-5.1 0-5.2 4.2-9.4 9.4-9.4 2.5 0 4.9 1 6.7 2.8 1.8 1.8 2.8 4.2 2.8 6.7-.1 5.2-4.3 9.4-9.5 9.4zm5.1-7.1c-.3-.1-1.7-.9-1.9-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.1-.2.2-.3.2-.6.1s-1.2-.5-2.3-1.4c-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.5.1-.6s.3-.3.4-.5c.2-.1.3-.3.4-.5.1-.2 0-.4 0-.5C10 9 9.3 7.6 9 7c-.1-.4-.4-.3-.5-.3h-.6s-.4.1-.7.3c-.3.3-1 1-1 2.4s1 2.8 1.1 3c.1.2 2 3.1 4.9 4.3.7.3 1.2.5 1.6.6.7.2 1.3.2 1.8.1.6-.1 1.7-.7 1.9-1.3.2-.7.2-1.2.2-1.3-.1-.3-.3-.4-.6-.5z"/></svg></div>Condividi su WhatsApp</div>
		</a>
		</div></center>
		""" , unsafe_allow_html=True)
		#st.audio(audio_bytes, format='audio/mp3')
		#st.markdown("<br>",unsafe_allow_html=True)


			

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
argomenti_selezionati = st.multiselect('Seleziona uno o più argomenti per leggere le ultime notizie sull\'intelligenza artificiale e rimanere aggiornato sugli ultimi sviluppi', argomenti,default=argomenti)


Scelte = ["Notizie del Momento","Notizie Popolari","Ultime Notizie","Cerca le notizie su ciò che ti interessa"]
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
	

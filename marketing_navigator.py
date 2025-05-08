import streamlit as st

# Initialiseer sessie
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.responses = []
    st.session_state.name = ''
    st.session_state.email = ''

# Vragen per deelgebied
questions = {
    "Strategie en positionering": [
        "We hebben een duidelijke en onderscheidende positionering in de markt.",
        "Onze missie, visie en kernwaarden zijn scherp geformuleerd en bekend binnen het team.",
        "Onze strategische doelstellingen zijn helder en meetbaar.",
        "We hebben inzicht in onze concurrentie en hoe wij ons onderscheiden.",
        "Onze positionering sluit aan bij de behoeften van onze doelgroep.",
        "We hebben een langetermijnstrategie die regelmatig wordt geëvalueerd.",
        "Onze strategie wordt gedragen door alle afdelingen binnen de organisatie.",
        "We passen onze strategie aan op basis van marktontwikkelingen.",
        "Onze unieke waardepropositie is duidelijk voor onze klanten.",
        "We communiceren onze strategie effectief naar externe stakeholders."
    ],
    "Klantinzicht": [
        "We hebben duidelijke klantsegmenten gedefinieerd.",
        "We kennen de behoeften en het gedrag van onze klanten goed.",
        "We gebruiken klantdata actief voor marketingdoeleinden.",
        "We voeren regelmatig klanttevredenheidsonderzoeken uit.",
        "Onze klantinzichten worden gedeeld binnen het team.",
        "We hebben inzicht in de klantreis van onze doelgroepen.",
        "We verzamelen feedback op meerdere contactmomenten.",
        "We analyseren klantgedrag om onze diensten te verbeteren.",
        "We segmenteren klanten op basis van waarde en gedrag.",
        "We gebruiken persona's om onze marketing te richten."
    ],
    "Waardepropositie": [
        "Onze producten/diensten bieden unieke waarde voor onze klanten.",
        "We communiceren duidelijk wat onze klantvoordelen zijn.",
        "Onze propositie sluit aan op de belangrijkste klantbehoeften.",
        "We passen onze waardepropositie regelmatig aan op basis van feedback.",
        "We kunnen onze waardepropositie in één zin duidelijk maken.",
        "Onze waardepropositie is consistent over alle kanalen heen.",
        "We testen regelmatig nieuwe proposities in de markt.",
        "Onze medewerkers kunnen de waardepropositie helder uitleggen.",
        "We vergelijken onze propositie met die van concurrenten.",
        "Onze propositie is afgestemd op verschillende klantsegmenten."
    ],
    "Contentstrategie": [
        "We hebben een contentplan met doelen, thema’s en formats.",
        "Onze content sluit aan op de klantreis.",
        "We publiceren consistent nieuwe content.",
        "Onze content is afgestemd op onze doelgroepen.",
        "We meten het effect van onze contentmarketing.",
        "We gebruiken verschillende contenttypes (blogs, video's, etc.).",
        "Onze content wordt verspreid via de juiste kanalen.",
        "We hergebruiken en optimaliseren bestaande content.",
        "We hebben een redactionele kalender die we volgen.",
        "Onze content draagt bij aan leadgeneratie en conversie."
    ],
    "Kanalen en middelen": [
        "We hebben de juiste (online/offline) kanalen gekozen voor onze doelgroep.",
        "We gebruiken deze kanalen strategisch en consistent.",
        "Onze middelenmix ondersteunt onze doelen effectief.",
        "We stemmen middelen goed op elkaar af qua boodschap en timing.",
        "We evalueren periodiek het rendement van onze middelen.",
        "We passen onze kanaalstrategie aan op basis van prestaties.",
        "We integreren nieuwe kanalen wanneer relevant.",
        "Onze middelen zijn afgestemd op de klantvoorkeuren.",
        "We hebben een duidelijke budgetverdeling over kanalen.",
        "We trainen ons team in het effectief gebruiken van kanalen."
    ],
    "Campagnes en activatie": [
        "We voeren regelmatig campagnes om leads/klanten te activeren.",
        "Onze campagnes hebben duidelijke doelstellingen en KPI’s.",
        "We gebruiken creatieve en impactvolle boodschappen.",
        "Onze campagnes zijn goed getimed en gepland.",
        "We meten en evalueren onze campagnes systematisch.",
        "We segmenteren onze campagnes op basis van doelgroep.",
        "We testen verschillende campagnevarianten voor optimalisatie.",
        "Onze campagnes zijn geïntegreerd over meerdere kanalen.",
        "We gebruiken automatisering waar mogelijk in campagnes.",
        "Onze campagnes dragen bij aan merkbekendheid en conversie."
    ],
    "Meten en optimaliseren": [
        "We maken gebruik van dashboards of rapportages om prestaties te meten.",
        "We evalueren periodiek onze marketinginspanningen.",
        "We gebruiken data actief om te optimaliseren.",
        "We testen en experimenteren regelmatig met nieuwe aanpakken.",
        "We gebruiken inzichten voor continue verbetering.",
        "Onze KPI's zijn duidelijk gedefinieerd en worden gemonitord.",
        "We delen inzichten en resultaten binnen het team.",
        "We gebruiken A/B-testing voor optimalisatie.",
        "We analyseren klantfeedback voor verbeteringen.",
        "Onze rapportages leiden tot concrete actiepunten."
    ],
    "Organisatie en processen": [
        "Marketing is goed verankerd in onze organisatie.",
        "Onze interne processen voor marketing zijn duidelijk en efficiënt.",
        "Taken en verantwoordelijkheden binnen marketing zijn helder verdeeld.",
        "We beschikken over voldoende kennis en capaciteit.",
        "We werken effectief samen met externe partners indien nodig.",
        "Onze marketingprocessen worden regelmatig geëvalueerd.",
        "We investeren in training en ontwikkeling van het marketingteam.",
        "Er is een cultuur van samenwerking tussen marketing en andere afdelingen.",
        "We hebben duidelijke procedures voor campagne-uitvoering.",
        "Onze marketingafdeling is flexibel en kan snel inspelen op veranderingen."
    ]
}

# Vlak alle vragen uit
def flatten_questions(questions):
    return [(cat, q) for cat in questions for q in questions[cat]]

flat_questions = flatten_questions(questions)

# Analyse en export
def analyse_and_export():
    result = {}
    scores = st.session_state.responses
    idx = 0
    for category, qs in questions.items():
        set_scores = scores[idx:idx+len(qs)]
        idx += len(qs)
        avg = round(sum(set_scores)/len(set_scores), 2)
        result[category] = avg

    st.subheader("🔍 Jouw Analyse")
    for category, avg in sorted(result.items(), key=lambda x: x[1]):
        priority = "Hoog" if avg < 3 else ("Gemiddeld" if avg < 4 else "Laag")
        st.write(f"**{category}**: {avg} → Prioriteit: {priority}")

    submitted_info = {
        "Naam": st.session_state.name,
        "E-mail": st.session_state.email,
        "Scores per deelgebied": result
    }
    st.download_button("📥 Download jouw resultaten", str(submitted_info), file_name="marketing_navigator_resultaten.txt")

# UI
st.title("📊 Marketing Navigator")

if not st.session_state.name:
    st.session_state.name = st.text_input("Wat is je naam?")
    st.session_state.email = st.text_input("Wat is je e-mailadres?")
    if st.session_state.name and st.session_state.email:
        st.experimental_rerun()
else:
    total = len(flat_questions)
    q_index = st.session_state.question_index

    if q_index < total:
        category, question = flat_questions[q_index]
        st.write(f"Vraag {q_index+1} van {total} ({category})")
        score = st.slider(question, 1, 5, 3, key=f"slider_{q_index}")
        if st.button("Volgende vraag"):
            st.session_state.responses.append(score)
            st.session_state.question_index += 1
    else:
        analyse_and_export()

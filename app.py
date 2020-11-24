from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from flask import Flask, render_template, request
import docx
import os
from docx.shared import Pt
from docx.shared import Inches
from docx.shared import RGBColor


app = Flask(__name__)




@app.route('/', methods=['get','post'])
def index():
    if request.method == 'POST':
        titre = request.form['titre']
        password = request.form['password']
        print('titre:', titre, 'password:', password)

        return 'traitement'
    else:
        return render_template('index.html')

@app.route('/post-login', methods=['get','post'])
def login():
    sujet = request.form['sujet']
    type = request.form['type']
    date = request.form['date']
    serv = request.form['serv']
    numero = request.form['numero']
    source = request.form['source']
    client = request.form['client']
    description = request.form['description']
    doc = Document()
    section = doc.sections[0]
    header = section.header
    paragraph = header.paragraphs[0]
    paragraph.text = "\tCyber Security Innovation – Response Team"
    font = paragraph.style.font
    font.name = 'Hanzel Extended'
    font.size = Pt(14)
    font.color.rgb = RGBColor(19, 32, 223)


    parag = doc.add_paragraph()

    titre1 = parag.add_run('\t \t \tSecurity Bulletin N°' + client + ' ')
    font = titre1.font
    font.name = 'Cambria (Headings)'
    font.size = Pt(14)

    titre2 = parag.add_run(type)
    font = titre2.font
    font.name = 'Cambria (Headings)'
    font.size = Pt(14)
    font.color.rgb = RGBColor(0, 51, 102)
    font.bold = True

    if (serv == "Elévé"):
        font.color.rgb = RGBColor(255, 0, 0)
    elif (serv == "Moyenne"):
        font.color.rgb = RGBColor(0, 51, 102)
    else:
        font.color.rgb = RGBColor(0, 153, 0)

    titre3 = parag.add_run('-')
    font = titre3.font
    font.name = 'Cambria (Headings)'
    font.size = Pt(14)
    font.color.rgb = RGBColor(255, 128, 0)
    font.bold = True


    if (serv == "Elévé"):
        font.color.rgb = RGBColor(255, 0, 0)
    elif (serv == "Moyenne"):
        font.color.rgb = RGBColor(0, 51, 102)
    else:
        font.color.rgb = RGBColor(0, 153, 0)

    titre4 = parag.add_run(date + '-' + numero + '\n')
    font = titre4.font
    font.name = 'Cambria (Headings)'
    font.size = Pt(14)
    font.color.rgb = RGBColor(255, 128, 0)
    font.bold = True

    if (serv == "Elévé"):
        font.color.rgb = RGBColor(255, 0, 0)
    elif (serv == "Moyenne"):
        font.color.rgb = RGBColor(0, 51, 102)
    else:
        font.color.rgb = RGBColor(0, 153, 0)

    titre5 = parag.add_run('Sujet: '+sujet+'\n')
    font = titre5.font
    font.name = 'Calibri (Body)'
    font.size = Pt(14)
    font.bold = True

    titre6 = parag.add_run("Référence:")
    font = titre6.font
    font.name = 'Cambria (Headings)'
    font.size = Pt(14)
    font.bold = True

    titre7 = parag.add_run(type + '-' + date + '-'+numero + '\n')
    font = titre7.font
    font.name = 'Calibri (Body)'
    font.size = Pt(16)
    font.color.rgb = RGBColor(255, 128, 0)
    font.bold = True
    if (serv == "Elévé"):
        font.color.rgb = RGBColor(255, 0, 0)
    elif (serv == "Moyenne"):
        font.color.rgb = RGBColor(0, 51, 102)
    else:
        font.color.rgb = RGBColor(0, 153, 0)

    titre8 = parag.add_run("Sévérité: ")
    font = titre8.font
    font.name = 'Calibri (Body)'
    font.size = Pt(14)
    font.bold = True

    titre9 = parag.add_run(serv + '\n')
    font = titre9.font
    font.name = 'Liberation Serif'
    font.size = Pt(16)
    font.color.rgb = RGBColor(255, 128, 0)
    font.bold = True
    if (serv == "Elévé"):
        font.color.rgb = RGBColor(255, 0, 0)
    elif (serv == "Moyenne"):
        font.color.rgb = RGBColor(0, 51, 102)
    else:
        font.color.rgb = RGBColor(0, 153, 0)

    titre10 = parag.add_run('Description: \n')
    font = titre10.font
    font.name = 'Calibri (Body)'
    font.size = Pt(14)
    font.bold = True

    titre11 = parag.add_run(description + '\n')
    font = titre11.font
    font.name = 'Calibri (Body)'
    font.size = Pt(14)

    titre12 = parag.add_run('Source: \n')
    font = titre12.font
    font.name = 'Calibri (Body)'
    font.size = Pt(14)
    font.bold = True

    titre13 = parag.add_run(source)
    font = titre13.font
    font.name = 'Calibri (Body)'
    font.size = Pt(14)

    doc.save("Bulletin_"+client+"-"+type+"_"+date+"_"+numero+"_"+sujet+".docx")
    os.system("start Bulletin_"+client+"-"+type+"_"+date+"_"+numero+"_"+sujet+".docx")
    return "Bulletin Crée"

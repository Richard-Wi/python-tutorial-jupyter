import re

def regEx_filter(output_content):
    #regex für: lösche alle - (wegen Satzumbrüchen könnten sonst sol-che wör-ter entstehen)
    addline1 = re.sub('-','',output_content)
    #regex für: Entferne alle Escapesequenzen für Zeilenumbrüche
    addline2 = re.sub('\n',' ', addline1)
    addline3 = re.sub('\sn\s','', addline2)
    #regex für: lösche alle Sachen die keine Wörter sind(Satzzeichen etc.)
    newlines1 = re.sub('\W',' ', addline3)
    #regex für: lösche alle doppelten leerstellen
    spacedelines1 = re.sub('\s\s+',' ',newlines1)
    #regex für: tausche alle Leerstellen gegen kommata aus
    kommalines1 = spacedelines1.split()
    return kommalines1

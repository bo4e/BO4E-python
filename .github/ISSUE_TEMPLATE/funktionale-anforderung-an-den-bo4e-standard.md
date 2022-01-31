---
name: Funktionale Anforderung an den BO4E Standard
about: Eine Anforderung die so noch nicht vom BO4E Standard abgedeckt ist und/oder
  ein Vorschlag, wie sie abzubilden wäre
title: 'Ein aussagekräftiger Titel: Hunde- und Katzentarife können nicht abgebildet
  werden'
labels: BO4E Enhancement Proposal
assignees: ''

---

Bitte **möglichst kleinteilig** pro Problem oder Anmerkung genau ein Ticket eröffnen anstatt alle Probleme, Gedanken oder Verbesserungsvorschläge in ein Mega-Ticket zu verpacken. Das erleichtert die Umsetzung und Diskussion ganz massiv.

**Die fachliche Anforderung**

_Hier bitte kurz die Anforderung umschreiben. Z.B.:_
Ich will als Lieferant einen Tarif anbieten und abrechnen, der sich explizit an Haustierliebhaber richtet und nicht mehr leistungsgemessen oder pauschal abgerechnet wird, sondern dessen Grundpreis sich an der Anzahl der Haustiere in einem Haushalt orientiert. Das lässt sich in BO4E nicht abbilden.

**Gibt es schon eine Idee zur Umsetzung?**

_Hier als Text (oder gerne auch Pseudo-Code) einfügen, wie eine Lösung aussehen könnte; Z.B.:_
Das ENUM `Tarifart` soll um die Werte
* `KATZENTARIF`
* `HUNDETARIF`

erweitert werden.
Außerdem müssen dem BO `TARIF` zwei optionale Intergerfelder hinzugefügt werden, die die Anzahl der Katzen und Hunde im Haushalt beschreiben.

**Weitere Anmerkungen**

_Gerne alle Ideen oder Gedanken zum Thema hierhin schreiben._

# Datenbank

Es wurde sich vorgestellt, dass die Datenbank alle Produkte beinhaltet, die im
Webshop angeboten werden. Momentan arbeiten wir mit **Stripe** und dort muss
man ebenfalls Produkte im Developer Dashboard anlegen. Es wird angenommen, dass
auf der Datenbank die "originalen" Produkte liegen. Bedeutet: Wenn neue Produkte
angelegt oder bestehende Produkte bearbeitet / entfernt werden, muss gleichzeitig
vom Backend eine Anfrage an Stripe gesendet werden, damit dort die Daten ebenfalls
angepasst werden koennen. Dies gilt in der Zukunft natuerlich auch fuer andere **Payment Gateway** Anbieter.

Die Datenbank sollte auch die Lizen- und Kundendaten beinhalten.

## TODO

- [ ] Datenbank installieren und einrichten
- [ ] Datenbank Tabellen anlegen, eine Uebersicht der Tabellen findest du [hier]()
- [ ] Eine moeglichkeit finden, mit der Datenbank zu kommunizieren (Wahrscheinlich wird eine extra Datenbank API gebaut bzw. genutzt werden muessen)
- [ ] Die Oben beschriebene Besonderheit der Produkte muss implementiert werden
# app.py
from flask import Flask, render_template

app = Flask(__name__)

# Rotina organizada por tipo de dia
rotina = {
    "Dias Normais (chegada às 17:20)": [
        ("05:00 – 06:10", "Acordar, higiene, café, se arrumar"),
        ("06:10 – 08:00", "Deslocamento (podcasts ou videoaulas leves do ENEM)"),
        ("08:00 – 17:20", "Trabalho"),
        ("17:20 – 19:20", "Volta pra casa (relaxar, lanche leve)"),
        ("19:20 – 19:40", "Banho e jantar leve"),
        ("19:40 – 20:20", "Estudo ENEM (1 disciplina)"),
        ("20:20 – 20:35", "Lazer curto (15 min)"),
        ("20:35 – 21:15", "Estudo de Programação (40 min)"),
        ("21:15 – 21:25", "Calistenia (10 min)"),
        ("21:25 – 21:45", "Limpeza leve da casa"),
        ("21:45 – 22:00", "Relaxar, higiene noturna"),
        ("22:00", "Dormir")
    ],
    "Dias que chega cedo (14:00)": [
        ("14:00 – 14:30", "Chegada, lanche leve e relaxamento"),
        ("14:30 – 16:00", "Estudo ENEM (1h30)"),
        ("16:00 – 16:30", "Lazer / pausa ativa"),
        ("16:30 – 17:15", "Estudo de Programação (45 min)"),
        ("17:15 – 17:30", "Calistenia (15 min)"),
        ("17:30 – 18:00", "Limpeza leve da casa"),
        ("18:00 – 19:00", "Lazer ou hobby maior"),
        ("19:00 – 19:20", "Banho e jantar leve"),
        ("19:20 – 20:00", "Revisão ENEM / exercícios rápidos"),
        ("20:00 – 21:00", "Programação leve ou hobby criativo"),
        ("21:00 – 21:20", "Relaxar / higiene noturna"),
        ("21:20 – 22:00", "Lazer leve ou ritual de relaxamento"),
        ("22:00", "Dormir")
    ]
}

@app.route('/')
def index():
    return render_template('index.html', rotina=rotina)

if __name__ == "__main__":
    app.run(debug=True)

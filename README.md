# ⏳ Flowmodoro App (CLI Version)

> Um timer de estudos baseado no fluxo mental, não em tempos rígidos.

## 🧠 O Conceito
Diferente do Pomodoro tradicional, que obriga paradas a cada 25 minutos, o **Flowmodoro** foca no estado de *Flow*.
1. **Foco:** Você estuda o quanto aguentar. O cronômetro conta para cima (progressivo).
2. **Pausa:** Quando você cansa, o app calcula sua pausa baseada na regra de ouro: **Tempo de Foco / 5**.

Exemplo: Focou 50 minutos? Ganha 10 minutos de descanso.

## 🚀 Funcionalidades
- [x] Cronômetro progressivo (Start/Stop).
- [x] Cálculo automático de tempo de pausa.
- [x] Persistência de dados: Salva o histórico de estudos em `.csv`.
- [ ] Dashboard: Gráfico de evolução diária gerado com `Matplotlib`.
- [ ] Interface Gráfica (Tkinter).

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Matplotlib** (Para geração de gráficos)
- **CSV & Datetime** (Nativas do Python)

## 📂 Estrutura do Projeto
O projeto segue o padrão **MVC** (Model-View-Controller) simplificado:

flowmodoro_app/ 
├── main.py # Controller: Gerencia o fluxo do app e inputs do usuário 
    ├── timer_logic.py # Model: Toda a lógica matemática e de estado do timer 
    ├── dashboard.py # View (Analítica): Lê o CSV e gera os gráficos 
    ├── flow_history.csv # Database: Arquivo gerado automaticamente com o histórico 
    └── requirements.txt # Dependências do projeto


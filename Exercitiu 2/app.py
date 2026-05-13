from flask import Flask, render_template, request
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot', methods=['POST'])
def plot():
    df = pd.read_csv('data.csv')
    tip_grafic = request.form.get('tip')
    
    plt.figure(figsize=(10, 6))


    if tip_grafic == 'toate':
        plt.plot(df)
        plt.legend(df.columns)
    elif tip_grafic == 'primele':
        plt.plot(df.head(6))
        plt.legend(df.columns)
    elif tip_grafic == 'ultimele':
        y_val_ox = df['Durata'].tail(5)
        y_val_oy = df['Puls'].tail(5)
        plt.plot(y_val_ox, y_val_oy, 'x:b', label='Puls vs Durata')
        plt.xlabel('Durata [s]')
        plt.ylabel('Puls [bpm]')
            
    filepath = os.path.join('static', 'grafic.png')
    plt.savefig(filepath)
    plt.close()
    
    return render_template('index.html', imagine='grafic.png')

if __name__ == '__main__':
    app.run(debug=True)

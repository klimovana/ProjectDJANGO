import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Инициализация Dash-приложения
app = dash.Dash(__name__)

# Пример данных (замените на свои данные)
data = {
    "User": ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown"],
    "Waist Circumference": [32.5, 28.0, 30.2, 34.1],
    "Chest Circumference": [95.0, 88.5, 92.0, 98.5],
    "Torso Length": [60.0, 58.0, 59.5, 61.0],
    "Hip Circumference": [100.0, 95.0, 98.0, 102.0],
    "Leg Length": [110.0, 105.0, 108.0, 112.0],
    "Sleeve Length": [60.0, 58.0, 59.0, 61.0],
}
df = pd.DataFrame(data)


# Функция для создания графиков
def create_graph(df, x_column, y_column, title):
    """
    Создает bar chart с использованием Plotly Express.

    :param df: DataFrame с данными
    :param x_column: Название столбца для оси X
    :param y_column: Название столбца для оси Y
    :param title: Заголовок графика
    :return: Figure объект Plotly
    """
    return px.bar(df, x=x_column, y=y_column, title=title)


# Список параметров для графиков
graph_params = [
    {"y_column": "Waist Circumference", "title": "Waist Circumference by User"},
    {"y_column": "Chest Circumference", "title": "Chest Circumference by User"},
    {"y_column": "Torso Length", "title": "Torso Length by User"},
    {"y_column": "Hip Circumference", "title": "Hip Circumference by User"},
    {"y_column": "Leg Length", "title": "Leg Length by User"},
    {"y_column": "Sleeve Length", "title": "Sleeve Length by User"},
]

# Динамическое создание графиков
graphs = []
for i, params in enumerate(graph_params):
    fig = create_graph(df, x_column="User", y_column=params["y_column"], title=params["title"])
    graphs.append(
        dcc.Graph(
            id=f'graph-{i}',
            figure=fig,
            style={'width': '48%', 'display': 'inline-block', 'margin': '1%'}  # Стиль для сетки
        )
    )

# Макет приложения
app.layout = html.Div(children=[
    html.H1(children='User Measurements Dashboard', style={'textAlign': 'center', 'color': '#333'}),

    html.Div(children='''
        Dash: A web application framework for Python.
    ''', style={'textAlign': 'center', 'marginBottom': '20px'}),

    # Контейнер для графиков
    html.Div(children=graphs, style={'display': 'flex', 'flexWrap': 'wrap'})
])

# Запуск сервера
if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8050)

import altair as alt
from altair.datasets import data

movies = data.movies()
movies = movies.dropna(
    subset=[
        "Production Budget",
        "Worldwide Gross",
        "IMDB Rating",
        "Major Genre",
        "MPAA Rating",
    ]
)

scatter = (
    alt.Chart(movies)
    .mark_point()
    .encode(
        x="Production Budget:Q",
        y="Worldwide Gross:Q",
    )
)
scatter

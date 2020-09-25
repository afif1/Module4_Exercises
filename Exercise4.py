from sqlalchemy import create_engine
import pandas as pd

#Exercise 4a
engine = create_engine('sqlite:///database/Chinook.sqlite')

with engine.connect() as con:
    rs = con.execute("select Title, Name from Album inner join Artist on Album.ArtistID=Artist.ArtistID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    print(df)
con.close()

#Exercise 4b
df = pd.read_sql_query("select * from PlaylistTrack inner join Track on PlaylistTrack.TrackId=Track.TrackId where Milliseconds < 250000", engine)
print(df)

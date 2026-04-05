from sunpy.net import Fido, attrs as a
import sunpy.map
import matplotlib.pyplot as plt

result = Fido.search(
    a.Time("2014-10-21 06:00", "2014-10-21 07:00"),
    a.Instrument("HMI"),
    a.Physobs.intensity
)

downloaded_files = Fido.fetch(result[0,0:1])
map_hmi = sunpy.map.Map(downloaded_files[0])
map_hmi.plot()
plt.show()

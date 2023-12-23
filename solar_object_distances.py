from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, get_body
import numpy as np 
from datetime import datetime, timedelta
import matplotlib.pyplot as plt 

start_time = datetime(2000, 1, 1)
end_time = datetime(2020, 1, 1)
time_step = timedelta(days=1)

times = np.arange(start_time, end_time, time_step).astype(datetime)

astro_times = Time(times)

with solar_system_ephemeris.set("builtin"):
    neptune = get_body("neptune", astro_times)
    uranus = get_body("uranus", astro_times)
    saturn = get_body("saturn", astro_times)
    jupiter = get_body("jupiter", astro_times)
    mercury = get_body("mercury", astro_times)
    mars = get_body("mars", astro_times)
    earth = get_body("earth", astro_times)
    moon = get_body("moon", astro_times)
    venus = get_body("venus", astro_times)
    sun = get_body("sun", astro_times)

earth_to_mars = sun.separation_3d(mars).km
earth_to_venus = sun.separation_3d(venus).km
earth_to_mercury = sun.separation_3d(mercury).km
earth_to_jupiter = sun.separation_3d(jupiter).km
earth_to_saturn = sun.separation_3d(saturn).km
earth_to_uranus = sun.separation_3d(uranus).km
earth_to_neptune = sun.separation_3d(neptune).km
# earth_to_sun = earth.separation_3d(sun).km
# earth_to_moon = earth.separation_3d(moon).km
# sun_to_earth = sun.separation_3d(earth).km
# sun_to_mars = sun.separation_3d(mars).km

#plt.plot(times, earth_to_mars, "--", label="From Earth")
plt.plot(times, earth_to_mars, "--", label="to Mars")
plt.plot(times, earth_to_venus, "--", label="to Venus")
plt.plot(times, earth_to_mercury, "--", label="to Mercury")
plt.plot(times, earth_to_jupiter, "--", label="to Jupiter")
plt.plot(times, earth_to_saturn, "--", label="to Saturn")
plt.plot(times, earth_to_uranus, "--", label="to Uranus")
plt.plot(times, earth_to_neptune, "--", label="to Neptune")

plt.legend()
plt.xlabel("Time")
plt.ylabel("Distance (km)")
plt.title("Distance from Earth..")
#plt.savefig("earth_to_mars.png")
plt.show()
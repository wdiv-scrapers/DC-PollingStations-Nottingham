from dc_base_scrapers.hashonly_scraper import HashOnlyScraper


stations_url = "https://geoserver.nottinghamcity.gov.uk/opendata/geojson/ncc_Polling_Stations.json?t=636729712048460234"
council_id = 'E06000018'


stations_scraper = HashOnlyScraper(stations_url, council_id, 'stations', 'geojson')
stations_scraper.scrape()

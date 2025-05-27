# TODO (later)
# - Add a description that shows up on the widget?
# - Build this list programmatically based on LIO CSV?
# FM work in progress on this...
# - This: https://geohub.lio.gov.on.ca/datasets/lio::ontario-geohub-item-report/about
# - led me here: https://services9.arcgis.com/a03W7iZ8T3s5vB7p/ArcGIS/rest/services/Ontario_GeoHub_Item_Report_v2/FeatureServer/0
# - I used the query builder at the bottom to achieve this URL: https://services9.arcgis.com/a03W7iZ8T3s5vB7p/ArcGIS/rest/services/Ontario_GeoHub_Item_Report_v2/FeatureServer/0/query?where=url_slug+LIKE+%27https%3A%2F%2Fgeohub.lio%25%27+AND+item_type+%3D+%27Feature+Layer%27&outFields=publisher,agol_owner,item_title,snippet,data_url,url_slug,item_type&f=pjson
# - result is lio_list_TEMPFILE_proposed_new.json
# Further filtering likely required.

# The resulting list could be generated each time the plugin starts, but maybe we want a pre-built list as a fallback so that the whole plugin isn't reliant on the item-report service?
# But how often would we refresh the hard coded version, and what would trigger it?
# Doing it dynamically each time could be something like:
"""
import requests

url = "https://services9.arcgis.com/a03W7iZ8T3s5vB7p/ArcGIS/rest/services/Ontario_GeoHub_Item_Report_v2/FeatureServer/0/query"

params = {
    "where": "data_url LIKE 'https://ws.lioservices.lrc.gov.on.ca/arcgis2/rest/services/LIO_OPEN_DATA%' AND url_slug LIKE 'https://geohub.lio%' AND item_type = 'Feature Layer'",
    "outFields": "publisher,agol_owner,item_title,snippet,data_url,url_slug,item_type",
    "f": "json"  # or "pjson" for pretty formatting
}

response = requests.get(url, params=params)
data = response.json()

# Print sample
for feature in data.get("features", []):
    print(feature["attributes"]["item_title"])

"""


# 'snippet' and 'url_slug' should be shown to the user directly in the dialogue, on hover, or on click somehow.

# TODO AO, we could parse this list to update the existing lio_list, but that seems like an extra step. What do you think about refactoring how each data_url is accessed and called?





# TODO (now)
# - Define what the parts of each sub list are. 

lio_list = [
    ['33', 'Building as Symbol', '01'],
    ['28', 'Spot Height', '01'],
    ['27', 'Bathymetry Point', '01'],
    ['6', 'OHN Hydrographic Point', '01'],
    ['32', 'ORN Segment With Address', '01'],
    ['30', 'Bathymetry Line', '01'],
    ['29', 'Contour', '01'],
    ['9', 'OHN Hydrographic Line', '01'],
    ['7', 'Constructed Drain', '01'],
    ['14', 'OHN Shoreline', '01'],
    ['26', 'OHN Watercourse', '01'],
    ['35', 'Built Up Area', '01'],
    ['34', 'Building To Scale', '01'],
    ['31', 'Bathymetry Index', '01'],
    ['10', 'OHN Hydrographic Poly', '01'],
    ['11', 'Tile Drainage Area', '01'],
    ['15', 'Wetland With Significance', '01'],
    ['25', 'OHN Waterbody', '01'],
    ['2', 'Conservation Reserve Regulated', '03'],
    ['11', 'Conservation Authority Admin Area', '03'],
    ['15', 'Ecodistrict', '03'],
    ['16', 'Ecoregion', '03'],
    ['17', 'Ecozone', '03'],
    ['10', 'Federal Protected Area', '03'],
    ['12', 'Indian Reserve', '03'],
    ['1', 'Landform Conservation Area', '03'],
    ['6', 'MNR District', '03'],
    ['7', 'MNR Region', '03'],
    ['3', 'Municipal Park', '03'],
    ['14', 'Municipal Bnd Lower And Single', '03'],
    ['13', 'Municipal Bnd Upper And Dist', '03'],
    ['9', 'National Wildlife Area', '03'],
    ['8', 'OPS Region', '03'],
    ['5', 'Provincial Park Admin Zone', '03'],
    ['4', 'Provincial Park Regulated', '03'],
    ['0', 'Province', '03'],
    ['18', 'Site District', '03'],
    ['19', 'Site Region', '03'],
    ['19', 'Ontario Trail Network (OTN) Segment', '04'],
    ['20', 'Ontario Trail Network (OTN) Access Point', '04'],
    ['20', 'Emergency Management Historical Event', '05'],
    ['21', 'Fire Aviation and Emergency Facility Point', '05'],
    ['10', 'Utility Site', '05'],
    ['11', 'Utility Line', '05'],
    ['19', 'Aggregate Designated Area', '05'],
    ['18', 'Aggregate Inspector Jurisdiction', '05'],
    ['17', 'Aggregate Site Authorized Active', '05'],
    ['16', 'Aggregate Site Authorized Inactive', '05'],
    ['23', 'Aggregate Site Authorized Partial Surrender', '05'],
    ['24', 'Aggregate Extraction Area', '05'],
    ['25', 'Aggregate Site Unrehabilitated', '05'],
    ['0', 'Airport Official', '05'],
    ['1', 'Airport Other', '05'],
    ['3', 'ANSI', '05'],
    ['15', 'Cadastral Location', '05'],
    ['8', 'Caribou Range Boundary', '05'],
    ['7', 'Crown Game Preserve', '05'],
    ['14', 'Designated Gas Storage Area', '05'],
    ['13', 'Fire Management Agreement Area', '05'],
    ['12', 'Fire Response Plan Area', '05'],
    ['9', 'Soil Survey Complex', '05'],
    ['2', 'Source Protection Area Generalized', '05'],
    ['5', 'Wildlife Management Unit', '05'],
    ['16', 'Greenbelt Hamlet', '06'],
    ['18', 'Greenbelt River Valley Connection', '06'],
    ['4', 'CLUPA Overlay', '06'],
    ['5', 'CLUPA Provincial', '06'],
    ['0', 'Federal Land Other', '06'],
    ['20', 'Greenbelt Towns Villages', '06'],
    ['19', 'Greenbelt Specialty Crop', '06'],
    ['17', 'Greenbelt Outer Boundary', '06'],
    ['15', 'Greenbelt Designation', '06'],
    ['1', 'Geographic Township Improved', '06'],
    ['21', 'Lake Simcoe PAW Boundary', '06'],
    ['2', 'Lot Fabric Improved', '06'],
    ['22', 'Natural Heritage System Area', '06'],
    ['23', 'NGO Nature Reserve', '06'],
    ['27', 'Niagara Escarpment Policy Area', '06'],
    ['24', 'Niagara Escarpment Minor Urban Centre', '06'],
    ['25', 'Niagara Escarpment Plan Boundary', '06'],
    ['26', 'Niagara Escarpment Plan Designation', '06'],
    ['29', 'ORM Planning Area', '06'],
    ['28', 'ORM Land Use Designation', '06'],
    ['22', 'Forest Processing Facility', '07'],
    ['0', 'Aquatic Resource Area Survey Point', '07'],
    ['15', 'Fishing Access Point', '07'],
    ['1', 'ARA Water Line Segment', '07'],
    ['13', 'Fish Pathogen Boundary Source', '07'],
    ['10', 'Fish Culture Operation MNR', '07'],
    ['33', 'Fish Culture Operation Areas of Impact', '07'],
    ['3', 'Bait Harvest Area', '07'],
    ['2', 'ARA Water Poly Segment', '07'],
    ['12', 'Fish Pathogen Management Zone', '07'],
    ['14', 'Fisheries Management Zone', '07'],
    ['31', 'Fish Activity Area', '07'],
    ['16', 'Forest Abiotic Damage Event', '07'],
    ['17', 'Forest Disease Damage Event', '07'],
    ['18', 'Forest Genetics Zone', '07'],
    ['19', 'Forest Insect Damage Event', '07'],
    ['20', 'Forest Management Unit', '07'],
    ['21', 'Forest Misc Damage Event', '07'],
    ['23', 'Forest Resource Inventory Status', '07'],
    ['25', 'Provincially Tracked Species 1km Grid', '07'],
    ['29', 'Wooded Area', '07'],
    ['0', 'Ontario Road Network', '09']

    ]

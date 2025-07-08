---
title: Manage data about sensitive localities
status: draft
topics:
- manage data
- sensitive locality
- georeference
---
Restricting locality data
Specific locality information may be restricted for some or all paleontological specimens due to federal regulations as well as the preferences of private landowners. 

If coordinates need to be shared with less precision than the data available
- Information should be truncated
    - Do not round or randomize numbers
- The recommendation is to truncate to a tenth of a degree equivalent 
    - Similar to being as specific as a city name
- Remove any other descriptive locality information that would compromise the more specific location

If any locality data is restricted data providers using Darwin Core should share the terms 'informationWithheld' and 'dataGeneralizations'.

'informationWithheld' - Explanation of restriction can be included here. Examples: "More data may be available" or "Locality description is available to researchers upon request."

'dataGeneralizations' - Essential term to include if an institution does not serve the most specific decimal latitude/longitude available for a specimen. Example: "Latitude and longitude reported at maximum precision of 0.1 degrees."

{% include resource_list topics='sensitive locality' %}

select
    incident_date,
    battalion,
    neighborhood_district,
    count(*) as total_incidents
from source_data
group by incident_date, battalion, neighborhood_district
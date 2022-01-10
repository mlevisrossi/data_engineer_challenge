select
    date(incident_date) as incident_date,
    battalion,
    neighborhood_district,
    count(*) as total_incidents
from {{ source('postgres', 'incidents') }}
group by incident_date, battalion, neighborhood_district
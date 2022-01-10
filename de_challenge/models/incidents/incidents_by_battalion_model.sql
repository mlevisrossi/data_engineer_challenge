select
    battalion,
    count(*) as total_incidents
from {{ source('postgres', 'incidents') }}
group by battalion
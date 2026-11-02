# Employee shuttle modeling checks

## Ask what may change

Home-to-stop assignment, stop placement, stop-to-bus assignment, visit order and departure times are different decisions. Establish which are supplied and which are optimized. A fixed-stop CVRP does not solve station selection or pedestrian access. A nearest-stop assignment may violate capacity, walking eligibility or work shifts.

Determine whether routes start at a bus depot, a first pickup or a company; whether they end at a company, a depot or elsewhere; and whether the return trip is charged. Morning pickups and evening dropoffs can need different models and matrices. A bus running several trips requires temporal compatibility, unloading/reset and non-overlap checks, not duplicate independent copies with unconstrained availability.

## Coverage and capacity

Represent employee identity separately from coordinates. Two people at the same point remain two demand records; a shared stop aggregates only their demand. Preserve the employee-to-stop-to-bus mapping so coverage can be checked against the original employees. Document optional travel explicitly; all-employee service cannot be made optional by adding penalties.

For all pickups and unloading only at the terminal, cumulative demand rises along the route. For all deliveries from a depot, initial load is the total and decreases. Mixed pickup/dropoff, transfers or several destinations require load and precedence at each event; route demand totals alone are insufficient. Wheelchair seats, vehicle eligibility or group cohesion matter only if the assignment specifies them and need corresponding constraints.

## Time and fairness

Keep travel, arrival, waiting, boarding/service, departure and final arrival distinct. A stop window may constrain service start or completion: use the assignment's semantics. Company arrival deadlines apply to the actual final leg too. Some windows permit waiting and some models restrict it; do not assume either silently.

Maximum route duration includes the required components, but it is not an individual passenger's ride time. A rider boarded at stop k has a different duration from one at the last stop; include any post-boarding waits according to the contract. Walking distance/time and vehicle travel are different matrices. Average time can hide extreme commutes; enforce a maximum or fairness measure only when required or explicitly chosen.

## Explain the objective

Reducing bus count, total distance, total passenger time and the longest commute are different goals. Preserve stated priority/weights. Compare feasible solutions on the same metrics; report a heuristic best-found result without claiming a global optimum. Show load, served count, travel/service/wait time, arrival, and unserved/violations at the granularity the actual problem needs.

## Failure probes

- One group larger than every bus; sufficient total capacity but impossible indivisible assignment.
- Shared coordinates with distinct employees; demand cannot vanish through deduplication.
- A required directed arc is unreachable; missing travel cannot become zero.
- Capacity-feasible route arrives after the company deadline because waiting/service was omitted.
- Local route improvement that duplicates or loses an employee during reassignment.
- A visually shorter line with higher directed travel cost or unacceptable ride time.
- A timeout without a solution versus a proven contradiction in the submitted model.

Keep actual task data local. Build the required UI in the provided stack, with participant-only preview operation. A map, attractive polyline or solver objective number alone does not establish a working service or a correct assignment.

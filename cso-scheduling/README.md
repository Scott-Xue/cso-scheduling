# cso-scheduling

Purpose of this project is to optimize a work schedule for cso workers given their preferences for shifts and a shift schedule. We want to output an assignment of workers to shifts that satisfies given constraints:
1. Min/max shifts for each worker
2. Qualifications for certain shifts need to be met
3. Require essential shifts to be satisfied
4. Minimum employees per shift
5. Employee availability for each shift
We want to maximize "utility", which we will define as a person's preference for a certain shift (higher the number, the higher the preference) times his/her rank. We believe a linear program is suitable for this problem, and furthermore, because the problem can be formulated as a network flow problem with integer capacities, we are guaranteed integer solutions.
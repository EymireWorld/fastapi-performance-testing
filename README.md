Suggest your options on how to increase the performance of this "application", it's interesting to learn something new.
Please don't mention caching, I already know about it.
Idk why Tiangolo recommend using only uvicorn, I really don't understand why.

gunicorn + uvicorn workers:
```
TOTAL RESULTS

checks_total.......: 834597  2781.533211/s
checks_succeeded...: 100.00% 834597 out of 834597
checks_failed......: 0.00%   0 out of 834597

✓ status was 200

HTTP
http_req_duration..............: avg=71.78ms min=7.01ms med=64.71ms max=1.44s p(90)=102.87ms p(95)=120.12ms
  { expected_response:true }...: avg=71.78ms min=7.01ms med=64.71ms max=1.44s p(90)=102.87ms p(95)=120.12ms
http_req_failed................: 0.00%  0 out of 834597
http_reqs......................: 834597 2781.533211/s

EXECUTION
iteration_duration.............: avg=71.88ms min=7.01ms med=64.81ms max=1.44s p(90)=102.97ms p(95)=120.21ms
iterations.....................: 834597 2781.533211/s
vus............................: 200    min=200         max=200
vus_max........................: 200    min=200         max=200

NETWORK
data_received..................: 154 MB 514 kB/s
data_sent......................: 68 MB  225 kB/s

```
uvicorn:
```
TOTAL RESULTS

checks_total.......: 715935  2385.974577/s
checks_succeeded...: 100.00% 715935 out of 715935
checks_failed......: 0.00%   0 out of 715935

✓ status was 200

HTTP
http_req_duration..............: avg=83.7ms min=8.03ms med=69.06ms max=1.55s p(90)=129.69ms p(95)=154.62ms
  { expected_response:true }...: avg=83.7ms min=8.03ms med=69.06ms max=1.55s p(90)=129.69ms p(95)=154.62ms
http_req_failed................: 0.00%  0 out of 715935
http_reqs......................: 715935 2385.974577/s

EXECUTION
iteration_duration.............: avg=83.8ms min=8.03ms med=69.16ms max=1.55s p(90)=129.79ms p(95)=154.71ms
iterations.....................: 715935 2385.974577/s
vus............................: 200    min=200         max=200
vus_max........................: 200    min=200         max=200

NETWORK
data_received..................: 132 MB 441 kB/s
data_sent......................: 58 MB  193 kB/s
```